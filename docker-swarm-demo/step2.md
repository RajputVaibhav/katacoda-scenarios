To list the nodes in the cluster, run `docker node ls`{{execute T1}}

You can also view the join commands post creation of cluster using the following commands

Worker `docker swarm join-token worker`{{execute T1}}

Worker `docker swarm join-token manager`{{execute T1}}
