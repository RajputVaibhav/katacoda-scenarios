# Populating the CVE database

We know that Clair downloads the CVE data on regular intervals but the first pull can take some time, so we will that manually.

<br/>

First download the data 

`curl -LO https://gist.githubusercontent.com/BenHall/34ae4e6129d81f871e353c63b6a869a7/raw/5818fba954b0b00352d07771fabab6b9daba5510/clair.sql`{{execute}}

<br/>

And the push that data into postgres using

```
docker run -it \
    -v $(pwd):/sql/ \
    --network "${USER}_default" \
    --link clair_postgres:clair_postgres \
    postgres:latest \
        bash -c "PGPASSWORD=password psql -h clair_postgres -U postgres < /sql/clair.sql"
```{{execute}}