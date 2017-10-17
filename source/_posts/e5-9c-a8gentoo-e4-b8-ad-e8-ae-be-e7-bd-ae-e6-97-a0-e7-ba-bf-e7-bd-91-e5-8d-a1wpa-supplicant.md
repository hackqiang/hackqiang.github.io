---
title: 在gentoo中设置无线网卡(wpa_supplicant)
tags:
  - gentoo
  - 无线网卡
id: 1796
comment: false
categories:
  - Linux
date: 2011-06-09 23:37:00
---

装好gentoo后，一直都是用的有线网卡，今天晚上捣鼓了下无线网卡的设置，成功了，在这记录一下。
因为我的无线使用wpa加密，刚好我的无线网卡在wpa_supplicant的支持列表中，所以我就毫不犹豫的选择了wpa_supplicant方案。
首先，下载安装wpa_supplicant：
emerge wpa_supplicant
然后生成一个配置文件：
bzip2 -d /usr/share/doc/wpa_supplicant-
/wpa_supplicant.conf.gz
cp /usr/share/doc/wpa_supplicant-
/wpa_supplicant.conf /etc
配置文件的修改可以参阅注释。
修改/etc/conf.d/net，添加：
modules=( “wpa_supplicant” )
config_wlan0=(“dhcp”)
最后添加网卡的开机启动：
ln -s /etc/init.d/net.lo /etc/init.d/net.wlan0
rc-update add net.wlan0 default
OK，搞定了