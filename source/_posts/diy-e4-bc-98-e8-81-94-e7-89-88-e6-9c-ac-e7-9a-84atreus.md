---
title: DIY 优联版本的atreus
tags:
  - atreus
  - keyboard
id: 1896
comment: false
categories:
  - DIY
date: 2017-04-18 23:17:25
---

atreus项目应该是受到了ergodox的启发产生的，项目地址是：

https://github.com/technomancy/atreus

我觉得这么小的键盘不搞个无线的话没什么意思，正好看到yang DIY的40优联，决定也做一个优联版的，配合usb2usb实现自定义的配列。

<!--more-->

既然是自己DIY，那么能自己做的东西一定要自己做起来，外壳和定位板先打印出来：

![](https://hackqiang.org/wp-content/uploads/2017/04/20170410_184910-1024x768.jpg) ![](https://hackqiang.org/wp-content/uploads/2017/04/20170416_070126-1024x768.jpg)

正好翻出了以前diy牛反的碳纤维贴纸，贴顶层。

选择罗技 k230的主控，便宜也够用。

因为atreus的键只有42个，所以没必要按照原来的k230矩阵飞线了，为了简化飞线，我就选取了其中的4行，加上12列，矩阵如下：

![](https://hackqiang.org/wp-content/uploads/2017/04/matrix-1024x625.png)

因为原本的k230矩阵是经过优化的，一定程度上减少了按键冲突，但是我这么一简化飞线，按键冲突就会比较明显了，所以要为每一个轴增加一个二极管防冲突：

![](https://hackqiang.org/wp-content/uploads/2017/04/QQ截图20170418234454-1024x516.png)

最后使用两块CR2032，保守估计1年不用换电池了。

![](https://hackqiang.org/wp-content/uploads/2017/04/222222222222-1024x577.png)

在此借用yang的一张矩阵图，下半部分是按照我这个矩阵得到的key映射表，这长表后面配置usb2usb的固件时要用到：

![](https://hackqiang.org/wp-content/uploads/2017/04/QQ截图20170418234646-1024x638.png)

再凑点垃圾键帽，装上壳子，硬件上，键盘就差不多OK了（上面我的ergodone露出了半截）：

![](https://hackqiang.org/wp-content/uploads/2017/04/1111111-1024x628.png)

下面就该去改usb2usb的代码了：

https://github.com/hackqiang/tmk_keyboard/commit/fb83b1830349ff4fda5468b250f61a0b531b1d4f

配列的修改有两种方式：

1.  首先定义一个key的映射，在源码中里定义好配列，就不多说了。参考keymap_unifyingAtreus.c。直接make KEYMAP=unifyingAtreus
2.  通过KLE以及TKG，图形化的配置。

    1.  tkg的地址为https://tkg.io，KLE为http://www.keyboard-layout-editor.com。
    2.  这是原本的[矩阵](http://www.keyboard-layout-editor.com/##@_name=unifying%20matrix%20for%20Atreus&amp;notes=%5B%7Ba%2F:7%7D,%22C%22,%22E%22,%7Ba%2F:5%7D,%22%7C%5Cn%5C%5C%22,%7Ba%2F:7%7D,%22enter%22,%22I%22,%7Bx%2F:2%7D,%22D%22,%7Ba%2F:5%7D,%22!%5Cn1%22,%22~%5Cn%60%22,%22$%5Cn4%22,%7Ba%2F:7%7D,%22esc%22%5D,%0A%5B%22B%22,%7Ba%2F:5%7D,%223%5Cnpgdn%22,%226%5Cn%E2%86%92%22,%7Ba%2F:7%7D,%22L%22,%22P%22,%7Bx%2F:2%7D,%22Q%22,%7Ba%2F:5%7D,%22%7B%5Cn%5B%22,%7Ba%2F:7%7D,%22T%22,%22F8%22,%22F4%22%5D,%0A%5B%22N%22,%22numlock%22,%7Ba%2F:5%7D,%229%5Cnpgup%22,%22%2F:%5Cn%2F%3B%22,%7Ba%2F:7%7D,%22Y%22,%7Bx%2F:2%7D,%22caps%22,%22F12%22,%22X%22,%22F9%22,%22F5%22%5D,%0A%5B%22space%22,%22+%22,%22bs%22,%7Ba%2F:5%7D,%228%5Cn%E2%86%91%22,%22%5E%5Cn6%22,%7Ba%2F:7%7D,%22Z%22,%22F11%22,%22F1%22,%22F2%22,%22W%22,%22tab%22,%22F6%22%5D%3B&amp;@_r:10&amp;rx:1&amp;y:-0.09999999999999998&amp;x:2&amp;a:5%3B&amp;=%7C%0A%5C%3B&amp;@_y:-0.65&amp;x:1&amp;a:7%3B&amp;=E&amp;_x:1%3B&amp;=enter%3B&amp;@_y:-0.75%3B&amp;=C%3B&amp;@_y:-0.9&amp;x:4%3B&amp;=I%3B&amp;@_y:-0.7000000000000001&amp;x:2&amp;a:5%3B&amp;=6%0A%E2%86%92%3B&amp;@_y:-0.6499999999999999&amp;x:1%3B&amp;=3%0Apgdn&amp;_x:1&amp;a:7%3B&amp;=L%3B&amp;@_y:-0.75%3B&amp;=B%3B&amp;@_y:-0.8999999999999999&amp;x:4%3B&amp;=P%3B&amp;@_y:-0.7000000000000002&amp;x:2&amp;a:5%3B&amp;=9%0Apgup%3B&amp;@_y:-0.6499999999999999&amp;x:1&amp;a:7%3B&amp;=numlock&amp;_x:1&amp;a:5%3B&amp;=%2F:%0A%2F%3B%3B&amp;@_y:-0.75&amp;a:7%3B&amp;=N%3B&amp;@_y:-0.8999999999999999&amp;x:4%3B&amp;=Y%3B&amp;@_y:-0.75&amp;x:5&amp;h:1.5%3B&amp;=Z%3B&amp;@_y:-0.9500000000000002&amp;x:2%3B&amp;=bs%3B&amp;@_y:-0.6499999999999999&amp;x:1%3B&amp;=+&amp;_x:1&amp;a:5%3B&amp;=8%0A%E2%86%91%3B&amp;@_y:-0.75&amp;a:7%3B&amp;=space%3B&amp;@_y:-0.8999999999999999&amp;x:4&amp;a:5%3B&amp;=%5E%0A6%3B&amp;@_r:-10&amp;rx:7&amp;ry:0.965&amp;y:-0.20000000000000018&amp;x:2%3B&amp;=~%0A%60%3B&amp;@_y:-0.6499999999999999&amp;x:1%3B&amp;=!%0A1&amp;_x:1%3B&amp;=$%0A4%3B&amp;@_y:-0.75&amp;x:4&amp;a:7%3B&amp;=esc%3B&amp;@_y:-0.8999999999999999%3B&amp;=D%3B&amp;@_y:-0.7000000000000002&amp;x:2%3B&amp;=T%3B&amp;@_y:-0.6499999999999999&amp;x:1&amp;a:5%3B&amp;=%7B%0A%5B&amp;_x:1&amp;a:7%3B&amp;=F8%3B&amp;@_y:-0.75&amp;x:4%3B&amp;=F4%3B&amp;@_y:-0.8999999999999999%3B&amp;=Q%3B&amp;@_y:-0.7000000000000002&amp;x:2%3B&amp;=X%3B&amp;@_y:-0.6499999999999999&amp;x:1%3B&amp;=F12&amp;_x:1%3B&amp;=F9%3B&amp;@_y:-0.7500000000000004&amp;x:4%3B&amp;=F5%3B&amp;@_y:-0.9000000000000004%3B&amp;=caps%3B&amp;@_y:-0.7499999999999996&amp;x:-1&amp;h:1.5%3B&amp;=F11%3B&amp;@_y:-0.9499999999999997&amp;x:2%3B&amp;=W%3B&amp;@_y:-0.6500000000000004&amp;x:1%3B&amp;=F2&amp;_x:1%3B&amp;=tab%3B&amp;@_y:-0.75&amp;x:4%3B&amp;=F6%3B&amp;@_y:-0.9000000000000004%3B&amp;=F1)，把raw中的数据复制到tkg的USB2USB的”设定“中.
    3.  在KLE中配置自己的配列，例如[我的](http://www.keyboard-layout-editor.com/##@_backcolor=%23b3aaaa&amp;name=qiang)，复制raw到TKG的"层"中，选择“简单”模式，设置下fn的效果。
    4.  点击下载.c文件，放到tmk_keyboard/converter/usb_usb中，重命名为keymap_tkg.c，然后make KEYMAP=tkg
生成的hex通过Arduloader烧到USB2USB中就可以了。

&nbsp;