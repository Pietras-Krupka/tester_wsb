import os
import datetime
import time
import shutil

print(os.getcwd())
if os.path.exists('.tester-wsb'):
    shutil.rmtree('tester-wsb')

os.chdir('C:\\Users\\User\\Desktop\\tester-wsb')
os.chdir('C:\\Users\\User\\Desktop\\tester-wsb\\test11')
os.mkdir('test11')

for i in range(10):
    time_now = datetime.datetime.now()
    time_now_f = time_now.strftime('%H%M%S')
    f = open(f'report {time_now_f}.txt', 'w')
    f.close()
    time.sleep(2)


