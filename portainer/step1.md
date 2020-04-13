First, we create a volume which will be bound to the Portainer container. This will be helpful in persisting the data in case of a restart or an upgrade.

`docker volume create portainer_data`{{execute}}

---

Second, we deploy the Portainer container.


`docker run -d -p 9000:9000 -p 8000:8000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer`{{execute}}