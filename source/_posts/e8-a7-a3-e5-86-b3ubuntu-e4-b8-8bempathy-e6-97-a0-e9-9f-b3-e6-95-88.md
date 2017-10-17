---
title: 解决Ubuntu下Empathy无音效
tags:
  - empathy
  - Ubuntu
id: 1754
comment: false
categories:
  - Linux
  - 未分类
date: 2010-04-06 19:55:00
---

用的 EEEUBUNTU，装了empathy后发现没声音，找了个解决方法。
Empathy
用 的音效是ubuntu”預設”音效 (/usr/share/sounds/ubuntu/stereo)
只要那个目录有以下几个文件就可以：
“message-new-instant”
“message-sent-instant”
“service-login”
“service-logout”
“phone-incoming-call”
“phone-outgoing-calling”
“phone-hangup”
格式为”ogg”
参考网站：
http://hi.baidu.com/%CF%EB%B2%BB%B3%F6%87%E5%B5%C4id%C1%CB/blog/item/67bede27ccbe2908908f9d4d.html