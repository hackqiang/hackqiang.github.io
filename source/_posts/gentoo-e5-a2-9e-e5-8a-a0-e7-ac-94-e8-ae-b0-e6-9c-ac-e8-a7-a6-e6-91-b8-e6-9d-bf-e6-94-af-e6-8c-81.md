---
title: gentoo增加笔记本触摸板支持
tags:
  - gentoo
id: 1802
comment: false
categories:
  - Linux
date: 2011-06-28 07:33:00
---

支持装xorg时，没有在INPUT_DEVICE中添加synaptics，导致触摸板使用不正常，经过搜索摸索，解决了问题。
emerge -1 x11-drivers/xf86-input-synaptics
cp -r /usr/share/X11/xorg.conf.d /etc/X11
修改 /etc/X11/xorg.conf.d/10-evdev.conf ：
view plaincopy to clipboardprint?
Section “InputClass”
Identifier “evdev touchpad catchall”
MatchIsTouchpad “on”
MatchDevicePath “/dev/input/event*”
Driver “synaptics”
Option “TapButton1″ “1”
Option “TapButton2″ “2”
Option “TapButton2″ “3”
EndSection
重启。
参考资料：
http://en.gentoo-wiki.com/wiki/Synaptics_Touchpad
http://blog.csdn.net/changfengxiongfei/archive/2011/05/02/6384202.aspx