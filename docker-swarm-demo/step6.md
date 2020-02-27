In this section, we will be deploying a Prometheus service and see how it works.

Edit the file at `/etc/docker/daemon.json` to add the follwing entries

___
`{
  "metrics-addr" : "127.0.0.1:9323",
  "experimental" : true
}`
___

Save and exit the file.


Next, go to `/tmp/prometheus.yml` file and add the following content in it

___


<pre>
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.

  external_labels:
      monitor: 'codelab-monitor'

rule_files:
  # - "first.rules"
  # - "second.rules"

scrape_configs:
  - job_name: 'prometheus'

    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'docker'

    static_configs:
      - targets: ['localhost:9323']
</pre>


___

Now, start a single-replica Prometheus service using this configuration

`docker service create --replicas 1 --name my-prometheus \
    --mount type=bind,source=/tmp/prometheus.yml,destination=/etc/prometheus/prometheus.yml \
    --publish published=9090,target=9090,protocol=tcp \
    prom/prometheus`{{execute T1}}


Once the service is deployed, you should be able to access the Prometheus Dashboard at 

https://[[HOST_SUBDOMAIN]]-9090-[[KATACODA_HOST]].environments.katacoda.com
