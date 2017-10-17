---
title: Linux Socket 学习笔记15-主机名和网络名的查询
tags:
  - socket
id: 1709
comment: false
categories:
  - Linux
  - 未分类
  - 读书笔记
date: 2009-07-31 12:03:00
---

相对于IP来说，人们更倾向于使用名字。
下面就学习几个常用的关于主机名和IP地址等相关的函数：
gethostname(2)：获取当前主机名。
定义：
＃include<sys/utsname.h>
int gethostname(char *name,size_t len);
参数说明：
name用于接受主机名信息，len为name的最大长度。
成功返回0；否则返回－1，错误信息保存在errno中。
getdomainname(2):获取主机上的NIS域名。
用法与函数gethostname几乎一样。
gethostbyname(2)
这个函数的输入参数是想要查询的主机名，返回值是一个指向结构hostent的指针。
定义：
#include<netdb.h>
extern int h_errno;
struct hostent *gethostbyname(const  char *name);
struct hostent{
char h_name;//主机官方名
char **h_aliases;//别名清单
int h_addrtype;//地址类型
int h_length;//地址长度
char **h_addr_list;//地址清单
};
#define h_addr h_addr_list[0]
gethostbyaddr(3):用IP地址查找主机信息。
定义：
#include <sys/socket.h>
struct hostent *gethostbyaddr(
const char *addr,
int len,
int type);