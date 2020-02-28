`docker inspect <container-id>`


`docker ps`{{execute}}


`docker run -d -p 8080:8080 -e SA_LOGIC_API_URL=http://<container-ip of sa-logic>:5000 vaibhavrajput/docker-demo-sa-webapp`


`docker run -d -p 8080:8080 -e SA_LOGIC_API_URL=http://$(docker ps | awk '{
if($2 =="vaibhavrajput/docker-demo-sa-logic")
{
print $1;
}
}'):5000 vaibhavrajput/docker-demo-sa-webapp`{{execute}}
