---
title: Linux Socket 学习笔记14-TCP/IP协议实现的服务器端
tags:
  - socket
  - TCP/IP
id: 1708
comment: false
categories:
  - Linux
date: 2009-07-30 12:17:00
---

服务器端的基本工作步骤为：
建立套接口。
绑定地址接口。
监听。
接受连接请求。
与客户端通讯。
关闭。
监听所用的函数为listen(2):
定义：
#include <sys/socket.h>
int listen(int s, int backlog);
s为监听的套接口，backlog为连接队列的长度。
如果调用成功返回0；负责返回－1，错误信息在变量errno中。
接受连接请求使用函数accept(2):
定义：
#include <sys/socket.h>
#include <sys/types.h>
int accept(int s, struct sockaddr *addr,int *len);
s必须为之前的监听套接口，addr为接受客户套接口的地址，len指向接受套接口地址缓存最大长度的指针。
如果调用成功返回一个新的套接口描述符；负责返回－1，错误信息在变量errno中。
下面一段是提供daytime服务的服务器代码：
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
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
/* server.c:
* Example daytime server :
*/
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <time.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
static
void
bail
(
const
char
*
on_what
)
{
if
(
errno
!=
0
)
{
fputs
(
strerror
(
errno
)
,
stderr
)
;
fputs
(
": "
,
stderr
)
;
}
fputs
(
on_what
,
stderr
)
;
fputc
(
'
\n
'
,
stderr
)
;
exit
(
1
)
;
}
int
main
(
int
argc
,
char
**
argv
)
{
int
z
;
char
*
srvr_addr
=
NULL
;
char
*
srvr_port
=
"13"
;
struct
sockaddr_in adr_srvr
;
/* AF_INET */
struct
sockaddr_in adr_clnt
;
/* AF_INET */
int
len_inet
;
/* length  */
int
s
;
/* Socket */
int
c
;
/* Client socket */
int
n
;
/* bytes */
time_t td
;
/* Current date&time */
char
dtbuf
[
128
]
;
/* Date/Time info */
/*
* Create a TDP/IP socket to use :
*/
s
=
socket
(
PF_INET
,
SOCK_STREAM
,
0
)
;
if
(
s
==
-
1
)
bail
(
"socket()"
)
;
/*
* Create a server socket address:
*/
memset
(
&
adr_srvr
,
0
,
sizeof
adr_srvr
)
;
adr_srvr.
sin_family
=
AF_INET
;
adr_srvr.
sin_port
=
htons
(
atoi
(
srvr_port
)
)
;
adr_srvr.
sin_addr
.
s_addr
=
inet_addr
(
"127.0.0.1"
)
;
/*
* Bind the server address:
*/
len_inet
=
sizeof
adr_srvr
;
z
=
bind
(
s
,
(
struct
sockaddr
*
)
&
adr_srvr
,
len_inet
)
;
if
(
z
==
-
1
)
bail
(
"bind(2)"
)
;
/*
* Make it a listening socket:
*/
z
=
listen
(
s
,
10
)
;
if
(
z
==
-
1
)
bail
(
"listen(2)"
)
;
/*
* Start the server loop :
*/
for
(
;;
)
{
/*
* Wait for a connect :
*/
len_inet
=
sizeof
adr_clnt
;
c
=
accept
(
s
,
(
struct
sockaddr
*
)
&
adr_clnt
,
&
len_inet
)
;
if
(
c
==
-
1
)
bail
(
"accept(2)"
)
;
/*
* Generate a time stamp :
*/
time
(
&
td
)
;
n
=
(
int
)
strftime
(
dtbuf
,
sizeof
dtbuf
,
"%A %b %d %H:%M:%S %Y
\n
"
,
localtime
(
&
td
)
)
;
/*
* Write result back to the client :
*/
z
=
write
(
c
,
dtbuf
,
n
)
;
if
(
z
==
-
1
)
bail
(
"write(2)"
)
;
close
(
c
)
;
}
return
0
;
}