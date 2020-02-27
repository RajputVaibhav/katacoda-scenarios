## PROMETHEUS AND GRAFANA INSTALLATION

`helm install stable/prometheus-operator --name prometheus-operator --namespace monitoring`{{execute T1}}


`kubectl port-forward -n monitoring prometheus-prometheus-operator-prometheus-0 9090`{{execute T1}}


`kubectl port-forward $(kubectl get pods --selector=app=grafana -n monitoring --output=jsonpath="{.items..metadata.name}") -n monitoring 3000`{{execute T1}}

