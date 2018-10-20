##実行時間の計測##
s = ''
for i in range(1000):
    s += '根菜町1町目2番地 人参¥n'

s = '根菜町1町目2番地 人参¥n' * 1000

##  timeモジュールを使って時間を計測する

import time

old = time.time()
s = ''
for i in range(1000000):
    s += '根菜町1町目2番地 人参¥n'

print(time.time()-old, '秒')

import time

old = time.time()
s = '根菜町1町目2番地 人参¥n' * 1000000
print(time.time()-old, '秒')
