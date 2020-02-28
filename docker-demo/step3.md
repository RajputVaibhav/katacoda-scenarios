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


`docker run -d -p 8080:8080 -e SA_LOGIC_API_URL=http://<container-ip of sa-logic>:5000 vaibhavrajput/docker-demo-sa-webapp`

<br/>

Use `docker ps`{{execute}} to see the running containers