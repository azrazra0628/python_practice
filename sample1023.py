# ■問題３－５（▲参考：問題３－２）
# 整数を4つ入力して，それらの合計を表示するプログラムを作りなさい．
# 例えば，プログラムを実行して，10,20,33,44を入力すると，
# その合計の107が表示されます．

# total = 0
# for i in range(4):
#     n = int(input('please enter an integer > '))
#     total += n
# print('合計は'+str(total)+'です')


# ●問題４－６
# 　キーボードから入力した数が10以上20以下であればOKと表示するプログラムを作りなさい．
# n = int(input('please enter an integer > '))
# if 10 < n < 20 :
#     print('OK')



# ■問題５－７（▲参考：例題５－９）
# （１）forの2重ループを使って，九九の表を書くプログラムを作成せよ．
# 　　　ただし，表の罫線を書くのは大変なので，中身の数字だけを書く．
# （２）9×9 の足し算の答えを表にせよ．
# （３）12×12 の掛け算の答えを表にせよ．




# ■問題５－１２（for，whileの使い分け）（▲参考：問題５－５）
# ２つの整数aとbをキーボードから入力させ，
# a以上b以下の整数をすべて表示させるプログラムを作れ
# （１）for文を使って作れ（whileは使わない）
# （２）while文を使って作れ（forは使わない）

# a = int(input('please enter an integer > '))
# b = int(input('please enter an integer > '))

# for i in range(b-a-1):
#     a += 1
#     print(str(a),end=' ')

a = int(input('please enter an integer > '))
b = int(input('please enter an integer > '))

while b-1 > a :
    a += 1
    print(str(a),end=' ')



# ●問題６－７
# 入力した10個の数の中に1と0，どちらが多いかを判定するプログラムを作りなさい．
# count0 = 0
# count1 = 0
# for i in range(10):
#     n = int(input('please enter an integer > '))
#     if n == 0 :
#         count0 += 1
#     elif n == 1 :
#         count1 += 1
# if count0 > count1 :
#     print('あなたは０を1より'+str(count0-count1)+'回多く選択しました')
# elif count1 > count0 :
#     print('あなたは1を0より'+str(count1-count0)+'回多く選択しました')
# else :
#     print('同点です')




# 　1以上の整数を入力し、その数までのべき乗を計算するプログラムを作成せよ。
# 実行結果
# 数> 25
# 25! = 15511210043330985984000000



# n = int(input('数> '))
# total = 1
# s = 0
# for i in range(n):
#     s += 1
#     total *= s
# print(str(n)+'! = '+str(total))



# 　数を次々と入力し、負の数が入力されるまで続け、負の数が入力されたら、それまでの数の合計と平均を求めるプログラムを書きなさい。
# 実行結果
# データ入力(負の数で終了)> 10
# データ入力(負の数で終了)> 20
# データ入力(負の数で終了)> 30
# データ入力(負の数で終了)> 40
# データ入力(負の数で終了)> 50
# データ入力(負の数で終了)> -1
# データ数: 5 合計: 150 平均: 30.0

# n = int(input('please enter an integer > '))
# lst =[]
# count = 0
# while n > 0 :
#     count += 1
#     lst.append(n)
#     n = int(input('please enter an integer > '))
# total = sum(lst)
# avg = total / count
# print('データ数: '+str(count)+' 合計: '+str(total)+' 平均: '+str(avg))
