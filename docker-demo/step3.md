<br/>

# Create a Dockerfile in sa-webapp


- Set Java home using `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre`{{execute}}
- Go to webapp directory using `cd ~/container-microservice-app/sa-webapp`{{execute}} and build using `mvn clean install`{{execute}}
- Start with `openjdk:8-jdk-alpine` image
- Set environment variable `SA_LOGIC_API_URL` with value `http://localhost:5000`
- Add `target/sentiment-analysis-web-0.0.1-SNAPSHOT.jar` at default path in the container
- Expose `8080` port
- Run `java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar --sa.logic.api.url=${SA_LOGIC_API_URL}"` command in the container


<br/>


---


Build image using from Dockerfile


Sample command: `docker build -t sa-webapp .`

<br/>


Get the IP of sa-logic container using the `docker inspect <container-id>` command. To get the container id, run `docker ps`{{execute}}

<br/>

Or you can also run the following command to get the container id

`docker ps | awk '{
if($2 =="vaibhavrajput/docker-demo-sa-logic")
{
print $1;
}
}'`{{execute}}


<br/>



After fetching the container IP, run the following command by replacing the correct IP in value for `SA_LOGIC_API_URL` environment variable


Sample command: `docker run -d -p 8080:8080 -e SA_LOGIC_API_URL=http://<container-ip of sa-logic>:5000 vaibhavrajput/docker-demo-sa-webapp`

<br/>

Use `docker ps`{{execute}} to see the running containers
