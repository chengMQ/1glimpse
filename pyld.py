from inspect import getmembers
import rules


aa=dict([i for i in getmembers(rules) if i[0].endswith('pyld')])
aa.keys()

print(aa['tuicool_pyld']())