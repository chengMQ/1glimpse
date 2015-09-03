import re
from multiprocessing.dummy import Pool
import datetime
import time
import os
import rules
from inspect import getmembers


this_day = datetime.datetime.now().strftime('%Y-%m-%d')
this_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def list2html(table_html):
    # 具体的数据转HTML过程
    website, list1, num, iscover = table_html
    head = "<table cellspacing=5 cellpadding=7  width='100%' align='center'><tbody><p><h2 align='center'>{}</h2></p>".format(
        website)
    table1 = ''
    for i, each in enumerate(list1):
        cover, title, url, desc = each
        if iscover:
            cover = '<img   width="100%" height=200  src="{}"  />'.format(
                cover)
        else:
            cover = ''
        n = i + 1
        if (n - 1) % num == 0:
            table1 += '<tr style="width:100%;">'
        table1 += '<td style="background:#eeeeee" VALIGN=TOP width="{width1}%"><a  href="{url}" target="_blank" style="font-size:18px;">{cover}<p><span style="color:#000000;"><strong>{title}</strong></span></p></a><span style="font-size:16px;">{desc}</span></td>'.format(
            cover=cover, url=url, title=title, desc=desc, width1=100 / num)
        if n % num == 0 or n == len(list1):
            table1 += '</tr>'
    return head + table1 + '</tbody></table>'


def withpics_to_file(ss):
    # 传入feed的列表，输出为文件
    ss = [list2html(i) for i in ss]
    with open('./pages/%s[cover-yes].html' % this_day, 'w', encoding='utf-8') as f:

        scode = '<meta charset="utf-8"><style> body{background-color:#999999} </style><style>A {text-decoration: NONE} </style><strong>当前订阅列表：</strong>%s<hr>' % titles + '<br>'.join(
            ss) + '<hr>采集时间：%s' % this_time
        f.write(scode)


def withoutpic_to_file(ss):
    ss = [list2html(i) for i in ss]
    with open('./pages/%s[cover-no].html' % this_day, 'w', encoding='utf-8') as f:

        scode = '<meta charset="utf-8"><style> body{background-color:#999999} </style><style>A {text-decoration: NONE} </style><strong>当前订阅列表：</strong>%s<hr>' % titles + '<br>'.join(
            ss) + '<hr>采集时间：%s' % this_time
        f.write(scode)


def refresh_index():
    # 刷新index.html
    def list2index(each_item):
        return '<li><a href="/pages/%s.html">%s</a></li>' % (each_item, each_item +'blabla'+ datetime.datetime.now().strftime('%H:%M:%S'))
    list0 = [list2index(i.replace('.html', '')) for i in sorted(
        os.listdir('.\\pages'), reverse=True) if i.endswith('html')]
    list1=''.join([i.replace('[cover-yes]blabla',' ') for i in list0 if '[cover-yes]' in i])
    list2=''.join([i.replace('[cover-no]blabla',' ') for i in list0 if '[cover-no]' in i])
    str1 = '<!--网址列表--start--><table style="width:80%;" border="0" cellpadding="2" cellspacing="0" align="center"><tbody><tr><td><strong>有图版</strong></td><td><strong>无图版</strong></td></tr><tr><td>{}</td><td>{}</td></tr></tbody></table><!--网址列表--end-->'.format(list1,list2)
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
    titles = '、'.join(['[%s]' % i[0] for i in ss])
    withpics_to_file(ss)
    withoutpic_to_file(ss)
    refresh_index()
