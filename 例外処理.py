###例外###
##例外はプログラムの実行中に起こるエラーのこと エラーが発生するとメッセージを表示して終了suru
##例外処理を記述しておけば、エラー発生後も実行を継続する

#try:
#   処理A
#except 例外名:
#   処理B

#複数の例外処理がある場合には多段で記載するか下記の通り記載
#except (例外名,　例外名, …):

number = ['1','2', 'three', '4']
sum = 0 
for n in number:
    sum += int(n)

print(sum)

#下記のエラーメッセージが出現
#ValueError: invalid literal for int() with base 10: 'three'

number = ['1','2', 'three', '4']
sum = 0 
for n in number:
    try:
        sum += int(n)
    except ValueError:
        pass

print(sum)

##else節やfinally節も記述可能
