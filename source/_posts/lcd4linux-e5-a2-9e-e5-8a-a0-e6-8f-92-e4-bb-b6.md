---
title: lcd4linux增加插件
tags:
  - lcd4linux
id: 1804
comment: false
categories:
  - Linux
date: 2011-06-30 10:44:00
---

参考资料：http://ssl.bulix.org/projects/lcd4linux/wiki/plugin_howto
实例说明：
目标：写一个插件，功能为在lcd上显示字符串
使用的版本为lcd4linux-0.11.0-SVN
步骤：
1.
cp plugin_sample.c plugin_myecho.c
2.修改plugin.c 增加相关选项：
53行增加 “myecho”,
171行增加int plugin_init_myecho(void);
172行增加void plugin_exit_myecho(void);
267行增加 plugin_init_myecho();
483行增加plugin_exit_myecho();
3.修改makefile.in，增加相关选项；
71行后增加 plugin_myecho.$(OBJEXT)
253行增加 plugin_myecho.c
545行增加 @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/plugin_myecho.Po@am__quote@
4.修改plugins.m4，如果在plugin.c中如果没有使用宏开关，这个文件可不修改。
5.修改/etc/lcd4linux.conf。
附件：
1\.      plugin_myecho.c:
/* define the include files you need */
#include “config.h”
#include
#include
#include
/* these should always be included */
#include “debug.h”
#include “plugin.h”
#ifdef WITH_DMALLOC
#include
#endif
static void my_myecho(RESULT * result, RESULT * arg1)
{
char *val = R2S(arg1);
SetResult(&result, R_STRING, val);
}
/* plugin initialization */
/* MUST NOT be declared ‘static’! */
int plugin_init_myecho(void)
{
AddFunction(“myecho”, 1, my_myecho);
return 0;
}
void plugin_exit_myecho(void)
{
return;
}
2\.      lcd4linux.conf
Display LCD2USB {
Driver   ‘LCD2USB’
Port     ‘libusb’
Size     ’16×2′
}
Widget ECHO1 {
class  ‘Text’
expression  myecho(‘hackqiang’)
width  16
align  ‘L’
update tick
}
Layout Default {
Row1 {
Col1 ‘ECHO1′
}
}
Variables {
tick 50
}
Display ‘LCD2USB’
Layout  ‘Default’