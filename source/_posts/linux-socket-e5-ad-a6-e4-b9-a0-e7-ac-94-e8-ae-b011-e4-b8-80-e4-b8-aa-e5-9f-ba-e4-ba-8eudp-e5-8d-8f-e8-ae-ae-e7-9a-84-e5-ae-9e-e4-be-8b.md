---
title: Linux Socket 学习笔记11-一个基于UDP协议的实例
tags:
  - Linux
  - socket
  - UDP
id: 1703
comment: false
categories:
  - Linux
date: 2009-07-27 11:40:00
---

要使用UDP协议进行通讯，需要以下几个步骤：
服务器端（接收着端）：
创建套接字。
将创建的套接字绑定到本地的地址和端口上。
等待接收数据。
关闭套接字。
客户端（发送端）：
创建套接字。
向服务器端发送数据。
关闭套接字。
服务器端代码：
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
104
105
/*
* server :
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
struct
sockaddr_in adr_inet
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
char
dgram
[
512
]
;
/* Recv buffer */
char
dtfmt
[
512
]
;
/* Date/Time Result */
srvr_addr
=
"127.0.0.23"
;
/*
* Create a UDP socket to use :
*/
s
=
socket
(
AF_INET
,
SOCK_DGRAM
,
0
)
;
/*
* Create a socket address, for use
* with bind(2) :
*/
memset
(
&
adr_inet
,
0
,
sizeof
adr_inet
)
;
adr_inet.
sin_family
=
AF_INET
;
adr_inet.
sin_port
=
htons
(
9090
)
;
adr_inet.
sin_addr
.
s_addr
=
inet_addr
(
srvr_addr
)
;
len_inet
=
sizeof
adr_inet
;
/*
* Bind a address to our socket, so that
* client programs can contact this
* server:
*/
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
adr_inet
,
len_inet
)
;
/*
* Now wait for requests:
*/
for
(
;;
)
{
/*
* Block until the program receives a
* datagram at our address and port:
*/
len_inet
=
sizeof
adr_clnt
;
z
=
recvfrom
(
s
,
/* Socket */
dgram
,
/* Receiving buffer */
sizeof
dgram
,
/* Max recv buf size */
0
,
/* Flags: no options */
(
struct
sockaddr
*
)
&
adr_clnt
,
/* Addr */
&
len_inet
)
;
/* Addr len, in & out */
/*
* Process the request :
*/
dgram
[
z
]
=
0
;
/* null terminate */
printf
(
"%s:%s
\n
"
,
inet_ntoa
(
adr_clnt.
sin_addr
)
,
dgram
)
;
fputs
(
"Enter:"
,
stdout
)
;
if
(
!
fgets
(
dtfmt
,
sizeof
dtfmt
,
stdin
)
)
break
;
z
=
sendto
(
s
,
/* Socket to send result */
dtfmt
,
/* The datagram result to snd */
strlen
(
dtfmt
)
,
/* The datagram lngth */
0
,
/* Flags: no options */
(
struct
sockaddr
*
)
&
adr_clnt
,
/* addr */
len_inet
)
;
/* Client address length */
}
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
客户端代码：
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
/*
* client :
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
int
x
;
char
*
srvr_addr
=
NULL
;
struct
sockaddr_in adr_srvr
;
/* AF_INET */
struct
sockaddr_in adr
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
char
dgram
[
512
]
;
/* Recv buffer */
srvr_addr
=
"127.0.0.23"
;
/*
* Create a socket address, to use
* to contact the server with:
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
9090
)
;
adr_srvr.
sin_addr
.
s_addr
=
inet_addr
(
srvr_addr
)
;
len_inet
=
sizeof
adr_srvr
;
/*
* Create a UDP socket to use :
*/
s
=
socket
(
AF_INET
,
SOCK_DGRAM
,
0
)
;
for
(
;;
)
{
/*
* Prompt user for a date format string:
*/
fputs
(
"Enter:"
,
stdout
)
;
if
(
!
fgets
(
dgram
,
sizeof
dgram
,
stdin
)
)
break
;
/* EOF */
z
=
strlen
(
dgram
)
;
if
(
z
>
0
&&
dgram
[
--
z
]
==
'
\n
'
)
dgram
[
z
]
=
0
;
/* Stomp out newline */
/*
* Send format string to server:
*/
z
=
sendto
(
s
,
/* Socket to send result */
dgram
,
/* The datagram result to snd */
strlen
(
dgram
)
,
/* The datagram lngth */
0
,
/* Flags: no options */
(
struct
sockaddr
*
)
&
adr_srvr
,
/* addr */
len_inet
)
;
/* Server address length */
/*
* Wait for a response :
*/
x
=
sizeof
adr
;
z
=
recvfrom
(
s
,
/* Socket */
dgram
,
/* Receiving buffer */
sizeof
dgram
,
/* Max recv buf size */
0
,
/* Flags: no options */
(
struct
sockaddr
*
)
&
adr
,
/* Addr */
&
x
)
;
/* Addr len, in & out */
dgram
[
z
]
=
0
;
/* null terminate */
printf
(
"%s:%s
\n
"
,
inet_ntoa
(
adr.
sin_addr
)
,
dgram
)
;
}
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