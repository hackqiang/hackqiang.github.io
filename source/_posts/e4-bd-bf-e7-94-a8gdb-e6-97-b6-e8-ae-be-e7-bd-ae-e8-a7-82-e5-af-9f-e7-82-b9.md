---
title: 使用GDB时设置观察点
tags:
  - GDB
id: 1710
comment: false
categories:
  - Linux
date: 2009-07-31 17:33:00
---

调试程序的时候除了要设置断点，有时还需要设置观察点，即监视一个变量，当他的值改变时程序暂停。
设置观察点的命令为：watch.
例如watch  var即为变量var设置一个观察点。
下面是几个经常用到的命令：
i watchpoints:显示所有观察点。
x var：打印变量var起始地址一段区域的内存，以字节为单位。