sudo kubectl apply -f helloendoworld-kubernetes-job.yaml && sleep 1
sudo kubectl get job helloendoworld-job && sleep 1
sudo kubectl describe job helloendoworld-job && sleep 1
#sudo kubectl get replicasets && sleep 1
#sudo kubectl describe replicasets && sleep 1

# take the NodePort number
#sudo kubectl describe services helloendoworld-service && sleep 1
sudo kubectl get pods --output=wide && sleep 1
#sudo kubectl describe services helloendoworld-service | grep NodePort && sleep 1
