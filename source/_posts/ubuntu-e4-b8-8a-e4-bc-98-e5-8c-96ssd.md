---
title: ubuntu上优化SSD
tags:
  - Linux
  - SSD
  - Ubuntu
id: 1688
comment: false
categories:
  - Linux
date: 2009-07-19 10:07:00
---

前几天在笔记本上装上了UBUNTU，因为是SSD硬盘，所以上网找了点资料，优化SSD。在这记录一下。
第一步：
编辑fstab文件：
前几天在笔记本上装上了UBUNTU，因为是SSD硬盘，所以上网找了点资料，优化SSD。在这记录一下。
第一步：
编辑fstab文件：
?
View Code
BASH
1
sudo
gedit
/
etc
/
fstab
把relatime都改成noatime.
第二步，建立一个虚拟磁盘
在fstab最后加上这一行：
tmps /tmp tmps default, noatime,mode=1777 00 0
这样就在每次开机的时候挂载了一个由内存构成的虚拟分区/tmp。
最后，把一些程序的cache都移到这个虚拟分区。
举个例子，把firefox的缓存移到/tmp：
打开firefox,输入about:config打开设置。添加一个新字符串，名称为：browser.cache.disk.parent_directory，值为/tmp。