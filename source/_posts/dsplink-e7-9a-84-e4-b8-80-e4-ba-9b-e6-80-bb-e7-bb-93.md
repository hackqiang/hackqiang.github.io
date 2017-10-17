---
title: dsplink的一些总结
tags:
  - dsp
  - dsplink
id: 1832
comment: false
categories:
  - embeded
date: 2011-12-22 15:27:00
---

之前一直用的dspbridge，因为一些原因，需要换成dsplink.
1\. 编译dsplink最好的方法是下载dvsdk，配置好后（内核路径一定要配置好）直接make dsplink就行了。
2\. 如果要用kgdb调试dsplinkk.ko，必须要在配置编译kernel后再次编译dsplink，否则insmod时会出问题。
3\. 注意于alsa-oss库的冲突，看
这里
。
以后再更新。