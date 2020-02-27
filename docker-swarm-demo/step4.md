Now, lets create our first service.

Run the following command to create a service named test within the network net1 (which we just created) which runs 2 tasks of nginx image and map their http port to hosts port
`docker service create --name test --network net1 --replicas 2 -p 80:80 nginx`{{execute T1}}

Once created, you can view the service using `docker service ls`{{execute T1}}

Also, you can run view the containers running on first host using the command `docker ps`{{execute T1}} and on the second host using the command `docker ps`{{execute T2}}

Furthermore, you can curl on the hosts using their hostnames, `host01` and `host02` from either hosts to see the nginx welcome page.
On first host, run 
`curl host01`{{execute T1}}
`curl host02`{{execute T1}}
And on second host, run
`curl host01`{{execute T2}}
`curl host02`{{execute T2}}

You can also access the Welcome page at https://[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com
