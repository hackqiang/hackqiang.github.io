---
title: kernel中添加logo
tags:
  - logo
id: 1824
comment: false
categories:
  - embeded
  - kernel/drivers
  - Linux
  - 未分类
date: 2011-08-01 12:33:00
---

简单记一下，免得以后翻。
1\. 做好224色的ppm文件logo_mylogo_clut224.ppm，放到drivers/video/logo下
2\. 在include/linux/linux_logo.h中添加
?
View Code
C
1
extern
const
struct
linux_logo logo_mylogo_clut224
;
3\. 在drivers/video/logo/Makefile中添加
?
View Code
C
1
obj
-
$
(
CONFIG_LOGO_MYLOGO_CLUT224
)
+=
logo_mylogo_clut224.
o
4\. 修改drivers/video/logo/Kconfig
?
View Code
C
1
2
3
4
config LOGO_MYLOGO_CLUT224
bool
"224-color logo"
depends on LOGO
default
y
5\. 修改drivers/video/logo/logo.c
?
View Code
C
1
2
3
4
#ifdef CONFIG_LOGO_MYLOGO_CLUT224
/* M32R Linux logo */
logo
=
&
amp
;
logo_mylogo_clut224
;
#endif
至于logo的居中显示，可以参考
http://qiang.ws/?p=613