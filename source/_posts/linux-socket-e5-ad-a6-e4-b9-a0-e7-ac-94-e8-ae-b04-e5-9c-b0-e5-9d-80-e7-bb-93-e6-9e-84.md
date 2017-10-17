---
title: Linux Socket 学习笔记4–地址结构
tags:
  - C/C++
  - Linux
  - socket
  - 地址结构
id: 1685
comment: false
categories:
  - Linux
date: 2009-07-17 14:26:00
---

每一种通信协议都对网络地址格式做了明确的规定，地址族的作用就是指明使用哪一种地址类型。
BSD定义了一个通用的地址结构：
?
View Code
C
1
2
3
4
5
6
7
struct
sockaddr
{
sa_family_t   sa_family
;
char
sa_data
[
14
]
;
}
;
其中sa_family_t是一个无符号的整形。虽然这个通用结构对编程者来说没什么用处，但是它为其他的地址结构提供了一个 重要的参考。
在linux中，使用最普遍的地址族是AF_INET,TCP/IP协议就使用具有IPv4地址的套接口，下面是C语言描述的结构sockaddr_in：
?
View Code
C
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
＃include
&
lt
;
netinet
/
in.
h
&
gt
;
struct
sockaddr_in
{
sa_family_t      sin_family
;
//地址族
unit16_t           sin_port
;
//端口号
struct
in_addr   sin_addr
;
//Internet地址
unsigned
sin_zero
[
8
]
;
//占位字节
}
;
struct
in_addr
{
unit32_t        s_addr
;
}
;
在TCP/IP协议中，sin_family将被初始化为AF_INET，sin_zero[8]的 作用仅仅是对齐，实际使用时不用初始化。