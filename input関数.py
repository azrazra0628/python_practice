###input関数###
##キーボードから1行の入力を受け取り、末尾の改行を除いて文字列として返す
# input()

##合計300円以上になるまで合計を繰り返し300円を超えたらプログラムを終了する
total = 0 
while total <= 300:
    price = input()
    total += int(price)
    print('合計', total, '円')

# input関数は入力されたデータを文字列として扱うため、
# int関数やfloat関数を使用する

eigo = int(input('英語の点数を入力してください>'))
suugaku = int(input('数学の点数を入力してください>'))
total = eigo + suugaku
avg = total / 2
print('英語の得点:', eigo, sep=' ')
print('数学の得点:', suugaku, sep=' ')
print('合　　　計:',total, sep=' ')
print('平　　　均:', avg, sep=' ')


# 小数点以下の数字を扱う場合には、float関数を使用する
height = float(input('身長をm単位で入力してください>'))
weight = float(input('体重をkg単位で入力してください>'))

BMI = weight / height**2

print('BMI = ',BMI, sep=' ')
if BMI < 18.5:
    print('やせ')
elif BMI >= 18.5 and BMI < 25:
    print('標準')
elif BMI >= 25 and BMI < 30:
    print('肥満')
elif BMI >= 30:
    print('高肥満')

    