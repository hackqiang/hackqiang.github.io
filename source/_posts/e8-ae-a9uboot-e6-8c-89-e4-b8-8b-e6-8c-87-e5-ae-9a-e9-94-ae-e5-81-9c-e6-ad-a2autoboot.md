---
title: 让uboot按下指定键停止autoboot
tags:
  - u-boot
id: 1831
comment: false
categories:
  - embeded
date: 2011-12-19 23:05:00
---

默认uboot是按下任意键停止autoboot，有人觉得不爽，害怕终端操作用户误操作，要指定特殊按键
这个功能很简单，例如要按下ESC键，停止自动boot
只需要添加
?
View Code
C
1
2
3
4
5
6
7
#define CONFIG_AUTOBOOT_KEYED 1
#define CONFIG_AUTOBOOT_PROMPT "Press ESC to abort autoboot in %d seconds"
#define CONFIG_AUTOBOOT_DELAY_STR "linux"
#define CONFIG_AUTOBOOT_STOP_STR "\x1b"
即可，0x1B就是ESC的ascii码。
来源：
http://blog.chinaunix.net/space.php?uid=13889805&do=blog&id=1641961