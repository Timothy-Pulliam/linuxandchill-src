Title: A Docker Primer
Date: 2019-1-05 16:37
Modified: 2019-12-06 15:30
Category: Tutorials
Tags: Docker, Devops
Slug: a-docker-primer
Authors: Timothy Pulliam
Summary: A short introduction to Docker
Status: published

## Terminology

##### Image vs. Container

A Docker image can be thought of as the blueprint for an OS that will be used to construct a container. An image is essentially how the the container will be configured, while a container is the actual running OS itself.

A single image can generate many containers.

## Installation

The following is only for installing the docker community edition. For other
options installing Docker, see the [Docker Docs](https://docs.docker.com/install/).

Ubuntu

```
apt-get update
apt-get install docker-ce
```

Redhat

```
yum install docker-ce
```

Start the docker daemon

```
systemctl start docker

systemctl enable docker
```

## Pulling Images From Docker Hub

Community Images are uploaded to the [Docker Hub](https://hub.docker.com/) where
anyone can pull them. The concept is very similar to source code and Github.

You can search for a particular image, say kali linux.

```
tpulliam@lappy:~$ docker search kali
NAME                           DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
kalilinux/kali-linux-docker    Kali Linux Rolling Distribution Base Image      555                                     [OK]
linuxkonsult/kali-metasploit   Kali base image with metasploit                 68

...
```


Pull the one with the most stars, or the official one. Whichever.

```
tpulliam@lappy:~$ docker pull kalilinux/kali-linux-docker

Using default tag: latest
latest: Pulling from kalilinux/kali-linux-docker
014a6d74f96c: Pull complete
9febb14563a0: Pull complete
c38f04972c6b: Pull complete
9d39d049d5d0: Pull complete
4e80058918bf: Pull complete
ccd85f0810ad: Pull complete
6ab25bddb799: Pull complete
789ba1ebcb41: Pull complete
524584107b55: Pull complete
40a1af1b9680: Pull complete
fb6edc730b9f: Pull complete
270f87c17cf3: Pull complete
8159e4fffac9: Pull complete
01d3dc4e9fe9: Pull complete
a386beee6e20: Pull complete
46fa80bd0f33: Pull complete
2d3ff71a091d: Pull complete
6f41a333af7c: Pull complete
Digest: sha256:7f1253cba663662d78c121369e23d6c0b58b7b95de268886ecfdb73b003a3bd8
Status: Downloaded newer image for kalilinux/kali-linux-docker:latest
```

We can see the kali linux image has been added to the list of images.

```

tpulliam@lappy:~$ docker images
REPOSITORY                    TAG                 IMAGE ID            CREATED             SIZE
kalilinux/kali-linux-docker   latest              f26f3ae90aee        2 months ago        1.57GB
```

## Running An Instance/Container

There are two ways to run a container. You can run a container interactively,
where you have access to the shell

```
tpulliam@lappy:~$ docker run -t -i kalilinux/kali-linux-docker /bin/bash
root@f157bf90bca9:/#
```

Or you can instruct the container to run a single command and then terminate

```
tpulliam@lappy:~$ docker run kalilinux/kali-linux-docker echo "hello docker"
hello docker
```

To view all running and stopped containers use the `docker ps -a` command. If
you only want to see running containers (and not stopped/terminated ones) ommit
the `-a` flag.

```
tpulliam@lappy:~$ docker ps -a
CONTAINER ID        IMAGE                         COMMAND             CREATED              STATUS              PORTS               NAMES
f157bf90bca9        kalilinux/kali-linux-docker   "/bin/bash"         About a minute ago   Up About a minute                       objective_golick
37be294f38ab        kalilinux/kali-linux-docker   "echo 'hello docker'"   39 seconds ago      Exited (0) 37 seconds ago                       elegant_mccarthy

```

If we need to reattach to the container, we can do so by specifying the container
name or id.

```
tpulliam@lappy:~$ docker attach objective_golick
root@f157bf90bca9:/#
```

To stop and remove a running instance run the below commands (you can interchange container name and id). You can verify the containers have been removed by running
`docker ps -a`.

```
tpulliam@lappy:~$ docker stop objective_golick
objective_golick
tpulliam@lappy:~$ docker rm f157bf90bca9
f157bf90bca9
```
