# Installing minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_1.4.0.deb
sudo dpkg -i minikube_1.4.0.deb
#sudo minikube config set vm-driver none
minikube config set driver docker
sudo minikube start
sudo chown -R $USER $HOME/.kube $HOME/.minikube
#curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
#chmod +x ./kubectl
#sudo mv ./kubectl /usr/local/bin/kubectl
sudo kubectl get po -A
