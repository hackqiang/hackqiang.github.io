---
title: Linux Socket 学习笔记10-面向非连接的协议(UDP)
tags:
  - socket
  - UDP
id: 1701
comment: false
categories:
  - Linux
  - 未分类
  - 读书笔记
date: 2009-07-26 10:41:00
---

UDP协议相对于TCP/IP协议主要有下面几个优点：
简单：不需要建立连接。
灵活：每一次的消息都可以发送给不同的人。
高效：没有复杂的“三次握手”。
具有广播能力：一个消息可以同时发给多个接收者。
当然，它也有显著的缺点：
不可靠。
信息无序性。
消息的大小有限制。
在具体实现UDP连接之前，先看看下面两个函数：
sendto(2)用来将数据由指定的socket传给对方主机。
定义：
#include < sys/types.h >
#include < sys/socket.h >
int sendto ( int s ,const void * msg,int len, unsigned int flags,conststruct sockaddr * to , int tolen ) ;
参数说明：
参数s为已建好连线的socket,如果利用UDP协议则不需经过连线操作。参数msg指向欲连线的数据内容，参数flags 一般设0。参数to用来指定欲传送的网络地址。参数tolen为sockaddr的结果长度。
返回值
成功则返回实际传送出去的字符数，失败返回－1，错误原因存于errno 中。
recvfrom(2)用来接收远程主机经指定的socket 传来的数据。
定义:
#include<sys/types.h>
#include<sys/socket.h>
int recvfrom(int s,void *buf,int len,unsigned int flags ,struct sockaddr *from ,int *fromlen);
参数说明：
接收数据存到由参数buf 指向的内存空间，参数len 为可接收数据的最大长度。参数flags 一般设0。参数from用来指定欲传送的网络地址。参数fromlen为sockaddr的结构长度。
返回值：
成功则返回接收到的字符数，失败则返回-1，错误原因存于errno中。