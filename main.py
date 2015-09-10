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
    head = "<div sitename='{}'><table style='table-layout:fixed;' cellspacing=5 cellpadding=7 width='100%' align='center'><tbody><p><h2 align='center'>{}</h2></p><hr>blablablabla</tbody></table></div>".format(
        website, website)
    if not list1:
        return head.replace('blablablabla', '<div align="center">暂无新数据</div>')
    table1 = ''
    for i, each in enumerate(list1):
        cover, title, url, desc = each
        if not cover:
            cover='error'
        if iscover:
            cover = '<img   style="width:100%;" height=200  src="{}" onerror="this.src=\'empty.jpg\'" />'.format(
                cover)
        else:
            cover = ''
        n = i + 1
        if (n - 1) % num == 0:
            table1 += '<tr style="width:100%;">'
        table1 += '<td style="background:#cccccc" VALIGN=TOP width="{width1}%"><a  href="{url}" target="_blank" style="font-size:18px;">{cover}<p><span style="color:#000000;"><strong>{title}</strong></span></p></a><span style="font-size:16px;">{desc}</span></td>'.format(
            cover=cover, url=url, title=title, desc=desc, width1=100 / num)
        if n % num == 0 or n == len(list1):
            table1 += '</tr>'
    return head.replace('blablablabla', table1)


def withpics_to_file(ss):
    # 传入多个feed的列表，输出为文件
    ss = [list2html(i) for i in ss]
    with open('./pages/%s[cover-yes].html' % this_day, 'w', encoding='utf-8') as f:

        scode = '<meta charset="utf-8"><meta name=”viewport” content=”target-densitydpi=device-dpi” /><title>一瞥日报 %s</title><style> body{background-color:#a4a4a4} </style><style>A {text-decoration: NONE} </style><p style="font-size:18px;"><strong>当前订阅列表：</strong>%s</p><div align="right">—— 更新时间：%s </div><hr>' % (this_time, titles, this_time) + '<hr>'.join(
            ss)
        f.write(scode)


def withoutpic_to_file(ss):
    for i in ss:
        i[-1] = 0
    ss = [list2html(i) for i in ss]
    with open('./pages/%s[cover-no].html' % this_day, 'w', encoding='utf-8') as f:

        scode = '<meta charset="utf-8"><meta name=”viewport” content=”target-densitydpi=device-dpi” /><title>一瞥日报 %s</title><style> body{background-color:#a4a4a4} </style><style>A {text-decoration: NONE} </style><p style="font-size:18px;"><strong>当前订阅列表：</strong>%s</p><div align="right">—— 更新时间：%s </div><hr>' % (this_time, titles, this_time) + '<hr>'.join(
            ss)
        f.write(scode)


def refresh_index():
    # 刷新index.html
    def list2index(each_item):
        return '<li><a target="_blank" style="font-size:18px;" href="./pages/%s.html">%s</a></li>' % (each_item, each_item + 'blabla')
    list0 = [list2index(i.replace('.html', '')) for i in sorted(
        os.listdir('.\\pages'), reverse=True) if i.endswith('html')]
    list1 = ''.join([i.replace('[cover-yes]blabla', '')
                     for i in list0 if '[cover-yes]' in i])
    list2 = ''.join([i.replace('[cover-no]blabla', '')
                     for i in list0 if '[cover-no]' in i])
    str1 = '<!--网址列表--start--><p style="font-size:18px;">最后更新：{}</p><p style="font-size:18px;"><strong>当前订阅列表：</strong>{}</p><div align="center"><table style="width:100%;" border="0" cellpadding="2" cellspacing="0" align="center"><tbody><tr><td width="9999"><strong style="font-size:35px;">有图版</strong></td><td width="50%"><strong style="font-size:35px;">无图版</strong></td></tr><tr><td><ul>{}</ul></td><td><ul>{}</ul></td></tr></tbody></table></div><!--网址列表--end-->'.format(
        this_time, titles, list1, list2)
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
    titles = ' | '.join([i[0] for i in ss])
    withpics_to_file(ss)
    withoutpic_to_file(ss)
    refresh_index()
