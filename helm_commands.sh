#!/bin/bash
TIMER=60

sudo helm install helloendoworld-chart helloendoworld-chart/ --values helloendoworld-chart/values_no_nginx.yaml
export NODE_PORT=$(sudo kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services helloendoworld-chart)
export NODE_IP=$(sudo kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT

export POD_NAME=$(sudo kubectl get pods -l "app.kubernetes.io/name=helloendoworld-chart,app.kubernetes.io/instance=helloendoworld-chart" -o jsonpath="{.items[0].metadata.name}")

sudo kubectl describe pod

sudo kubectl get pod

echo "Waiting $TIMER seconds"
sleep $TIMER
echo "$TIMER seconds passed"
touch port_forwarding.log
sudo kubectl port-forward $POD_NAME 8080:8080 > port_forwarding.log &
sleep 5


counter=1
until [ $counter -gt 10 ]
do
  echo "$counter test the HTTP server on /helloworld endpoint"
  curl http://localhost:8080/helloworld
  curl http://localhost:80/helloworld
  sleep 2
  let "counter++"
done

sudo bg >> port_forwarding.log
echo "-------grep-----------------"  >> port_forwarding.log
sudo ps aux | grep "kubectl port-forward" >> port_forwarding.log
echo "-------pkill-----------------"  >> port_forwarding.log
sudo pkill "kubectl port-forward" >> port_forwarding.log
echo "------killall-------------------"  >> port_forwarding.log
trap "killall background" EXIT  >> port_forwarding.log
echo "---------grep again------"  >> port_forwarding.log
sudo ps aux | grep kubectl port-forward >> port_forwarding.log
echo "----------------------------"  >> port_forwarding.log

sudo helm uninstall helloendoworld-chart
cat port_forwarding.log
sudo cp port_forwarding.log ../port_forwarding.log

exit 0

#sudo helm uninstall helloendoworld-chart
#sudo kubectl delete ns my-first-terraform-namespace
