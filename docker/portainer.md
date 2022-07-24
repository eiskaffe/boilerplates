# Portainer
Simple setup guide for portainer

## Portainer without SSL
Switch to root user
```terminal
sudo su -
```
Make a new volume to store portainer's data
```terminal
docker volume create portainer_data
```
Run the following command to start portainer
```terminal
docker run -d -p 8000:8000 -p 9443:9443 \
    --name portainer --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer-data:/data \
    portainer/portainer-ce:latest
```
Check if it is running
```terminal
docker ps
```
Access the web interface by navigating to
`http://localipaddress:9443`
<br>*More detailed information can be found the [portainer website](https://docs.portainer.io/start/install/server/docker/linux).*
## Portainer with self-signed SSL
Switch to root user
```terminal
sudo su -
```
Make a new volume to store portainer's data
```terminal
docker volume create portainer_data
```
Generate a self-signed SSL certificate<br>
<sub>Note that this is useful when you can not use a local DNS</sub>
```terminal
openssl req -new -newkey rsa:4096 -days 3650 -nodes -x509 -keyout /etc/local-certs/portainer.key -out /etc/local-certs/portainer.crt
```
Run the following command to start portainer with a self-signed certificate
```terminal
docker run -d -p 8000:8000 -p 9443:9443 \
    --name portainer --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /etc/local-certs:/certs \
    -v portainer-data:/data \
    portainer/portainer-ce:latest --ssl --sslcert /etc/local-certs/portainer.crt --sslkey /etc/local-certs/portainer.key
```
Check if it is running
```terminal
docker ps
```
Access the web interface by navigating to
`https://localipaddress:9443`
<br>*More detailed information can be found the [portainer website](https://docs.portainer.io/v/ce-2.6/advanced/ssl).*

## Updating portainer
While you are root use the following commands to upgrade portainer
```terminal
docker stop portainer
```
```terminal
docker rm portainer
```
```terminal
docker pull portainer/portainer-ce:latest
```
After the download is done deploy portainer with the same command that you used
<br>*More detailed information can be found the [portainer website](https://docs.portainer.io/start/upgrade/docker).*
