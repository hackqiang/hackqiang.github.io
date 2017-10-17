---
title: usb2usb
tags:
  - DIY
  - keyboard
id: 1886
comment: false
categories:
  - DIY
date: 2017-04-13 20:22:26
---

因为要做一个优联版本的无线小键盘atreus，所以usb2usb是必须的。

usb2usb我就不多说了，看原作者hasu的帖子。

只要USB Host Shield 2.0和pro micro，就可以自己DIY了，可以把成本控制在22+40（不含邮费）。

具体的硬件连接yang已经说的比较详细了，我再总结归纳下。

<!--more-->

首先，USB Host Shield 2.0哪里买， http://duinopeak.com/store/index.php?route=product/product&amp;product_id=47，理论上来说，长的一样应该都可以。

然后，pro micro一定要买3.3v的版本，一般对于的晶振就是8MHZ。

正好这两个板子可以叠起来，尺寸会做的比较小。

还有就是因为接了3.3v，所以usb端口的电压就不够了，需要切断一处pcb上的走线，并接上5v的电压。

![](https://hackqiang.org/wp-content/uploads/2017/04/cut.jpg)

固件的话，记得要再makefile中把频率改成8MHZ，可以参考我的代码：

https://github.com/hackqiang/tmk_keyboard/commit/fb83b1830349ff4fda5468b250f61a0b531b1d4f

最后增加一个rst按钮，再打印个外壳：

![](https://hackqiang.org/wp-content/uploads/2017/04/20170418_214951-1024x768.jpg)

外壳stl下载地址：

http://www.thingiverse.com/thing:2256751

ref：

1.  https://forum.colemak.com/topic/2158-dreymars-big-bag-of-keyboard-tricks-usb2usb-edition/
2.  https://geekhack.org/index.php?topic=69169.0
3.  https://geekhack.org/index.php?topic=80421