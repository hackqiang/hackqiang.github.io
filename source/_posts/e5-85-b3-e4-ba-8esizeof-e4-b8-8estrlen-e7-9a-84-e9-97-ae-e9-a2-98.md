---
title: 关于sizeof与strlen的问题
tags:
  - 面试
id: 1741
comment: false
categories:
  - C/C++
  - 未分类
date: 2009-11-07 19:43:00
---

今天开始作面试题了，准备找工作了。
关于sizeof和strlen的问题，以前就接触到了，现在再提一下。
先看看这个：
Char *a=”1234567890″;
Sizeof(a)=?
Strlen(a)=?
答案是
Sizeof(a)=4,它相当于sizeof(char *)
Strlen(a)=10
再看看这个：
Char a[]=”1234567890″;
Sizeof(a)=?
Strlen(a)=?
Sizeof(a)=11,它包含了自动生成的’\0′,
Strlen(a)=10.它并不包含那个’\0′.