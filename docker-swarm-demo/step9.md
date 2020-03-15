## BUILD DOCKER IMAGES

Build monitored subject image using

`docker build -t subject -f Dockerfile-subject .`{{execute}}

<br/>

---

<br/>

Build exposing api image using

`docker build -t api -f Dockerfile-flask .`{{execute}}

<br/>

---

<br/>

Edit `script.js` and replace the `http://localhost:5050/` in line 10 with https://[[HOST_SUBDOMAIN]]-5050-[[KATACODA_HOST]].environments.katacoda.com



Now, build frontend image using

`docker build -t frontend -f Dockerfile-frontend .`{{execute}}


## CREATE OVERLAY NETWORK


<br/>

Create an overlay network using `docker network create --driver overlay <network-name>`