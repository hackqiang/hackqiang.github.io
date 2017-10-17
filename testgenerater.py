import os
import shutil

posts_path = '/home/qiang/posts'
bad_posts_path = '/home/qiang/posts_bad'
good_posts_path = '/home/qiang/posts_ok'
target_path = '/home/qiang/hackqiang.github.io/source/_posts'

for root, dirs, files in os.walk(posts_path):
    for file in files:
        source = os.path.join(posts_path, file)
        target = os.path.join(target_path, file)
        good = os.path.join(good_posts_path, file)
        bad = os.path.join(bad_posts_path, file)
        
        print source, target
        if file.endswith('.md'):
            shutil.copy(source, target)
            os.system('hexo clean')
            if not os.system('hexo g'):
                # success
                print 'OK'
                shutil.move(target, good)
            else:
                print 'bad'
                shutil.move(target, bad)

