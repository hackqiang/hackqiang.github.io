---
title: 准备做Nexus S的bootloader
tags:
  - bootloader
  - Nexus s
id: 1837
comment: false
categories:
  - embeded
  - 手机
  - 未分类
date: 2011-12-27 12:29:00
---

入手NS已经半年了，当初买这个手机主要是为了玩android，因为这个手机好刷，相对其他手机比较开放。
经历了一段时间的刷机后，觉得刷android已经没什么意思了，就开始研究起bootloader和recovery。
recovery没什么好说的，就像一个小系统，有意思的是bootloader，因为没有提供源码，竟然没有源码！
稍微看了下android源码目录里的bootable/bootloader/legacy，
觉得NS的bootloader应该是基于它修改了
，于是萌生了自己移植一个bootloader的想法。
最近先收集点资料，预计元旦开工。
12/29更新：昨天晚上仔细看了下bootable/bootloader/legacy，发现以前的推断有错，NS的bootloader不太可能基于他修改，因为他P都没有，没有一点有用的东西，还是走老路子，从u-boot移植吧，但是手机的bootloader还是和开发板不太一样的，毕竟涉及到一些加密的东西，所以可能会比较难，不过我还是要尝试尝试。