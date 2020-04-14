# Setting up the database

Let us start by creating the database for storing the Common Vulnerabilities and Exposures (CVE) data.

<br/>

---

First we begin by downloading a few files

<br/>

Postgres docker-compose file for storing CVE rules in the database:

`curl -LO https://raw.githubusercontent.com/coreos/clair/05cbf328aa6b00a167124dbdbec229e348d97c04/contrib/compose/docker-compose.yml`{{execute}}

<br/>

Clair configuration file which defines how the images will be scanned, we will storing it in a `clair_config` folder so that it can mount in the clair container at the correct location:

`mkdir clair_config && curl -L https://raw.githubusercontent.com/coreos/clair/master/config.yaml.sample -o clair_config/config.yaml`{{execute}}

---

Now we make a few changes in the downloaded files.

<br/>

First change is to replace `clair-git:latest` image in `docker-compose.yml` file with a stable `clair:v2.0.1`.

`sed 's/clair-git:latest/clair:v2.0.1/' -i docker-compose.yml`{{execute}}

<br/>

Second change is to replace the `host` value from `localhost` to `postgres` and add a section of `password` with value `password` in `clair_config/config.yaml`

`sed 's/host=localhost/host=postgres password=password/' -i clair_config/config.yaml`{{execute}}

---

Now our files are ready to be used. So start the compose using the following command.

`docker-compose up -d postgres`{{execute}}