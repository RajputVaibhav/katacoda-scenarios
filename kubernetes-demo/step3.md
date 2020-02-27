## Dashboard Web UI

`DOWNLOAD_URL=$(curl --silent "https://api.github.com/repos/kubernetes-sigs/metrics-server/releases/latest" | jq -r .tarball_url)`{{execute T1}}


`DOWNLOAD_VERSION=$(grep -o '[^/v]*$' <<< $DOWNLOAD_URL)`{{execute T1}}


`curl -Ls $DOWNLOAD_URL -o metrics-server-$DOWNLOAD_VERSION.tar.gz`{{execute T1}}


`mkdir metrics-server-$DOWNLOAD_VERSION`{{execute T1}}


`tar -xzf metrics-server-$DOWNLOAD_VERSION.tar.gz --directory metrics-server-$DOWNLOAD_VERSION --strip components 1`{{execute T1}}


`kubectl apply -f metrics-server-$DOWNLOAD_VERSION/deploy/1.8+/`{{execute T1}}


`kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta4/aio/deploy/recommended.yaml`{{execute T1}}


`kubectl apply -f eks-admin-service-account.yaml`{{execute T1}}


`kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')`{{execute T1}}


`kubectl proxy`{{execute T1}}

