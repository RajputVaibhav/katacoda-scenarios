Here, we need to set the hostname where the registry will be hosted inside the `harbor.cfg` file

<br/>

You can display the file using `cat harbor.cfg`{{execute}} or specifically the hostname section using `cat harbor.cfg | grep hostname`{{execute}}

<br/>

We need to change the current value of `reg.mydomain.com` to the Host IP i.e. `[[HOST_IP]]`

To do this, either edit the file using your desired editor or just run the following command

`sed -i s/reg\.mydomain\.com/[[HOST_IP]]/g harbor.cfg`{{execute}}

