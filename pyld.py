import glob
import re
import os


def refresh_index():
    def list2index(each_item):
        return '<li><a href="/pages/%s.html">%s</a></li>' % (each_item, each_item)
    list1 = ''.join([list2index(i.replace('.html', '')) for i in sorted(
            os.listdir('.\\pages'), reverse=True) if i.endswith('html')])
    str1 = '<!--网址列表--start--><ul>%s</ul><!--网址列表--end-->' % list1
    # print(str1)
    with open('index.html', 'r', encoding='utf-8') as f:
        scode = f.read()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(
            re.sub('<!--网址列表--start-->[\s\S]+?<!--网址列表--end-->', str1, scode))
refresh_index()
