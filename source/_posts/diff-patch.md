---
title: diff patch
tags:
  - patch
  - 命令技巧
id: 1785
comment: false
categories:
  - Linux
  - 未分类
date: 2011-06-01 21:10:00
---

diff -Naur a/ b/ > patchfile
cd a/
patch -p1
patch to "a/", so now "a/" is the same as "b/"