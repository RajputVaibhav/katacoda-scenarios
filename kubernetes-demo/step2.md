`kubeadm init`{{execute T1}}


This will give you a join command similar to 



`kubeadm join <IP>:<port> --token <token> \
    --discovery-token-ca-cert-hash <sha hash>`


Run this command in second terminal to join the cluster


`export KUBECONFIG=/etc/kubernetes/admin.conf`{{execute T1}}
