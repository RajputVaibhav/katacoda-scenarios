## PROMETHEUS AND GRAFANA INSTALLATION

`helm install stable/prometheus-operator --name prometheus-operator --namespace monitoring`{{execute T1}}


`kubectl port-forward -n monitoring prometheus-prometheus-operator-prometheus-0 9090`{{execute T1}}


`kubectl port-forward $(kubectl get pods --selector=app=grafana -n monitoring --output=jsonpath="{.items..metadata.name}") -n monitoring 3000`{{execute T1}}


Access Prometheus at https://[[HOST_SUBDOMAIN]]-9090-[[KATACODA_HOST]].environments.katacoda.com


Access Grafana at https://[[HOST_SUBDOMAIN]]-3000-[[KATACODA_HOST]].environments.katacoda.com
