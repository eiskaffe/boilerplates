# Pihole
Simple pihole setup guide for docker instances<br>
<sub>More info at https://github.com/pi-hole/docker-pi-hole/ and https://docs.pi-hole.net/</sub>
## Installation
Standard portainer [docker-compose.yml](https://github.com/eiskaffe/scripts/blob/main/docker/pihole/docker-compose.yml) method:
```yaml
version: "3"

services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    # For DHCP it is recommended to remove these ports and instead add: network_mode: "host"
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "40080:80"
      - "40443:443"
    environment:
      TZ: 'Europe/Budapest'
      # WEBPASSWORD: 'set a secure password here or it will be random'
    # Volumes store your data between container upgrades
    volumes:
      - '/opt/pihole-storage/etc-pihole:/etc/pihole'
      - '/opt/pihole-storage/etc-dnsmasq.d:/etc/dnsmasq.d'
    #   https://github.com/pi-hole/docker-pi-hole#note-on-capabilities
    restart: unless-stopped
```
To get the random generated password use the following command in the terminal
```terminal
docker logs pihole | grep password
```

## Issues and possible solutions

### Port already binded
You can check what is listening already on that port using the following command
```terminal
sudo lsof -i -P -n | grep LISTEN
```
Once you found the root of your troubles, look it up how to disable it. For e.g. a common issue is [resolved](https://discourse.pi-hole.net/t/update-what-to-do-if-port-53-is-already-in-use/52033).
To fix the issue open the `/etc/systemd/resolved.conf` and set the DNSStubListener to no (`DNSStubListener=no`).
After that reboot or restart resolved
```terminal
service systemd-resolved restart
```
Now the problem should be solved
