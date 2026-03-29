# camera_parser
##Python-скрипт для захвата и записи видео с IP/USB камер с использованием OpenCV. 
Поддерживает сохранение в различные форматы, корректное 
освобождение ресурсов. Скрипт разработан под linux дистрибьютивы.
Для корректной работы необходимо установить следующие библиотеки и пакеты (debian):
```bash
pip3 install opencv-python diffusers ultralytics 
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2
```
Для работы на linux (debian) необходима установка rocm:
```bash
sudo apt update && sudo apt upgrad
sudo usermod -a -G render,video $LOGNAME
sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
sudo apt install python3-setuptools python3-wheel
wget https://repo.radeon.com/amdgpu-install/6.3.3/ubuntu/noble/amdgpu-install_6.3.60303-1_all.deb
sudo apt install ./amdgpu-install_6.3.60303-1_all.deb
sudo amdgpu-install --usecase=rocm
sudo reboot
```
Для проверки rocm: 
```bash
rocminfo
```
Также нужно создать виртуальное окружение:
```bash
python3 -m venv venv
```
Запуск:
```bash
python3 название_файла
```
Если вы используете скрипт для ip камеры, то не забудьте установить свой адрес камеры.
