import re
from multiprocessing.dummy import Pool
import datetime
import time
import os
import rules
from inspect import getmembers


this_day = datetime.datetime.now().strftime('%Y-%m-%d')

# 有图标准版。


def run_havepic(result):
    # 输入指定格式LIST，最终转为HTML代码片段
    aa = list2html(result)
    return aa


def list2html(table_html):
    # 转换HTML代码片段前判定是有cover还是无cover
    if table_html[-1] == 0:
        return image_no(table_html)
    else:
        return image_yes(table_html)


def image_yes(table_html):
    # 具体的转有图版HTML过程
    website, list1, num, iscover = table_html
    head = "<table cellspacing=5 cellpadding=7  width='100%' align='center'><tbody><p><h2 align='center'>{}</h2></p>".format(
        website)
    table1 = ''
    for i, each in enumerate(list1):
        cover, title, url, desc = each
        n = i + 1
        if (n - 1) % num == 0:
            table1 += '<tr style="width:100%;">'
        table1 += '<td style="background:#eeeeee" VALIGN=TOP width="{width1}%"><a  href="{url}" target="_blank" style="font-size:18px;"><img   width="100%" height=200  src="{cover}" alt="" /><p><span style="color:#000000;"><strong>{title}</strong></span></p></a><span style="font-size:16px;">{desc}</span></td>'.format(
            cover=cover, url=url, title=title, desc=desc, width1=100 / num)
        if n % num == 0 or n == len(list1):
            table1 += '</tr>'
    return head + table1 + '</tbody></table>'


def withpics_to_file(ss):
    # 传入列表的列表，输出为文件
    ss = [run_havepic(i) for i in ss]
    with open('./pages/%s.html' % this_day, 'w', encoding='utf-8') as f:

        scode = '<meta charset="utf-8"><style> body{background-color:#999999} </style><style>A {text-decoration: NONE} </style><strong>当前订阅列表：</strong>%s<hr>采集时间：%s<hr>'%(titles,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '<br>'.join(
            ss)
        f.write(scode)

# 以下为无图版


def run_nopic(result):
    # 将list转为无图table HTML代码
    aa = list2html_no_image(result)
    return aa


def list2html_no_image(table_html):
    # 转换时不管末尾是不是0，都变成0
    table_html[-1] = 0
    return list2html(table_html)


def image_no(table_html):
    # 具体转无图版HTML
    website, list1, num, iscover = table_html
    head = "<table cellspacing=5 cellpadding=7  width='100%' align='center'><tbody><p><h2 align='center'>{}</h2></p>".format(
        website)
    table1 = ''
    for i, each in enumerate(list1):
        cover, title, url, desc = each
        n = i + 1
        if (n - 1) % num == 0:
            table1 += '<tr style="width:100%;">'
        table1 += '<td style="background:#eeeeee" VALIGN=TOP width="{width1}%"><a  href="{url}" target="_blank" style="font-size:18px;"><p><span style="color:#000000;"><strong>{title}</strong></span></p></a><span style="font-size:16px;">{desc}</span></td>'.format(
            url=url, title=title, desc=desc, width1=100 / num)
        if n % num == 0 or n == len(list1):
            table1 += '</tr>'
    return head + table1 + '</tbody></table>'


def withoutpic_to_file(ss):
    ss = [run_nopic(i) for i in ss]
    with open('./pages/%s[no_cover].html' % this_day, 'w', encoding='utf-8') as f:

        scode = '<meta charset="utf-8"><style> body{background-color:#999999} </style><style>A {text-decoration: NONE} </style><strong>当前订阅列表：</strong>%s<hr>采集时间：%s<hr>'%(titles,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '<br>'.join(
            ss)
        f.write(scode)


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

if __name__ == '__main__':
    func_names = dict([i for i in getmembers(rules) if i[0].endswith('pyld')])
    func_list = sorted(func_names.keys())
    choose_func = [func_names[i] for i in func_list]
    pp = Pool(20)
    ss = pp.map(lambda x: x(), choose_func)
    pp.close()
    pp.join()
    titles='、'.join(['[%s]'%i[0] for i in ss])
    withpics_to_file(ss)
    withoutpic_to_file(ss)
    refresh_index()
