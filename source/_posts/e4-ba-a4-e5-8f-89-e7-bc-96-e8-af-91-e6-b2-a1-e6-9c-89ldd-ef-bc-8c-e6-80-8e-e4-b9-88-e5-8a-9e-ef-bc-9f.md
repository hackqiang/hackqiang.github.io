---
title: 交叉编译没有ldd，怎么办？
tags:
  - 命令技巧
id: 1867
comment: false
categories:
  - embeded
  - 未分类
date: 2013-06-08 11:50:00
---

?
View Code
C
1
mipsel
-
linux
-
gnu
-
readelf
-
d a.
out
|
grep NEEDED