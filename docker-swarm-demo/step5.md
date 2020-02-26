To get deatils about any service using `inspect` command. 
To get JSON view, run `docker service inspect test`{{execute T1}} and for YAML response, run `docker service inspect test`{{execute T1}}

To add more tasks to a service, you can run `scale` command as follows
`docker service scale test=5`{{execute T1}}