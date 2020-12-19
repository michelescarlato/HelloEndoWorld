sudo helm install helloendoworld-chart helloendoworld-chart/ --values helloendoworld-chart/values.yaml
export NODE_PORT=$(sudo kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services helloendoworld-chart)
export NODE_IP=$(sudo kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT

export POD_NAME=$(sudo kubectl get pods -l "app.kubernetes.io/name=helloendoworld-chart,app.kubernetes.io/instance=helloendoworld-chart" -o jsonpath="{.items[0].metadata.name}")

sudo kubectl describe pod

sudo kubectl get pod
sleep 60
sudo kubectl port-forward $POD_NAME 8080:8080
#curl http://121.179.158.56:8080/helloworld
#sudo helm uninstall helloendoworld-chart
#sudo kubectl delete ns my-first-terraform-namespace
