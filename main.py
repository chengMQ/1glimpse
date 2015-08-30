import re
from multiprocessing.dummy import Pool
import datetime
import time
import webbrowser
import rules
from inspect import getmembers


def run(f):
    result = f()
    aa = list2html(result)
    print(result[0],'finished...')
    return aa


def list2html(table_html):
    website, list1, num = table_html
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


if __name__ == '__main__':
    # print(vars())
    aa = dict([i for i in getmembers(rules) if i[0].endswith('pyld')])
    func_list = sorted(aa.keys())
    choose_func = [aa[i] for i in func_list]
    pp = Pool(20)
    ss = pp.map(run, choose_func)
    pp.close()
    pp.join()
    with open('./pages/%s.html'%datetime.datetime.now().strftime('%Y-%m-%d'), 'w', encoding='utf-8') as f:
        
        scode='<meta charset="utf-8"><style> body{background-color:#999999} </style><style>A {text-decoration: NONE} </style>' + '<br>'.join(ss)
        f.write(scode)
        webbrowser.open('/pages/%s.html'%datetime.datetime.now().strftime('%Y-%m-%d'))
