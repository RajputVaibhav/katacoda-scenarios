On terminal, execute `docker login [[HOST_IP]]`{{execute}} to configure docker cli to use the Harbor registry. Use your credentials to log in.

<br/>

Create a project and give it a name

<br/>

Now try pushing an image to this registry, say ubuntu. You can view the local images using `docker images`{{execute}}

If you don't have ubuntu image, pull it from DockerHub using `docker pull ubuntu`{{execute}}

<br/>

Now, tag the image using `docker tag ubuntu [[HOST_IP]]/<project-name>/ubuntu` command. Make sure you replace `<project-name>` with the project name.

<br/>

Once tagged, push the image to the Harbor registry using `docker push [[HOST_IP]]/<project-name>/ubuntu` command.