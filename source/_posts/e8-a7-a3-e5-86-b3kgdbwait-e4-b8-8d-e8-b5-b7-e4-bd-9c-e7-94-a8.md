---
title: 解决kgdbwait不起作用
tags:
  - kgdb
id: 1798
comment: false
categories:
  - kernel/drivers
  - Linux
  - 未分类
date: 2010-05-15 09:18:00
---

给内核选上kgdb相关配置后，在grub的引导参数后加：
kgdbwait kgdboc=ttyS0,115200
重启后，系统竟然还正常启动了，经过分析，发现有造成这种现象可能有两个原因：
1.串口驱动没配置好；
2.kgdboc后的配置有问题。
我把串口驱动配置后，就可以了。
但是问题是我用的笔记本，压根就没有串口，用usb转串口貌似也不管用，有人能帮忙吗？