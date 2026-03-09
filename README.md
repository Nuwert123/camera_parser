# camera_parser
##Python-скрипт для захвата и записи видео с IP/USB камер с использованием OpenCV. 
Поддерживает сохранение в различные форматы, корректное 
освобождение ресурсов. Скрипт разработан по linux дистрибьютивы.
##Установка зависимостей
Для корректной работы необходимо установить следующие библиотеки:
1.```pip3 install opencv-python diffusers ultralytics ```
2.```pip3 install pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2 ```
Для работы на linux (debian) необходима установка rocm:
1.```sudo apt update && sudo apt upgrade```
2.```sudo usermod -a -G render,video $LOGNAME```
3.```sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"```
4.```sudo apt install python3-setuptools python3-wheel```
5.```wget https://repo.radeon.com/amdgpu-install/6.3.3/ubuntu/noble/amdgpu-install_6.3.60303-1_all.deb```
6.```sudo apt install ./amdgpu-install_6.3.60303-1_all.deb```
7.```sudo amdgpu-install --usecase=rocm```
8.```sudo reboot```
Для проверки: 
1.```rocminfo```

