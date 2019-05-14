Title: Custom Firewalld Services
Date: 2018-05-08 19:05
Category: Tutorials
Tags: Networking, Firewall
Authors: Timothy Pulliam
Status: published

## Overview

You can define custom services using firewall-cmd. Services are groups of firewall rules. For example, on a freeipa server, you would need to open the following ports.

TCP Ports:

* 80, 443: HTTP/HTTPS
* 389, 636: LDAP/LDAPS
* 88, 464: Kerberos
* 53: DNS

UDP Ports:

* 88, 464: Kerberos
* 53: DNS
* 123: NTP


You can group these all into a single service (named freeipa) and then simply start the one service, rather than start each individual rule. This allows you to logically group firewall rules so they are started and stopped together if necessary. It also avoids the inevitable confusion when you list out the ports on your firewall and see that port 88/UDP is open you may wonder why.

## Creating New services

The following command creates a new file named `/etc/firewalld/services/freeipa.xml` as well as a new firewalld service named `freeipa`.

    $ firewall-cmd --permanent --new-service=freeipa

You can add a more descriptive name as well as a short name for the service, plus the ports you wish to be associated with this service.

```
$ firewall-cmd --permanent --service=freeipa --set-description="Firewall rules for a FreeIPA Server"
$ firewall-cmd --permanent --service=freeipa --set-short=freeipa
$ firewall-cmd --permanent --service=freeipa --add-port={80/tcp,443/tcp,389/tcp,636/tcp,88/tcp,464/tcp,53/tcp,88/udp,464/udp,53/udp,123/udp}
```


Now if you examine `/etc/firewalld/services/freeipa.xml` you will see it has been configured

```
$ cat /etc/firewalld/services/freeipa.xml
<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>freeipa</short>
  <description>Firewall rules for a FreeIPA Server</description>
  <port protocol="tcp" port="80"/>
  <port protocol="tcp" port="443"/>
  <port protocol="tcp" port="389"/>
  <port protocol="tcp" port="636"/>
  <port protocol="tcp" port="88"/>
  <port protocol="tcp" port="464"/>
  <port protocol="tcp" port="53"/>
  <port protocol="udp" port="88"/>
  <port protocol="udp" port="464"/>
  <port protocol="udp" port="53"/>
  <port protocol="udp" port="123"/>
</service>
```

Now, you can add this service just like any other service

```
# firewall-cmd --permanent --add-service freeipa
# firewall-cmd --reload
# firewall-cmd --list-services
ssh dhcpv6-client dns http freeipa
```

If you wish to permanently delete the service. You need to reload firewalld in order for effects to be recognized.

```
# firewall-cmd --remove-service=freeipa
# firewall-cmd --permanent --delete-service=freeipa
success
# firewall-cmd --reload
```

The *.xml config files are now deleted

```
# pwd
/etc/firewalld/services
# ls
freeipa.xml.old  test.xml.old
```

#### Resources
[http://www.firewalld.org/documentation/howto/add-a-service.html](http://www.firewalld.org/documentation/howto/add-a-service.html)
