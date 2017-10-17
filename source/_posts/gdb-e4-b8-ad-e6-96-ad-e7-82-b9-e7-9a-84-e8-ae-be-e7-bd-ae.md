---
title: GDB中断点的设置
tags:
  - GDB
id: 1705
comment: false
categories:
  - Linux
  - 未分类
date: 2009-07-28 12:41:00
---

在进行调试程序的时候会经常需要设置断点，GDB很好的支持了断点。
设置一个断点的命令是break(b).后面加行数或函数名，生成的每个断点都有一个编号。下面列出几个在设置断点时常用到的函数：
continue(c):从当前位置连续运行，直到遇到断点。
run(r):从程序开始处连续运行，直到断点。
info(i) breakpoints :显示所有断点。
delete breakpoints X:删除编号为x的断点。
disable/enable breakpoints x :使编号为x的断点失效/生效。
display s:跟踪查看变量s的值。
undisplay s:取消变量s的跟踪。
此外，GDB还可以让一个断点在满足一定的条件才有效。例如：
>break 5 if x>0
它的意思是在第5行设置一个断点，但只当x>0时断点才生效。