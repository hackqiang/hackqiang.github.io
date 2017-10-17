---
title: 为u-boot增加自定义命令
tags:
  - u-boot
id: 1787
comment: false
categories:
  - embeded
  - 未分类
date: 2011-01-01 21:29:00
---

最近需要给u-boot增加一个命令，上网搜了搜，是找到了方法，但是对于我移植的版本（2010-09）并不适用，于是自己摸索了一翻，才发现是如此的简单。
例如我要增加一个boot_zImage的命令，操作如下：
第一步：在common目录下建立一个cmd_boot_zImage.c的文件；
第二步：修改cmd_boot_zImage.c，在文件尾添加关键代码：
U_BOOT_CMD(
boot_zImage, 1, 0,      do_boot_zImage,
“cmd_boot_zImage – boot Linux’s zImage\n”,
“”
);
第一行中各字段含义：
boot_zImage：在u-boot中运行的命令；
1：最大参数个数
0：repeat last command
第二行为usage信息；
第三行为help信息。
第三步：修改common/Makefile，增加：
COBJS-y += cmd_boot_zImage.o
OK，搞定！