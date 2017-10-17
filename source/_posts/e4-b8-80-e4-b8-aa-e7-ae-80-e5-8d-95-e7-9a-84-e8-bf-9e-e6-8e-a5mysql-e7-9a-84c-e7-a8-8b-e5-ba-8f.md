---
title: 一个简单的连接Mysql的C程序
tags:
  - C/C++
  - Mysql
id: 1751
comment: false
categories:
  - C/C++
  - 未分类
  - 读书笔记
date: 2010-02-23 11:02:00
---

这段代码主要是为了测试Mysql C环境是不是安装好。
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
//file name: dbtest.c
#include <stdio.h>
#include <stdlib.h>
#include <mysql.h>
int
main
(
)
{
MYSQL mysql
;
mysql_init
(
&
mysql
)
;
return
0
;
}
接下来编译：
?
View Code
BASH
1
gcc
-lmysqlclient
dbtest.c
-o
dbtest
如果没有报错，应该就没问题了。