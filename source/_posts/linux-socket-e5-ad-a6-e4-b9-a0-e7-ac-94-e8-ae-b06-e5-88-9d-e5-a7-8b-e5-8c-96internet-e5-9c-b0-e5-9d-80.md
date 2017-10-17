---
title: Linux Socket 学习笔记6–初始化Internet地址
tags:
  - C/C++
  - Linux
  - socket
  - 地址结构
id: 1689
comment: false
categories:
  - Linux
  - 未分类
  - 读书笔记
date: 2009-07-19 16:19:00
---

Internet地址又可以分为通配地址和特定地址。
通配地址主要是为了适应一台电脑有多块网卡或一张网卡上邦定了多个地址的情况。
下面是初始化一个具有通配地址和通配端口号的AF_INET地址。
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
struct
sockaddr_in adr_inet
;
int
addr_len
;
menset
(
&
amp
;
adr_inet
,
0
,
sizeof
(
adr_inef
)
)
;
addr_inet.
sin_family
=
AF_INET
;
addr_inet.
sin_port
=
ntohs
(
0
)
;
addr_inet.
sin_addr
.
s_addr
=
ntohl
(
INADDR_ANY
)
;
adr_len
=
sizeof
(
adr_inet
)
;
千万要注意这里用的 是函数ntohl()和ntols()。
现在学习初始化一个特定的Internet地址。现看代码吧：
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
/*
* Establishing a Specific AF_INET
* Socket Address:
*/
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <netinet/in.h>
/*
* This function reports the error and
* exits back to the shell :
*/
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
perror
(
on_what
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
,
char
**
envp
)
{
int
z
;
/* Status return code */
int
sck_inet
;
/* Socket  */
struct
sockaddr_in adr_inet
;
/* AF_INET */
int
len_inet
;
/* length  */
const
unsigned
char
IPno
[
]
=
{
127
,
0
,
0
,
23
/* Local loopback */
}
;
/* Create an IPv4 Internet Socket */
sck_inet
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
if
(
sck_inet
==
-
1
)
bail
(
"socket()"
)
;
/* Create an AF_INET address */
memset
(
&
amp
;
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
9000
)
;
memcpy
(
&
amp
;
adr_inet.
sin_addr
.
s_addr
,
IPno
,
4
)
;
len_inet
=
sizeof
adr_inet
;
/* Now bind the address to the socket */
z
=
bind
(
sck_inet
,
(
struct
sockaddr
*
)
&
amp
;
adr_inet
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
"bind()"
)
;
/* Display all of our bound sockets */
system
(
"netstat -pa --tcp 2&gt;/dev/null | "
"sed -n '1,/^Proto/p;/af_inet/p'"
)
;
close
(
sck_inet
)
;
return
0
;
}
这也要注意，用的函数是htonl()。