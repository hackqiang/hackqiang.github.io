---
title: 交叉编译iperf
id: 1816
comment: false
categories:
  - embeded
  - Linux
  - 未分类
date: 2011-09-30 14:10:00
tags:
---

for s3c2440:
1\. export ac_cv_func_malloc_0_nonnull=yes
2\. ./configure –build=i686-linux –host=arm-none-linux-gnueabi –target=arm-none-linux-gnueabi
3\. 修改src/Makefile: CXXFLAGS,CPPFLAGS,CFLAGS后的 “=” 换成 “+=”
4\. make CXXFLAGS=-march=armv4t CPPFLAGS=-march=armv4t CFLAGS=-march=armvt
for dm3730:
just
1\. export ac_cv_func_malloc_0_nonnull=yes
2\. ./configure –build=i686-linux –host=arm-none-linux-gnueabi –target=arm-none-linux-gnueabi