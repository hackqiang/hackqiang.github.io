---
title: 终于能在LINUX下用淘宝了
tags:
  - 淘宝
id: 1732
comment: false
categories:
  - Linux
date: 2009-09-14 13:19:00
---

今天无意间看了一篇文章，实现了在LINUX下用淘宝。
先下载:
支付宝安全控件 for Linux 平台 的 Firefox
( MD5:
02240053d32688ed996e3a4788042801
)
将下载的文件解压:
?
View Code
BASH
1
$
tar
-zxvf
aliedit.tar.gz
推荐校验 MD5 值：
?
View Code
BASH
1
$ md5sum aliedit.tar.gz
02240053d32688ed996e3a4788042801  aliedit.tar.gz
创建~/.mozilla/plugins目录
?
View Code
BASH
1
mkdir
~
/
.mozilla
/
plugins
并将这两个文件复制到 ~/.mozilla/plugins 目录：
?
View Code
BASH
1
$
cp
aliedit.so aliedit.xpt ~
/
.mozilla
/
plugins
重新启动 Firefox 即可。整个安装过程还是很简单的。