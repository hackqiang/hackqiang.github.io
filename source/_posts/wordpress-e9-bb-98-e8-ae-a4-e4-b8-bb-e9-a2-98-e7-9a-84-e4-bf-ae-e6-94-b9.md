---
title: WordPress默认主题的修改
tags:
  - wordpress
  - 主题
id: 1687
comment: false
categories:
  - 乱七八糟
date: 2009-07-18 20:34:00
---

装上WordPress后就开始寻找主题,以前用Z-BLOG的时候就羡慕WordPress的主题,可现在用上了WordPress后却发现WordPress的主题没想象的好.找来找去也没发现中意的.最后还是觉得默认主题看着舒服.
但是默认主题主要有两个缺点.
1.主页上没有自动显示摘要,导致了页面太长.
2.分页不实用（这貌似是通病）.
3.没有留言（这貌似也是通病）.
先解决分页问题,下载wp-pageavi插件,安装.然后打开主题的index.php文件.
把代码:
?
View Code
PHP
1
2
3
4
<
div
class
=
"navigation"
>
<
div
class
=
"alignleft"
><!--
p next_posts_link
(
__
(
'&laquo; Older Entries'
,
'kubrick'
)
)
;--></
div
>
<
div
class
=
"alignright"
><!--
p previous_posts_link
(
__
(
'Newer Entries &raquo;'
,
'kubrick'
)
)
;--></
div
>
</
div
>
修改为:
?
View Code
PHP
1
<
div
><!--
p
if
(
function_exists
(
'qiang_pagenavi'
)
)
{
qiang_pagenavi
(
)
;
}
--></
div
>
这样分页就解决了,如果想要居中显示,在div里加上“align=”center””属性.
首页摘要显示的修改：
打开index.php。
找到代码：
?
View Code
PHP
1
注意the_content()函数中可能会有参数，不过可以无视它。
修改为：
?
View Code
PHP
1
最后再加上“read more”的按钮：
?
View Code
PHP
1
2
3
<
div
class
=
"details"
>
<
div
class
=
"inside"
><
a href
=
"&lt;?php the_permalink() ?&gt;"
>
Read More »
</
a
></
div
>
</
div
>
这样，不能显示摘要的问题也解决了。
最后解决留言板的问题。
先复制一份single.php，改名为guestbook.php
在guestbook.php的顶部加上下面的代码:
?
View Code
PHP
1
最后，新建一个页面，在页面编辑器的底部，找到页面模板这个选项，从中选择刚才建立的Guestbook,保存就可以了.
但是问题还没完。还要美化一下。
在guestbook.php中把下面的代码删掉：
?
View Code
PHP
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
<
div
>
id
=
"post-"
&
gt
;
<
div
class
=
"entry"
>
' . __('
Read the rest of this entry »
', '
kubrick
') . '
'); ?&gt;
'
<
strong
>
' . __('
Pages
:
', '
kubrick
') . '
</
strong
>
', '
after
' =&gt; '
', '
next_or_number
' =&gt; '
number
')); ?&gt;

trackback from your own site.'
,
'kubrick'
)
,
trackback_url
(
false
)
)
;
?
&
gt
;</
div
>
</
div
>
为留言，也就是评论分页：下载wp-commentnavi插件，用法和wp-pagenavi差不多，这就不多说了。
用同样的方法可以修改search.php,archivers.php等等。