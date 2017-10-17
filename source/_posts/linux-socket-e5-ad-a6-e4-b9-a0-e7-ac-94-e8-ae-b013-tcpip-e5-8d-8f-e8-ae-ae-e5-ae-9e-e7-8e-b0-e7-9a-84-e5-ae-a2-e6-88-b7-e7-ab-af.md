---
title: Linux Socket 学习笔记13-TCP/IP协议实现的客户端
tags:
  - socket
  - TCP/IP
id: 1707
comment: false
categories:
  - Linux
  - 未分类
  - 读书笔记
date: 2009-07-29 20:32:00
---

要基于TCP/IP协议进行通信，客户端需要进行以下几个步骤：
建立套接口。
连接到服务器。
进行通讯。
关闭连接。
其中进行通讯使用read(2)和write(2)函数。
下面这段客户端的代码与服务器进行通讯，取得服务器时间。用到的服务为daytime,端口号为13，使用的协议为TCP/IP协议。
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
/* daytime.c:
* Example daytime client :
*/
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
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
struct
sockaddr_in adr_srvr
;
/* AF_INET */
int
len_inet
;
/* length  */
int
s
;
/* Socket */
char
dtbuf
[
128
]
;
/* Date/Time info */
/*
* Create a server socket address:
*/
memset
(
&
amp
;
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
13
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
len_inet
=
sizeof
adr_srvr
;
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
* Connect to the server:
*/
z
=
connect
(
s
,&
amp
;
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
"connect(2)"
)
;
/*
* Read the date/time info:
*/
z
=
read
(
s
,&
amp
;
dtbuf
,
sizeof
dtbuf
-
1
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
"read(2)"
)
;
/*
* Report the Date &amp; Time :
*/
dtbuf
[
z
]
=
0
;
/* null terminate string */
printf
(
"Date &amp; Time is: %s
\n
"
,
dtbuf
)
;
/*
* Close the socket and exit:
*/
close
(
s
)
;
return
0
;
}