---
title: gentoo与kernel-3.0-rc1的环境下emerge nss
tags:
  - gentoo
id: 1803
comment: false
categories:
  - Linux
date: 2011-06-28 07:37:00
---

因为用的3.0的内核，nss源码文件中没有Linux3.0.mk，emerge的时候出问题，最简单的一个方法，
写一个脚本：
#!/bin/bash
cp /usr/tmpportage/dev-libs/nss-3.12.9-rc1/work/nss-3.12.9/mozilla/security/coreconf/Linux2.6.mk /usr/tmpportage/dev-libs/nss-3.12.9-rc1/work/nss-3.12.9/mozilla/security/coreconf/Linux3.0.mk
在emerge中显示source prepared后，立即执行此脚本。