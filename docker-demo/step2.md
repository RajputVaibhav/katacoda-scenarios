To run the sa-logic container which executes the python logic in a container.

<br/>

# Create a Dockerfile in sa-logic


- Go to logic directory using `cd ~/container-microservice-app/sa-logic`{{execute}}
- Start with `python:3.6.6-alpine` image
- Copy contents of `sa` folder in `/app` folder of the container
- Set working directory to `/app`
- Install the required folders using `pip3 install -r requirements.txt` and `python3 -m textblob.download_corpora`
- Expose `5000` port
- Run `python3 sentiment_analysis.py` command

<br/>


---


Build image using from Dockerfile


Sample command: `docker build -t sa-logic .`

<br/>

Run the container


Sample command: `docker run -d -p 5050:5000 vaibhavrajput/docker-demo-sa-logic`{{execute}}


<br/>

Use `docker ps`{{execute}} to see the running containers
