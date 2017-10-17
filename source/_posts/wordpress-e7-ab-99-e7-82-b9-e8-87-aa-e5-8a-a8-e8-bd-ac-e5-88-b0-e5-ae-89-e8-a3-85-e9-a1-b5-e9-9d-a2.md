---
title: wordpress站点自动转到安装页面
tags:
  - wordpress
id: 1743
comment: false
categories:
  - 乱七八糟
date: 2010-02-09 20:31:00
---

废话不多说,直接把数据库的前缀(默认wp_)改掉(在wp-config.php文件中),然后把数据库文件中的wp_替换成刚刚修改的值,最后还原数据库.
应该可以了吧?