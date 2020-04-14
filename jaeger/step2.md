Now we deploy the ride-on-demand demo application. This demo application consists of several microservices and is a good use-case to illustrates the use of the OpenTracing API. You can find more details about this application at https://github.com/jaegertracing/jaeger/tree/master/examples/hotrod

<br/>

Use the following command to start the application.

```
docker run --rm -it \
  --link jaeger -p8080-8083:8080-8083 \
  jaegertracing/example-hotrod:1.3 \
  --jaeger-agent.host-port=jaeger:6831
```{{execute}}

<br/>

Once deployed, you can use access the application dashboard at 

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com

<br/>

Move to next step to see how to use the application.