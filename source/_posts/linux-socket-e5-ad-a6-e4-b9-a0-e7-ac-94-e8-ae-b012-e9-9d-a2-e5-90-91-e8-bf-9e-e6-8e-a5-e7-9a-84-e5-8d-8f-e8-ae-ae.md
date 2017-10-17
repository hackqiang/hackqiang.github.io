---
title: Linux Socket 学习笔记12-面向连接的协议
tags:
  - TCP/IP
id: 1706
comment: false
categories:
  - Linux
date: 2009-07-28 13:25:00
---

之前学了面向非连接的协议UDP协议，现在开始学习另一个重要的面向连接的协议－－TCP/IP协议。相对于UDP协议，TCP/IP协议将能很好的处理以下几个问题：
分组的丢失
超时和重发
接收顺序的混乱
流控
在学习TCP/IP协议之前我们先要了解几个属于Internet服务的TCP/IP附属设施。
/etc/services文件
这个文件将某个特定的Internet服务名映射到协议的端口号。
/etc/protocols文件
这个文件包含了已定义的Internet协议值。