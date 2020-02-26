First we initialize a cluster using `docker swarm init`{{execute T1}}

After execution, you should see a command to join the cluster.
It should look something like `docker swarm join --token <token> <IP>:<port>`

Run that command on second terminal to join the cluster.
