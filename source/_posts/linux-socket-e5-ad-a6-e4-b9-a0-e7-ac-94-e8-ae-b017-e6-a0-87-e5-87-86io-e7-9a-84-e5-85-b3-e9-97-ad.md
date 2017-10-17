---
title: Linux Socket 学习笔记17-标准I/O的关闭
tags:
  - I/O
id: 1712
comment: false
categories:
  - Linux
  - 未分类
  - 读书笔记
date: 2009-08-02 20:25:00
---

当打开多个文件描述符时就不能再简单的使用shutdown()函数了,因为shutdown()函数是不考虑套接口上打开的文件描述符个数的.
当连接建立后,我们需要考虑3种情况:
(在只关闭写端的情况下)进程只等待接收数据,而不再写数据.
(在只关闭读端的情况下)进程只试探写数据,而不再接收数据.
(同时关闭读写端的情况下)进程不进行读写操作.
第一中情况用源码表示:
fflush(wx);
shutdown(fileno(wx),SHUT_WR);
fclose(wx);
在关闭之前要先清除输出流,使用函数fflush().fileno()函数用于获得文件描述符.
第二中情况用源码表示:
shutdown(fileno(rx),SHUT_RD);
fclose(rx);
第三中情况用源码表示:
fclose(wx);
shutdown(fileno(rx),SHUT_DOWN);
fclose(rx);