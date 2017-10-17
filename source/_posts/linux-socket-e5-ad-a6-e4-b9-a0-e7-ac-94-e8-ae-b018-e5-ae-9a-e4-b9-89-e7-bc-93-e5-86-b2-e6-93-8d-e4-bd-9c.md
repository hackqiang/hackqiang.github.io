---
title: Linux Socket 学习笔记18-定义缓冲操作
tags:
  - I/O
  - 缓冲
id: 1713
comment: false
categories:
  - Linux
  - 未分类
  - 读书笔记
date: 2009-08-03 13:23:00
---

使用stdio(3)时,通常会用到缓冲技术.从而提高整个系统的I/O效率.
Linux中的FILE流有三种基本的饿缓冲模式:
全缓冲(“块缓冲”)
线形缓冲
无缓冲
用于缓冲控制的函数:
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
#include<stdio.h>
int
setbuf
(
FILE
*
stream
,
char
*
buf
)
;
int
setbuffer
(
FILE
*
stream
,
char
*
buf
,
size_t size
)
;
int
setlinebuf
(
FILE
*
stream
)
;
int
setvbuf
(
FILE
*
stream
,
char
*
buf
,
int
mode
,
size_t size
)
;
setvbuf中mode的取值有:
_IOFBF:全缓冲
_IOLBF:线形缓冲
_IONBF:无缓冲