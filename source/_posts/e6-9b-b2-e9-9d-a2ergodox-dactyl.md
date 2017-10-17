---
title: 曲面ergodox--dactyl
id: 1936
comment: false
categories:
  - DIY
date: 2017-07-24 23:39:06
tags:
---

dactyl应该也是Kinesis的衍生项目，原作者的项目：https://github.com/adereth/dactyl-keyboard

我对模型稍作了一点修改：https://github.com/hackqiang/dactyl-keyboard

二狗用多了，便也对这个键盘产生了兴趣，反正有打印机，那就做做呗。

<!--more-->

![](https://hackqiang.org/wp-content/uploads/2017/07/20170723_220120-1024x768.jpg) ![](https://hackqiang.org/wp-content/uploads/2017/07/20170723_005525-1024x768.jpg) ![](https://hackqiang.org/wp-content/uploads/2017/07/20170722_003518-1024x768.jpg)  ![](https://hackqiang.org/wp-content/uploads/2017/07/20170722_003506-1024x768.jpg) ![](https://hackqiang.org/wp-content/uploads/2017/07/20170721_214828-1024x768.jpg) ![](https://hackqiang.org/wp-content/uploads/2017/07/20170721_211739-1024x768.jpg) ![](https://hackqiang.org/wp-content/uploads/2017/07/20170721_211720-1024x768.jpg) ![](https://hackqiang.org/wp-content/uploads/2017/07/20170716_123236-1024x768.jpg) ![](https://hackqiang.org/wp-content/uploads/2017/07/20170710_070801-1024x768.jpg) ![](https://hackqiang.org/wp-content/uploads/2017/07/20170713_221657-1024x768.jpg)

使用ergodone的固件和BL，完全按照ergodone的原理图来连线，有一个坑就是右手的vss和gnd在原理图中并没有连接，实际需要连接。另外trrs可以参考下图：

![](https://hackqiang.org/wp-content/uploads/2017/07/20170708_204739.jpg)

![](https://hackqiang.org/wp-content/uploads/2017/07/left.png) ![](https://hackqiang.org/wp-content/uploads/2017/07/right.png)

（在标签页打开图片可看原图）

（“SW5：7” 表示 “ row5 col7”）

另外因为dactyl相对ergodone少了两列，刚好烧配列的键没了，所以我就把‘T'补到那个位置了，这样按T可以刷配列了，但是就没法用原版的[tkg](http://tkg.io)生成正确的eep了，所以我clone了原版的tkg，增加了dactyl ergodone的键盘类型，放到自己的[tkg](https://tkg.hackqiang.org)，<del>因为没有改chrome插件，就没法在线刷配列了，需要下载eep在本地用tkg-toolkit-master刷。 </del>修改了chrome插件：https://github.com/hackqiang/tkg/raw/master/tkg-chrome-app.crx，支持在线刷了。

感谢KTEC的ergodone固件，给我带来了极大的方便。