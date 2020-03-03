<br/>

# Create a Dockerfile in sa-webapp


- Set Java home using `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre`{{execute}}
- Go to webapp directory using `cd ~/container-microservice-app/sa-webapp`{{execute}} and build using `mvn clean install`{{execute}}
- Start with `openjdk:8-jdk-alpine` image
- Add `target/sentiment-analysis-web-0.0.1-SNAPSHOT.jar` at default path in the container
- Expose `8080` port
- Run `java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar --sa.logic.api.url=${SA_LOGIC_API_URL}"` command in the container


<br/>


---


Build image using from Dockerfile


Sample command: `docker build -t sa-webapp .`

<br/>



Now run the webapp container which will call the logic container at https://[[HOST_SUBDOMAIN]]-5000-[[KATACODA_HOST]].environments.katacoda.com


To configure this, pass the `SA_LOGIC_API_URL` environment variable with the https://[[HOST_SUBDOMAIN]]-5000-[[KATACODA_HOST]].environments.katacoda.com URL
Sample command: `docker run -d -p 8080:8080 -e SA_LOGIC_API_URL= <sa-logic container URL here> sa-webapp`

<br/>

Use `docker ps`{{execute}} to see the running containers
