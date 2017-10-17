---
title: 关于SIGPIPE
tags:
  - SIGPIPE
id: 1781
comment: false
categories:
  - C/C++
date: 2010-12-30 17:04:00
---

最近在做网络编程，有时候程序会挂掉，调试发现程序收到了SIGPIPE，造成这个信号的原因可以自行google，因为程序收到SIGPIPE的默认动作是终止程序，所以我们需要对这个信号进行屏蔽。
在多进程的环境下，下面代码可以解决问题：
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
struct
sigaction sa
;
sa.
sa_handler
=
SIG_IGN
;
sa.
sa_flags
=
0
;
sigemptyset
(
&
amp
;
sa.
sa_mask
)
;
sigaddset
(
&
amp
;
sa.
sa_mask
,
SIGPIPE
)
;
if
(
sigaction
(
SIGPIPE
,
&
amp
;
sa
,
0
)
)
{
perror
(
"failed to ignore SIGPIPE"
)
;
exit
(
-
1
)
;
}
如果是在多线程的环境下，在创建线程之前需要：
?
View Code
C
1
2
3
4
5
6
sigset_t signal_mask
;
sigemptyset
(
&
amp
;
signal_mask
)
;
sigaddset
(
&
amp
;
signal_mask
,
SIGPIPE
)
;
if
(
pthread_sigmask
(
SIG_BLOCK
,
&
amp
;
signal_mask
,
NULL
)
)
{
printf
(
"block sigpipe error
\n
"
)
;
}