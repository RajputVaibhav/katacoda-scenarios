First we initialize a cluster using `docker swarm init`{{execute T1}}

After execution, you should see a command to join the cluster.
It should look something like `docker swarm join --token <token> <IP>:<port>`

Run that command on second terminal to join the cluster or just run the below mention commands

This should display the token needed to join the cluster `token=$(ssh -o StrictHostKeyChecking=no 172.17.0.96 "docker swarm join-token -q worker") && echo $token`{{execute T1}}

And this should join the second node to the cluster `docker swarm join 172.17.0.96:2377 --token $token`{{execute T2}}
