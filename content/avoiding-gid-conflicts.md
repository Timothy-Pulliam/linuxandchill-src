Title: Avoiding GID "conflicts" when Creating Users/Groups In Linux
Date: 2018-04-23 1:38
Category: Tutorials
Tags: Users and Groups
Authors: Timothy Pulliam
Status: published

Often times when you first install your OS the first thing you want to do is add some users and groups. So let's go ahead and do that.

```
  [root@localhost ~]# useradd daisy
  [root@localhost ~]# groupadd cats
  [root@localhost ~]# useradd sophie
```

But when we go to check on our newly created users we see that the "sophie" user has a UID of 1001, but a GID of 1002. This could complicate things unnecessarily. So how do we prevent this?

```
  [root@localhost ~]# tail -2 /etc/passwd
  daisy:x:1000:1000::/home/daisy:/bin/bash
  sophie:x:1001:1002::/home/sophie:/bin/bash
```

We can see that the reason sophie was forced to take a GID of 1002, is because we had given the newly created "cats" group a GID of 1001.

```
[root@localhost ~]# tail -3 /etc/group
daisy:x:1000:
cats:x:1001:
sophie:x:1002:
```

An easy way to fix this is to designate a range of GIDs when creating groups (normally around 5000+) so they don't interfere with users in the 1000+ range. For example, what we could have done was the following.

```
  [root@localhost ~]# useradd daisy
  [root@localhost ~]# groupadd -g 5000 cats
  [root@localhost ~]# useradd sophie
  [root@localhost ~]# tail -2 /etc/passwd
  daisy:x:1000:1000::/home/daisy:/bin/bash
  sophie:x:1001:1001::/home/sophie:/bin/bash
```

Now we can see that users GIDs will never interfere with GIDs of newly created groups. Furthermore we only need to pass the groupadd -g flag the first time. After that, groupadd will know to give groups a GID that comes after the one highest in the /etc/group file.

```
[root@localhost ~]# tail -5 /etc/group
stapdev:x:158:
tcpdump:x:72:
daisy:x:1000:
cats:x:5000:
sophie:x:1001:
[root@localhost ~]# groupadd people
[root@localhost ~]# tail -5 /etc/group
tcpdump:x:72:
daisy:x:1000:
cats:x:5000:
sophie:x:1001:
people:x:5001:
```
