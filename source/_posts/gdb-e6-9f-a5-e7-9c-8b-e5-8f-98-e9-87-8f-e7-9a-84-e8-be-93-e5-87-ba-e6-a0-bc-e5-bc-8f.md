---
title: GDB查看变量的输出格式
tags:
  - GDB
id: 1736
comment: false
categories:
  - Linux
  - 未分类
date: 2009-09-26 10:26:00
---

今天用GDB调试程序，发现了一个问题，就是查看变量的时候显示格式很不好看，就如我要看一个数组里所有成员的十六进制表示，那么要怎么设置呢？
其实在使用命令print 和 display的时候可以更改显示格式，例如：
display /x  var
表示把var用十六进制显示。
其他常用的输出格式有有：
x:十进制
u:无符号的十六进制
o:八进制
t:二进制
c:字符格式