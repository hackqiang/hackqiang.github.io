---
title: Linux Socket 学习笔记8-bind(2)函数
tags:
  - bind
  - Linux
  - socket
id: 1697
comment: false
categories:
  - Linux
date: 2009-07-25 10:37:00
---

之前学了创建套接口的函数socket().创建好套接口后第二步就是地址绑定,用函数bind(2)实现.
函数定义：
?
View Code
C
1
2
3
#include<sys/types.h>
#include<sys/socket.h>
int
bind
(
int
sockfd
,
struct
sockaddr
*
addr
,
int
addrlen
)
;
参数说明：
之前学了创建套接口的函数socket().创建好套接口后第二步就是地址绑定,用函数bind(2)实现.
函数定义：
?
View Code
C
1
2
3
#include<sys/types.h>
#include<sys/socket.h>
int
bind
(
int
sockfd
,
struct
sockaddr
*
addr
,
int
addrlen
)
;
参数说明：
sockfd:套接口描述符。
addr:套接口地址。
addrlen:地址结构的长度。
返回值：
如果调用成功返回0，否则返回－1，出错信息在errno中查看。
注意这里的套接口地址是通用结构，我们在使用时一般要进行强制转换。
下面是一段关于bind2的示例代码：
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
.....
int
sockfd
;
struct
sockaddr_in addr
;
int
len_addr
=
sizeof
(
addr
)
;
addr.
sin_family
=
AF_INET
;
addr.
sin_port
=
hton
(
8888
)
;
inet_aton
(
"127.0.0.44"
,&
amp
;
addr.
sin_addr
)
;
sockfd
=
socket
(
AF_INET
,
SOCK_STREAM
,
0
)
;
bind
(
sockfd
,
(
struct
sockaddr
*
)
&
amp
;
addr
,
len_addr
)
;
....
sockfd:套接口描述符。
addr:套接口地址。
addrlen:地址结构的长度。
返回值：
如果调用成功返回0，否则返回－1，出错信息在errno中查看。
注意这里的套接口地址是通用结构，我们在使用时一般要进行强制转换。
下面是一段关于bind2的示例代码：
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
.....
int
sockfd
;
struct
sockaddr_in addr
;
int
len_addr
=
sizeof
(
addr
)
;
addr.
sin_family
=
AF_INET
;
addr.
sin_port
=
hton
(
8888
)
;
inet_aton
(
"127.0.0.44"
,&
amp
;
addr.
sin_addr
)
;
sockfd
=
socket
(
AF_INET
,
SOCK_STREAM
,
0
)
;
bind
(
sockfd
,
(
struct
sockaddr
*
)
&
amp
;
addr
,
len_addr
)
;
....