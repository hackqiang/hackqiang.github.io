---
title: /dev/dsplink一个及其诡异的问题
tags:
  - alsa
  - dsplink
  - oss
id: 1835
comment: false
categories:
  - kernel/drivers
  - Linux
  - 未分类
date: 2011-12-22 16:25:00
---

编译完，dsplink的相关模块加载都没有问题，但是当我运行dsp的测试程序的时候却出错了：
?
View Code
BASH
1
can
't open '
/
dev
/
dsplink
': No such file or directory
奇怪了，文件是存在的阿，再用cat，发现也是同样的错误，最后用重定向输入，这次倒是没有提示文件不存在的错误了。
怪，怪，真怪，我的第一反应是文件权限错了，我又仔细的看了一下文件属性，看样子没问题：
?
View Code
BASH
1
crw-------
1
root root
230
,
0
Dec
21
21
:
41
/
dev
/
dsplink
于是我又在一个相对纯净的rootfs（没有装很多的软件）上试了一次，发现一切正常，所以我有了如下推断：
1.内核应该不是问题，两次试验用的一个内核；
2.VFS那层是不是出了点问题；
3.是不是某个程序的影响，例如udev；
经过一段时间的排除，觉得是VFS出了点问题，开始debug kernel，在do_sys_open上下了断点，运行
?
View Code
BASH
1
cat
/
dev
/
dsplink
后，发现现象很怪异：打开了许多alsa的库文件（其实这里得到的结果没必要debug kernel，直接strace就好），这不应该阿，完全没有链接这些库嘛。
我突然想到，oss用的设备名不就是/dev/dspX吗，难道和这个有关系？
于是我直接运行
?
View Code
BASH
1
cat
/
dev
/
dsp
发现问题了，这个设备节点压根就不存在，却没出错，再试：
?
View Code
BASH
1
cat
/
dev
/
dspxxx
同样的没出错，这让我想到了adore的一个功能：通过插入一个内核模块，劫持vfs里的系统调用，实现了文件的隐藏，当然，这里的设备节点文件肯定不是被隐藏了。同理也可以实现文件的重定向访问，但是，我们自己的文件系统，自己的kernel，肯定没做过这些，这样分析看来，最大的疑点就落到了alsa上，再仔细一想，/dev/dsp是oss的东西，基本已经被抛弃，估计是对/dev/dsp[xxx]的访问都被重定向到/dev/snd上了，那么，又是谁做了这个重定向的工作呢？
问了下同事，原来是alsa-oss，那alsa-oss又是怎么做到的呢？
前面罗嗦了那么多，今天的主角来了–LD_PRELOAD，关于它，我也不想多说什么了，都老生常谈了，推荐一篇
好文章
。
再看看alsa-oss的源码alsa/alsa-oss.c，确实是这么回事：
?
View Code
C
1
125
if
(
strncmp
(
pathname
,
"/dev/dsp"
,
8
)
==
0
)
return
1
;
把这个地方改掉，还有alsa/pcm.c也有个类似的地方，应该就没什么问题了。
真是一个让人纠结的问题阿。