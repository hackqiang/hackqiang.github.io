---
title: VC++复习笔记1-Windows程序的运行机制
tags:
  - C/C++
  - VC++
  - 回调函数
id: 1694
comment: false
categories:
  - C/C++
  - 未分类
  - 读书笔记
date: 2009-07-23 13:07:00
---

没用VC++很久了,趁这个暑假有时间复习一下吧.
看了孙鑫老师的视频,感觉很多地方都生疏了.今天就复习第一章,Windows程序的运行机制.
先说一下大致的结构:
首先是入口函数WinMain,然后定义一个窗口类,接着注册窗口类,再创建窗口,显示窗口,编写消息循环机制,编写回调函数.
下面是一个简单的Windows程序的C代码:
?
View Code
C
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
#include <windows.h>
#include <stdio.h>
LRESULT CALLBACK WinProc
(
HWND hwnd
,
// handle to window
UINT uMsg
,
// message identifier
WPARAM wParam
,
// first message parameter
LPARAM lParam
// second message parameter
)
;
int
WINAPI WinMain
(
HINSTANCE hInstance
,
// handle to current instance
HINSTANCE hPrevInstance
,
// handle to previous instance
LPSTR lpCmdLine
,
// command line
int
nCmdShow
// show state
)
{
WNDCLASS wndcls
;
wndcls.
lpfnWndProc
=
WinProc
;
//注意这：回调函数名
wndcls.
lpszClassName
=
"WinClass"
;
//注意：类名
...

RegisterClass
(
&
amp
;
wndcls
)
;
//注册窗口类
HWND hwnd
;
hwnd
=
CreateWindow
(
"WinClass"
,
"这是标题"
,
WS_OVERLAPPEDWINDOW
,
0
,
0
,
600
,
400
,
NULL
,
NULL
,
hInstance
,
NULL
)
;
//具体参数参阅MSDN
ShowWindow
(
hwnd
,
SW_SHOWNORMAL
)
;
//显示窗口
UpdateWindow
(
hwnd
)
;
//刷新窗口
MSG msg
;
while
(
GetMessage
(
&
amp
;
msg
,
NULL
,
0
,
0
)
)
{
TranslateMessage
(
&
amp
;
msg
)
;
//翻译消息
DispatchMessage
(
&
amp
;
msg
)
;
//将消息交给回调函数处理
}
return
0
;
}
LRESULT CALLBACK WinSunProc
(
//回调函数
HWND hwnd
,
// handle to window
UINT uMsg
,
// message identifier
WPARAM wParam
,
// first message parameter
LPARAM lParam
// second message parameter
)
{
switch
(
uMsg
)
//消息处理
{
case
WM_CLOSE
:
DestroyWindow
(
hwnd
)
;
break
;
case
WM_DESTROY
:
PostQuitMessage
(
0
)
;
break
;
default
:
return
DefWindowProc
(
hwnd
,
uMsg
,
wParam
,
lParam
)
;
}
return
0
;
}
这里要注意窗口类里的lpfnWndProc和lpszClassName两个参数是与回调函数和CreateWindow里的参数是对应的.