---
title: 检查linux系统用户密码
id: 1805
comment: false
categories:
  - C/C++
  - Linux
  - 未分类
date: 2011-06-30 17:26:00
tags:
---

网上没找到什么资料，最后还是看login源码找到的方法。
/*
* 密码加密
*
* 编译： cc pwd.c -lcrypt
* usage:
* ./a.out passwd
*
*
*/
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
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <pwd.h>
#include <shadow.h>
#define SHADOW_PWD
int
checkpasswd
(
const
char
*
username
,
const
char
*
passwd
)
{
struct
passwd
*
pwd
=
NULL
;
char
*
salt
=
NULL
;
if
(
(
pwd
=
getpwnam
(
username
)
)
)
{
# ifdef SHADOW_PWD
struct
spwd
*
sp
;
if
(
(
sp
=
getspnam
(
username
)
)
)
pwd
-&
gt
;
pw_passwd
=
sp
-&
gt
;
sp_pwdp
;
# endif
salt
=
pwd
-&
gt
;
pw_passwd
;
}
else
salt
=
"xx"
;
//printf("read from /etc/shadow passwd:\t%s\n",pwd-&gt;pw_passwd);
//printf("crypted from %s passwd:\t%s\n",passwd,crypt(passwd, salt));
if
(
!
strncmp
(
crypt
(
passwd
,
salt
)
,
pwd
-&
gt
;
pw_passwd
,
strlen
(
pwd
-&
gt
;
pw_passwd
)
)
)
{
return
0
;
}
return
-
1
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
ret
=
checkpasswd
(
argv
[
1
]
,
argv
[
2
]
)
;
if
(
!
ret
)
printf
(
"success
\n
"
)
;
else
printf
(
"wrong passwd
\n
"
)
;
return
0
;
}