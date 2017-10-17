---
title: mips delay slot那点事
tags:
  - mips
id: 1860
comment: false
categories:
  - embeded
date: 2012-11-30 18:07:00
---

接触mips也有一段时间了，发现了delay slot的一个有趣的地方。
首先，问题是怎么引入的呢？
最近做mips exception方面的东西，基于ecos，打算支持coredump，以便系统发生崩溃的时候得到一些信息，但是ecos的一些特性（如不支持MMU，kernel space和user space未隔离），导致coredump不能像在linux kernel中那么得到，最终coredump的内容还是生成了，但是我要怎么把它写入u盘呢？显然在exception模式下是不现实的。于是，EPC登场了，mips 有个precise exception的概念，也就是when exception occured, EPC总是指向受害指令，但是有一个例外，那就是如果受害指令处于delay slot，那么epc会指向受害指令之前的那条分支指令。我的想法是直接用一条jal指令替换掉受害指令，这样就能在exception返回后运行我的函数。
那么，如果受害指令处于delay slot中，那么我修改后的代码就类似于：
jal xxxx
jal yyyy
nop
第二条就由原本的受害指令被我修改成一条跳转指令，它在“jal xxxx”的delay slot中，但是他本身又是一条分支指令，应该再去执行它delay slot中的指令，这就让人费解了，到底这样的指令执行的结果会是怎么样的？
实践证明，第二条和第三条指令不会被执行到，不明白这是特性呢，还是bug？