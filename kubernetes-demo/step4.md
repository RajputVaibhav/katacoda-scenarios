## HELM AND TILLER


`curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v2.8.2-linux-amd64.tar.gz
tar -xvf helm-v2.8.2-linux-amd64.tar.gz
mv linux-amd64/helm /usr/local/bin/`{{execute T1}}

# Helm Installation


`curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > get_helm.sh`{{execute T1}}


`chmod u+x get_helm.sh`{{execute T1}}


`./get_helm.sh`{{execute T1}}


`helm version`{{execute T1}}


# Tiller Installation


`kubectl -n kube-system create serviceaccount tiller`{{execute T1}}


`kubectl create  clusterrolebinding tiller --clusterrole=cluster-admin --serviceaccount=kube-system:tiller`{{execute T1}}


`helm init --service-account tiller`{{execute T1}}


`helm version`{{execute T1}}
