#!python3

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
    head = "<div id='{}'><table style='table-layout:fixed;' cellspacing=2 cellpadding=5 width='100%' align='center'><tbody><p><h2 style='font-size:38px;' align='center'>{}&nbsp;[ {} 篇 ]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='#headline' style='font-size:38px;'>↗</a></h2></p><hr>blablablabla</tbody></table></div>".format(
        re.sub('<.*?>', '', website), website, len(list1))
    if not list1:
        return head.replace('blablablabla', '<div align="center">暂无新数据</div>')
    table1 = ''
    for i, each in enumerate(list1):
        cover, title, url, sums = each
        if not cover:
            cover = 'error'
        if iscover:
            cover = '<img width=100%  src="{}" onerror="this.src=\'./empty.png\'" />'.format(
                cover)
        else:
            cover = ''
        n = i + 1
        if (n - 1) % num == 0:
            table1 += '<tr style="width:100%;">'
        table1 += '<td valign="top" width="{width1}%"><a  href="{url}" target="_blank" style="font-size:18px;">{cover}<p><span style="color:#000000;"><strong>{title}</strong></span></p></a><span style="font-size:16px;">{sums}</span></td>'.format(
            cover=cover, url=url, title=title, sums=sums, width1=100 / num)
        if n % num == 0:
            table1 += '</tr>'
        if n == len(list1) and num > (n % num):
            table1 = table1 + '<td width="16.666666666666668%" valign="TOP" ></td>' * \
                (num - n % num) + '</tr>'
    return head.replace('blablablabla', table1)


def withpics_to_file(ss):
    # 传入多个feed的列表，输出为文件
    ss = [list2html(i) for i in ss]
    with open('./pages/%s[cover-yes].html' % this_day, 'w', encoding='utf-8') as f:

        scode = r'''<meta charset="utf-8"><meta name="viewport" content="target-densitydpi=device-dpi" /><title>一瞥日报 {}</title><script type="text/javascript">document.write('<style>body{{background-image:url("./bgs/bg' + Math.round( Math.random() * 14 ) + '.jpg");background-size: 100% 100%;}}</style>');</script><style>A {{text-decoration: NONE}} </style><style>span{{word-break:normal; width:auto; display:block;word-wrap : break-word ;overflow: hidden ;}} </style><p id="headline" style="font-size:18px;"><strong>当前订阅列表：</strong>{}</p><div align="right">—— 更新时间：{} </div><hr>'''.format(this_time, titles2, this_time) + '<hr>'.join(
            ss) + '<div align="center"><a style="font-size:18px;" href="../index.html">回到首页</a></div>'
        f.write(scode)
    # for mobile
    with open('./pages/%s[cover-yes-mobile].html' % this_day, 'w', encoding='utf-8') as f:
        scode = re.sub('<td.*?>|</td>', '<hr>', scode).replace('font-size:16px;','font-size:46px;').replace('font-size:18px;', 'font-size:58px;')  # .replace('<fengebiaoji><fengebiaoji>', '<hr>')
        scode=re.sub('(<hr>){2,}', '<hr>', scode)
        f.write(scode)


def withoutpic_to_file(ss):
    for i in ss:
        i[-1] = 0
    ss = [list2html(i) for i in ss]
    with open('./pages/%s[cover-no].html' % this_day, 'w', encoding='utf-8') as f:

        scode = '<meta charset="utf-8"><meta name="viewport" content="target-densitydpi=device-dpi" /><title>一瞥日报 %s</title><style>body{background-color:#cccccc} </style><style> td{background-image: url("");background-size: 100% 100%;} </style><style>A {text-decoration: NONE} </style><p id="headline" style="font-size:18px;"><strong>当前订阅列表：</strong>%s</p><div align="right">—— 更新时间：%s </div><hr>' % (this_time, titles2, this_time) + '<hr>'.join(
            ss) + '<div align="center"><a style="font-size:18px;" href="../index.html">回到首页</a></div>'
        f.write(scode)
    # for mobile
    with open('./pages/%s[cover-no-mobile].html' % this_day, 'w', encoding='utf-8') as f:
        scode = re.sub('<td.*?>|</td>|<img.*?>|<video.*?</video>', '', scode).replace(
            'font-size:16px;', 'font-size:46px;').replace('font-size:18px;', 'font-size:58px;')
        f.write(scode)


