---
title: mount LVM
tags:
  - LVM
id: 1789
comment: false
categories:
  - Linux
  - 未分类
date: 2011-05-02 09:59:00
---

sudo apt-get install lvm2
sudo vgscan
sudo vgchange -ay volGroup0
sudo lvs
sudo mount /dev/volGroup0/logvol00 /mnt