---
title: 建立Mysql C开发环境
tags:
  - C
  - Mysql
  - Ubuntu
id: 1750
comment: false
categories:
  - Linux
date: 2010-02-21 19:27:00
---

之前安装了Mysql，现在开始建立C开发环境。
安装C语言编程接口：
?
View Code
BASH
1
sudo
apt-get
install
libmysqlclient15-dev
很简单，接口装好了，具体的接口函数可以参考这里：
http://dev.mysql.com/doc/refman/5.0/en/c.html
相关mysql头文件和库文件安装在/usr/include/mysql/和/usr/lib/mysql目录
把lib和头文件拷贝到公用：
sudo cp /usr/lib/mysql/* /usr/lib/
sudo cp /usr/include/mysql/* /usr/include/
这样，就可以直接用：
?
View Code
C
1
#include <mysql.h>
来替换
?
View Code
C
1
#include "/usr/include/mysql/mysql.h"
这篇文章的主要参考资料：
http://feizf.blogbus.com/logs/30689586.html