---
title: C 程序来访问和设置环境变量
tags:
  - 环境变量
id: 1725
comment: false
categories:
  - C/C++
  - Linux
  - 未分类
date: 2009-08-22 10:46:00
---

对于 C 程序的用户来说,可以使用下列三个函数来设置或访问一个环境变量。
◆ getenv()访问一个环境变量。输入参数是需要访问的变量名字,返回值是一个字符串。如果所访问的环境变量不存在,则会返回 NULL。
◆ setenv()在程序里面设置某个环境变量的函数。
◆ unsetenv()清除某个特定的环境变量的函数。
另外,还有一个指针变量 environ,它指向的是包含所有的环境变量的一个列表。下面的程序可以打印出当前运行环境里面的所有环境变量:
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
#include <stdio.h>
extern
char
**
environ
;
int
main
(
)
{
char
**
var
;
for
(
var
=
environ
;*
var
!=
NULL
;++
var
)
printf
(
"%s
\n
"
,*
var
)
;
return
0
;
}
还可以通过修改一些相关的环境定义文件来修改环境变量,比如对于 Red Hat 等 Linux 发行版本,与环境相关的文件有/etc/profile 和~/.bashrc 等。修改完毕后重新登录一次就生效了。
以上总结自《开源》杂志。