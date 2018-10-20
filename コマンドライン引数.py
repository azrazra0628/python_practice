###コマンドライン引数###
#プログラムの実行のたびにプログラムが処理するデータを変更したいときに使用する
##sysモジュールを使用する##

import sys
total = 0
for price in sys.argv[1:]:
    total += int(price)

print('合計', total, '円')




