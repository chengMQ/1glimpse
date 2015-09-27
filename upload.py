import os
import time
# os.chdir('./ClericPy.github.io')
os.system('python main.py')
os.system(r'git add * -f')
os.system(r'git commit -m "常规更新"')
os.system(r'git push origin master')
# os.system('pause')
for i in range(1,4):
    print(4-i)
    time.sleep(1)