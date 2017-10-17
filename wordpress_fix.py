import os
import shutil

posts_path = '/home/qiang/posts'
bad_posts_path = '/home/qiang/posts_bad'
good_posts_path = '/home/qiang/posts_ok'
target_path = '/home/qiang/hackqiang.github.io/source/_posts'

def check_post():
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


def fix_categories():
    os.system('hexo clean')
    for root, dirs, files in os.walk(good_posts_path):
        for file in files:
            source = os.path.join(good_posts_path, file)
            target = os.path.join(target_path, file)
            with open(source, 'rb') as inf:
                with open(target, 'wb') as outf:
                    flag = 'w'
                    for line  in inf.readlines():
                        if flag == 'w':
                            outf.write(line)
                        if line.startswith('categories:'):
                            flag = 'cate'
                            continue
                        if flag == 'cate':
                            outf.write(line)
                            flag = 'skip'
                            continue
                        if flag == 'skip':
                            if line.startswith('date: '):
                                flag = 'w'
                                outf.write(line)
                        
fix_categories()
