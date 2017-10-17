---
title: Linux Socket 学习笔记7–一些地址转换函数
tags:
  - TCP/IP
id: 1691
comment: false
categories:
  - C/C++
date: 2009-07-22 16:51:00
---

主要的地址转换函数有:
inet_addr(3)
inet_aton(3)
inet_ntoa(3)
inet_network(3)
inet_lnaof(3)
inet_netof(3)
inet_makeaddr(3)
inet_addr(3)
它的作用是把字符串转换为点分十进制IP地址,这个函数现在已经很少使用,但是之前文件中用的很多.现在可以用inet_aton(3)取代它.
定义:
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
unsigned long inet_addr(const char *string);
如果成功就返回一个32位二进制(网络字节序),失败返回INADDR_NONE.
inet_aton(3)
这个函数是函数inet_addr的改进.
定义:
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
int inet_aton(const char *string,struct in_addr *addr);
输出参数addr是被更新的结构,如果成功返回非0值,否则返回0.
inet_ntoa(3)
它的作用和函数inet_aton正好相反.
定义:
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
char *inet_ntoa(struct in_addr addr);
注意点:inet_ntoa的返回值在下一次调用之前有效.
inet_network(3)
这个函数的作用是把点十进制的IP地址转换成主机序的32位二进制IP地址.
定义:
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
unsigned long inet_network(const char *addr);
如果参数不正确,返回值为0xFFFFFFFF.
inet_lnaof(3)
这个函数的作用是把套接口地址中的IP地址(网络字节序)转换为没有网络位的主机ID(主机字节序).
定义:
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
unsigned long inet_lnaof(struct in_addr addr);
inet_netof(3)
这个函数的作用是把套接口地址中的IP地址(网络字节序)转换为没有网络位的网络ID(主机字节序).
定义:
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
unsigned long inet_netof(struct in_addr addr);
注意这个函数的返回值是右端对齐,主机位被移出.
inet_makeaddr(3)
它的作用是将网络位和主机位合并组成一个新的IP地址.
定义:
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
struct in_addr inet_makeaddr(int net,int host);