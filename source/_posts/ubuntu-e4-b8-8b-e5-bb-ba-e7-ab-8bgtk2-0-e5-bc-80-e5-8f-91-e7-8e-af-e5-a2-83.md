---
title: Ubuntu下建立GTK2.0开发环境
tags:
  - gtk
id: 1753
comment: false
categories:
  - Linux
  - 未分类
date: 2010-03-08 18:25:00
---

之前的论文是在终端下实现的，现在打算作一个UI，因为是在用UBUNTU，所以打算用GTK2.0做。
下面是建立开发环境的详细步骤：
1。安装基本的库，开发包
sudo apt-get install libgtk2.0-dev
sudo apt-get install libgtk2.0-doc (可选)
sudo apt-get install gtk2-examples (可选)
2。安装UI设计工具glade。
sudo apt-get install glade