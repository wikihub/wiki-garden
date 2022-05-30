---
title: "Networking"
linkTitle: "Networking"
weight: 20
---

* [Docker networks](https://geek-cookbook.funkypenguin.co.nz/reference/networks/)

# Ubuntu

* To see ports in use:

```
sudo lsof -i -P -n | grep LISTEN 
sudo netstat -tulpn | grep LISTEN
```

* [List of running services](https://linuxconfig.org/how-to-use-systemctl-to-list-services-on-systemd-linux):

```
systemctl list-units --type=service --state=running 
```
* To list all the IPv4 rules:

```
sudo iptables -S
```
