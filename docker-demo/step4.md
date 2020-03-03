Finally, run the following command to execute the frontend container

<br/>

# Create a Dockerfile in sa-frontend

- Go to frontend directory using `cd ~/container-microservice-app/sa-frontend`{{execute}} 
- Change the URL in `fetch` method of `analyzeSentence` in `container-microservice-app/sa-frontend/src/App.js` to https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/sentiment
- Build app using `npm run build`{{execute}}  
- Start with `nginx` image 
- Copy contents of `build` folder in `/usr/share/nginx/html` of container

<br/>


---


Build image using from Dockerfile


Sample command: `docker build -t sa-frontend .`

<br/>

Run the container


Sample command: `docker run -d -p 80:80 vaibhavrajput/docker-demo-sa-frontend`{{execute}}

<br/>


Use `docker ps`{{execute}} to see the running containers


<br/><br/>


You can access your app at


https://[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com
