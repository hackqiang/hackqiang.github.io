---
title: __devexit_p的功能
id: 1797
comment: false
categories:
  - kernel/drivers
  - Linux
  - 未分类
date: 2010-07-14 19:52:00
tags:
---

看驱动的时候，时常会有如下代码：
.remove = __devexit_p(XX_exit),
这里的__devexit_p有什么作用呢？
我在include/linux/init.h中找到了它的定义：
/* Functions marked as __devexit may be discarded at kernel link time, depending
on config options.  Newer versions of binutils detect references from
retained sections to discarded sections and flag an error.  Pointers to
__devexit functions must use __devexit_p(function_name), the wrapper will
insert either the function_name or NULL, depending on the config options.
*/
#if defined(MODULE) || defined(CONFIG_HOTPLUG)
#define __devexit_p(x) x
#else
#define __devexit_p(x) NULL
#endif
注释已经说的狠明白了吧！