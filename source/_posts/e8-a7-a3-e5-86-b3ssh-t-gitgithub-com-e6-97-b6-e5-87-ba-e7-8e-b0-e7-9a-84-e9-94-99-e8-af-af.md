---
title: 解决”ssh -T git@github.com”时出现的错误
tags:
  - github
id: 1819
comment: false
categories:
  - Linux
date: 2011-10-24 10:51:00
---

在执行ssh -T git@github.com后，出现：
Agent admitted failure to sign using the key.
Permission denied (publickey).
只需要
$ ssh-keygen -t rsa -C “your_email@youremail.com”
原文：
http://unixway.info/linux/agent-admitted-failure-to-sign-using-the-key-permission-denied-publickey/