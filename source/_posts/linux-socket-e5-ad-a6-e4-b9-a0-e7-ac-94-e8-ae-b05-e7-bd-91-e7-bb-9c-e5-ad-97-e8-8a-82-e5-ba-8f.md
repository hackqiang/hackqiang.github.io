---
title: Linux Socket 学习笔记5–网络字节序
tags:
  - C/C++
  - Linux
  - socket
  - 地址结构
id: 1686
comment: false
categories:
  - Linux
  - 未分类
  - 读书笔记
date: 2009-07-17 15:25:00
---

对于多字节的数据，不同的CPU有不同的处理方法，主要有以下两种方法：
1.小端字节序。就是把低位字节存储在起始位置。
2.大端字节序。就是把高位字节存储在起始位置。
intel的cpu采用的是小端字节序，而motorola的CPU则用的是大端字节序，如果intel的cpu和motorola的CPU进行直接的通讯，就会产生错误。
现在网络上采用的标准方式是大端字节序。
下面提供几个大／小端字节序相互转换的函数。
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
#include &lt;netinet/in.h&gt;
unsigned
long
htonl
(
unsigned
long
hostlong
)
;
unsigned
short
htons
(
unsigned
short
hostshort
)
;
unsigned
long
ntohl
(
unsigned
long
netlong
)
;
unsigned
short
ntohs
(
unsigned
short
netshort
)
;
这里有个记忆诀窍：”h”代表host,”n”代表network,”s”代表”short”,”l”代表”long”.