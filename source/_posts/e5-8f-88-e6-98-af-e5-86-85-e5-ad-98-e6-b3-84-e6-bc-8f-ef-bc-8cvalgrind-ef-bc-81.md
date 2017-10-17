---
title: 又是内存泄漏，valgrind！
tags:
  - valgrind
  - 内存泄漏
id: 1773
comment: false
categories:
  - C/C++
date: 2010-11-24 21:53:00
---

今天测试程序的时候，想看看CPU的占用率怎么样，无意间发现进程使用的内存一直增长。
果不其然，一会之后我的程序就被操作系统kill掉了。
以前记得有个内存泄漏的检测工具，不过好像有点麻烦，还要修改源代码。
同事给我推荐valgrind，果真很强大阿！
?
View Code
BASH
1
valgrind
--leak-check
=full .
/
test
如果输出结果太多不好看的话，可以增加 –log-file=valgrind_log ，在文件中慢慢分析。