---
title: zRAM分析1：zram设备
tags:
  - kernel
  - zram
id: 1879
comment: false
categories:
  - kernel/drivers
date: 2015-03-19 21:33:00
---

zRAM虽然说出来的时间挺长的，但是细节的资料不是很多，我把这几天看到的东西记录下，也方便后人。
zRAM是依赖swap机制的，核心的思想就是将待写入swap分区的页面压缩后写入内存，就要就避免了实际的swap分区，并且速度也相对快，最最关键的是对于一些使用flash设备的友好。
zRAM的主要文件都在drivers/block/zram中，核心文件很少：
zram_drv.c
以及为了减少内存碎片使用的一个内存分配器：
zsmalloc.c
关于这个内存分配器，后面再说。
惯例从init看起：