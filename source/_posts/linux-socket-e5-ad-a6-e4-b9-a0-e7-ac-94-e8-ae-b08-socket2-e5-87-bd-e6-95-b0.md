---
title: Linux Socket 学习笔记8-socket(2)函数
tags:
  - C/C++
  - Linux
  - socket
  - TCP/IP
id: 1693
comment: false
categories:
  - Linux
  - 未分类
  - 读书笔记
date: 2009-07-23 09:10:00
---

之前用过函数socket,但是没做说明,今天就好好研究下这个函数.
语法定义:
#include
#Incldue
int socket(int domain,int type,int protocol);
参数说明:
domain:协议族.一般有两个值:PF_LOCAL和PF_INET.
type:套接口类型.一般用到两个:SOCK_STREAM和SOCK_DGRAM.
protocol:使用的协议.我们一般设置它为0.
简单的说SOCK_STREAM是用的TCP协议，
SOCK_DGRAM是使用UDP协议。