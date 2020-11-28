sudo kubectl apply -f helloendoworld-kubernetes.yaml && sleep 1
sudo kubectl get deployments helloendoworld && sleep 1
sudo kubectl describe deployments helloendoworld && sleep 1
sudo kubectl get replicasets && sleep 1
sudo kubectl describe replicasets && sleep 1
sudo kubectl expose deployment helloendoworld --type=NodePort --name=helloendoworld-service && sleep 1
# take the NodePort number
sudo kubectl describe services helloendoworld-service && sleep 1
sudo kubectl get pods --selector="run=load-balancer-example" --output=wide && sleep 1
sudo kubectl describe services helloendoworld-service | grep NodePort && sleep 1 
