---
title: ubuntu9.10下配置apache支持CGI
tags:
  - apache
  - cgi
id: 1765
comment: false
categories:
  - Linux
date: 2010-08-16 15:53:00
---

我的apache安装好后默认的网页目录为：/var/www，我现在想要修改CGI目录到/var/www/cgi-bin/下，
首先，修改文件：/etc/apache2/sites-available/default
将其中的ScriptAlias /cgi-bin/段修改为：
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
<Directory “/var/www/cgi-bin/”>
AllowOverride None
Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
Order allow,deny
Allow from all
</Directory>
然后，重启apache就可以了：
sudo /etc/init.d/apache2 restart