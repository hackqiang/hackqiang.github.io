---
title: 为Ubuntu9.10安装配置Mysql
tags:
  - Mysql
id: 1749
comment: false
categories:
  - Linux
date: 2010-02-21 19:15:00
---

今天早上在床上的时候突然想起要给论文程序里加上一个数据库，因为在Linux平台，于是很自然的想到了Mysql。
这篇文章主要介绍了在Ubuntu9.10上安装配置Mysql，并建立其C开发环境。
第一步
，安装Mysql，可以参考这里：
http://wiki.ubuntu.org.cn/MySQL%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97
?
View Code
BASH
1
2
sudo
apt-get
install
mysql-server
sudo
apt-get
install
mysql-client
然后重启Mysql：
?
View Code
BASH
1
sudo
/
etc
/
init.d
/
mysql restart
非root用户可以通过以下命令进入Mysql：
?
View Code
BASH
1
mysql
-u
root
-p
第二步
，创建一个数据库，并赋予当前登录用户的权限。
?
View Code
BASH
1
2
3
4
5
mysql
-u
root
-p
mysql
&
gt; create database dbforc;
mysql
&
gt; grant all privileges on dbforc.
*
to qiang
@
localhost identified by
'123'
;
(
我的登录名为qiang,密码设为
123
)
mysql
&
gt; flush privileges;（刷新系统权限表）
mysql
&
gt; quit;
现在，就可以用下面的命令进入Mysql：
?
View Code
BASH
1
mysql
-u
qiang
-p
详细的数据库操作命令在这就不多说了，给个地址参考参考：
http://news.newhua.com/news1/program_database/2009/217/0921715343537K7H7IDI2CCI09JCI1DK8FJ4B07B3A04219G561C3JAB.html