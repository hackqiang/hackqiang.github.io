---
title: 在Ubuntu上安装配置python2.5
tags:
  - GAE
  - Python
id: 1745
comment: false
categories:
  - Linux
date: 2010-02-10 13:01:00
---

最近在弄GAE,但是我的ubuntu上的python的版本为2.6,我需要的是2.5.
于是安装2.5
?
View Code
BASH
1
sudo
apt-get
install
python2.5
然后修改默认的连接
?
View Code
BASH
1
2
3
sudo
rm
/
usr
/
bin
/
python
sudo
ln
-s
/
usr
/
bin
/
python2.5
/
usr
/
bin
/
python
这样在终端中输入python默认就是 2.5版本了