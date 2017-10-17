---
title: linux开机logo居中显示
id: 1809
comment: false
categories:
  - kernel/drivers
date: 2011-08-02 13:04:00
tags:
---

参考：
http://2836917.blog.51cto.com/2826917/511555
1.修改drivers/video/fbmen.c
?
View Code
C
471
472
473
474
// image.dx = 0;
// image.dy = y;
image.
dx
=
(
info
-&
gt
;
var.
xres
/
2
)
-
(
logo
-&
gt
;
width
/
2
)
;
image.
dy
=
(
info
-&
gt
;
var.
yres
/
2
)
-
(
logo
-&
gt
;
height
/
2
)
;
2.修改drivers/video/console/fbcon.c
增加
?
View Code
C
583
logo_height
+=
(
info
-&
gt
;
var.
yres
/
2
)
-
(
logo
-&
gt
;
height
/
2
)
;
OK