# Scanning the images

To scan the image, we will provide the following inputs

* CLAIR_ADDR - server where Clair is hosted i.e. localhost at port 6060
* CLAIR_OUTPUT - severity level threshold, vulnerabilities with severity level higher than or equal to this threshold will be showed
* CLAIR_THRESHOLD - how many outputted vulnerabilities Klar can tolerate before returning 1, default is 0

<br/>

So, our final statement would look like 

`CLAIR_ADDR=http://localhost:6060 CLAIR_OUTPUT=Low CLAIR_THRESHOLD=10 klar <image>`

<br/>

Try running it on `vaibhavrajput/compose-demo-api` image using the following command

`CLAIR_ADDR=http://localhost:6060 CLAIR_OUTPUT=Low CLAIR_THRESHOLD=10 klar vaibhavrajput/compose-demo-api`{{execute}}

