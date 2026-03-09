import os
from random import randint
import cv2, time

# URL потока IP-камеры (RTSP или HTTP)
stream_url = 'rtsp://admin:admin@192.168.1.126:554/av0_1'
local_time = time.localtime()
cm = []

cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.126:554/av0_1')
if not cap.isOpened(): exit("Ошибка подключения")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False
start_time = None
hour = local_time.tm_hour
lines = []
while True:
    if len(cm) == 2:
        cm.clear()

    t = time.localtime()

    is_recording_time = (6 <= hour < 10) or (15 <= hour < 17)

    if not recording and is_recording_time:
        out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 352))
        recording = True
        start_time = time.time()
        print("Запись начата")

    if recording:
        ret, frame = cap.read()
        if ret:
            out.write(frame)

        if not is_recording_time:
            out.release()
            recording = False
            print("Запись завершена")

            x = randint(1, 10000000)
            y = randint(1, 10000000)
            os.environ["HSA_OVERRIDE_GFX_VERSION"] = "10.3.0"
            os.environ["HIP_VISIBLE_DEVICES"] = "0"
            os.environ["TORCH_BLAS_PREFER_HIPBLASLT"] = "0"

            from ultralytics import YOLO
            import cv2

            model = YOLO('yolov8n.pt')
            cap = cv2.VideoCapture('output.mp4')
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(f'test{x}-{y}.mp4', fourcc, fps, (width, height))
            unique_ids = set()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                results = model.track(frame, classes=[0], conf=0.3, persist=True, verbose=False)
                if results[0].boxes.id is not None:
                    track_ids = results[0].boxes.id.cpu().numpy().astype(int)
                    for track_id in track_ids:
                        unique_ids.add(track_id)
                annotated_frame = results[0].plot()
                cv2.putText(annotated_frame, f"people: {len(unique_ids)}", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('People Counter', annotated_frame)  # опционально
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                out.write(annotated_frame)
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            print(f"Уникальных людей : {len(unique_ids)}")
            file_path = 'main1.txt'
            if os.path.exists(file_path):
                pass
            else:
                os.system("touch main.txt")
            if len(cm) == 0 or len(cm) == 1:
                cm.append(len(unique_ids))
            if len(cm) == 2:
                n = abs(cm[0] - cm[1])
                lines = [f"Уникальных людей : {len(unique_ids)}\n, осталось в школе:{n}",
                         f'hour={local_time.tm_hour} day={local_time.tm_mday} moth={local_time.tm_mon}', "\n"]
            if len(cm) == 1:
                lines = [f"Уникальных людей : {len(unique_ids)}\n",
                         f'hour={local_time.tm_hour} day={local_time.tm_mday} moth={local_time.tm_mon}', "\n"]
            with open('main.txt', 'a', encoding='utf-8') as file:
                file.writelines(lines)
            os.system('rm -rf output.mp4')
