# Installing docker and adding user to docker group
sudo apt install -y docker.io
sudo usermod -a -G docker $USER
sudo reboot
