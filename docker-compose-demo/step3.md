## CREATE COMPOSE FILE

<pre class="file" data-filename="docker-compose.yml" data-target="replace">
version: '3'
services:
  logical-name:
    image: image-name
    ports:
      - "host-port:container-port"
    volumes:
      - 'host-path:container-path'
    networks:
      - network-name

networks:
  network-name:
    driver: bridge
</pre>

Use the above mentioned format to create the `docker-compose.yml` file

When the `docker-compose.yml` file is ready, run `docker-compose up`{{execute}}

<br/>

Once the containers are ready, you should be able to view the app at https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com