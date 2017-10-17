---
title: Ubuntu下用rar命令分卷压缩文件
tags:
  - Ubuntu
  - 命令技巧
id: 1724
comment: false
categories:
  - Linux
date: 2009-08-19 12:56:00
---

今天下了个文档，DOC格式，用openoffic直接输出为pdf文档。传上论坛给大家共享，因为论坛的附件大小限制，必须分卷压缩。
之前在UBUNTU上装了RAR，所以打算用RAR命令进行压缩。于是先man了下rar，结果没有rar的man文档，于是上网找资料。
最后终于弄会了。这里给大家说说。
可以用这个命令：
rar a -v<size>(k,b) archives files
假如我在Desktop目录下有个大小为5M的文档 file.pdf, 现在要把它压缩为大小为2000k的几个部分，文件名为file.part1.rar ,file.part2.rar …
就可以用下面的命令：
?
View Code
BASH
1
$ rar a
-v2000k
file
file.pdf
OK,这就行了。