def refresh_index():
    # 刷新index.html
    def list2index(each_item):
        return '<li><a target="_blank" style="font-size:18px;" href="./pages/%s.html">%s</a></li>' % (each_item, each_item + 'blabla')
    list0 = [list2index(i.replace('.html', '')) for i in sorted(
        os.listdir('./pages'), reverse=True) if i.endswith('html')]
    list1 = ''.join([i.replace('[cover-yes]blabla', '')
                     for i in list0 if '[cover-yes]' in i])
    list2 = ''.join([i.replace('[cover-no]blabla', '')
                     for i in list0 if '[cover-no]' in i])
    list3 = ''.join([i.replace('[cover-yes-mobile]blabla', '')
                     for i in list0 if '[cover-yes-mobile]' in i])
    list4 = ''.join([i.replace('[cover-no-mobile]blabla', '')
                     for i in list0 if '[cover-no-mobile]' in i])
    str1 = '<!--网址列表--start--><p style="font-size:18px;">最后更新：{}</p><p style="font-size:18px;"><strong>当前订阅列表：</strong>{}</p><div align="center"><table style="width:100%;" border="0" cellpadding="2" cellspacing="0" align="center"><tbody><tr><td width="9999"><strong style="font-size:20px;">PC-有图版</strong></td><td width="25%"><strong style="font-size:20px;">手机-有图版</strong></td><td width="25%"><strong style="font-size:20px;">PC-无图版</strong></td><td width="25%"><strong style="font-size:20px;">手机-无图版</strong></td></tr><tr><td><ul>{}</ul></td><td><ul>{}</ul></td><td><ul>{}</ul></td><td><ul>{}</ul></td></tr></tbody></table></div><!--网址列表--end-->'.format(
        this_time, titles, list1, list3, list2, list4)
    # print(str1)
    with open('index.html', 'r', encoding='utf-8') as f:
        scode = f.read()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(
            re.sub('<!--网址列表--start-->[\s\S]+?<!--网址列表--end-->', str1, scode))


def refresh_old():
    # 刷新index.html
    def list2index(each_item):
        return '<li><a target="_blank" style="font-size:18px;" href="./pages/old/%s.html">%s</a></li>' % (each_item, each_item + 'blabla')
    list0 = [list2index(i.replace('.html', '')) for i in sorted(
        os.listdir('./pages/old'), reverse=True) if i.endswith('html')]
    list1 = ''.join([i.replace('[cover-yes]blabla', '')
                     for i in list0 if '[cover-yes]' in i])
    list2 = ''.join([i.replace('[cover-no]blabla', '')
                     for i in list0 if '[cover-no]' in i])
    list3 = ''.join([i.replace('[cover-yes-mobile]blabla', '')
                     for i in list0 if '[cover-yes-mobile]' in i])
    list4 = ''.join([i.replace('[cover-no-mobile]blabla', '')
                     for i in list0 if '[cover-no-mobile]' in i])
    str1 = '<meta charset="utf-8"><!--网址列表--start--><div align="center"><table style="width:100%;" border="0" cellpadding="2" cellspacing="0" align="center"><tbody><tr><td valign="top" width="9999"><strong style="font-size:20px;">PC-有图版</strong></td><td valign="top" width="25%"><strong style="font-size:20px;">手机-有图版</strong></td><td valign="top" width="25%"><strong style="font-size:20px;">PC-无图版</strong></td><td valign="top" width="25%"><strong style="font-size:20px;">手机-无图版</strong></td></tr><tr><td valign="top"><ul>{}</ul></td><td valign="top"><ul>{}</ul></td><td valign="top"><ul>{}</ul></td><td valign="top"><ul>{}</ul></td></tr></tbody></table></div><!--网址列表--end-->'.format(
        list1, list3, list2, list4)
    # print(str1)
    with open('old.html', 'w', encoding='utf-8') as f:
        f.write(str1)

if __name__ == '__main__':
    func_names = dict(
        [i for i in getmembers(rules) if i[0].startswith('pyld')])
    func_list = sorted(func_names.keys())
    choose_func = [func_names[i] for i in func_list]
    from torequests import pPool
    pp = pPool(40)
    ss = pp.map1(lambda x: x(), choose_func)
    # pp.close()
    # pp.join()
    titles = ' | '.join([i[0] for i in ss])
    titles2 = ' | '.join([re.sub('target="_blank" href=".*?"',
                                 'href="#%s"' % re.sub('<.*?>', '', i[0]), i[0]) for i in ss])
    withpics_to_file(ss)
    withoutpic_to_file(ss)
    refresh_index()
    refresh_old()
    print('===============All missions completed===============')
