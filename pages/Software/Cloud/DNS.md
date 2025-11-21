---

title: "DNS"  
linkTitle: "DNS"  
date: 2022-01-30  
weight: 70  
description: News and information about domain name servers
type: [[Cloud]]
---

* [naked domain redirect](http://wwwizer.com/naked-domain-redirect)
* To see the DNS servers, run: `resolvectl`
* Disable DNS service
```
sudo systemctl enable systemd-resolved
sudo systemctl start systemd-resolved
```
* [DNSmasq](https://computingforgeeks.com/install-and-configure-dnsmasq-on-ubuntu/)
* [BIND on Ubuntu](https://ubuntu.com/server/docs/service-domain-name-service-dns)
* [Query nameservers](https://docs.rackspace.com/support/how-to/using-dig-to-query-nameservers/)