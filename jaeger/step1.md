We start by deploying the Jaeger container. We will port-mapping its 5775 and 16686 ports.

5775 port is used to collect metrics from the application

16686 port is used to view the dashboard

<br/>

```
docker run -d --name jaeger \
  -p 5775:5775/udp -p 16686:16686 \
  jaegertracing/all-in-one:latest
```{{execute}}

<br/>

Once the command runs successfully, you should be able to view the dashboard at

https://[[HOST_SUBDOMAIN]]-16686-[[KATACODA_HOST]].environments.katacoda.com