Title: Automating RHEL 7 / CentOS 7 Updates With yum-cron
Date: 2018-04-21 1:39
Category: Tutorials
Tags: Automation
Authors: Timothy Pulliam
Status: published

## Overview

I’m sure by now every one knows about yum-cron. It automatically updates your systems packages, which can be handy if you have to manage lots of systems and you want to make sure the latest security patches have been installed. It’s also pretty straight forward to use. Just be careful not to automatically update systems such as your production web server without testing, as some updates can actually break things. You’ve been warned.

###Installation

Install the package the usual way

    # yum install yum-cron

Make sure the service is running

    # systemctl start yum-cron
    # systemctl enable yum-cron

###Configuration
There are two configuration files for yum cron. There are also two crontab entries for yum-cron

    # rpm -qc yum-cron
    /etc/yum/yum-cron-hourly.conf
    /etc/yum/yum-cron.conf

    # rpm -ql yum-cron
    /etc/cron.daily/0yum-daily.cron
    /etc/cron.hourly/0yum-hourly.cron
    …
    …

The */etc/cron.daily/0yum-daily.cron* job reads from the */etc/yum/yum-cron.conf* configuration file while the */etc/cron.hourly/0yum-hourly.cron* file reads from the */etc/yum/yum-cron-hourly.conf* configuration file. The two configuration files are meant to optimize yum-cron depending on whether it runs hourly or daily. If you want to disable hourly checks, you can edit the */etc/cron.hourly/0yum-hourly.cron* and comment out the exec line like so

    # Action!
    # exec /usr/sbin/yum-cron /etc/yum/yum-cron-hourly.conf

Configuration of /etc/yum/yum-cron.conf is straight forward. The only things you might need to set are

```
[commands]
apply_updates = yes
```

Otherwise, updates will not actually be applied ;b

You may also want to disable upgrading the kernel itself as this can effect your system in unexpected ways.

```
[base]
exclude = kernel*
```

yum-cron can also alert you when your system is updated. This can be set via the following options

```
[emitters]
system_name = your_hostname
emit_via = email

[email]
email_to = your_email@domain.com
```

You will also need to have an MTA like postfix running to be able to send emails.

```
# yum install postfix
# systemctl start postfix
# systemctl enable postfix
```
