# ■問題３－２（▲参考：例題３－３）
# 入力した数値を使った計算をする．inputを使ってキーボードから２つの整数を入力して
# その合計を表示する，というプログラムを作りたい．
# プログラムの基本的な構造は以下のようになる．
# 1. 整数変数を2つ宣言する
# 2. 整数を2つ入力し，宣言した変数に代入する
# 3. 2つの整数の和を表示する

# （１）上の構造どおりのプログラムを作れ
# （２）整数３つを入力して，その合計を表示するようにせよ
# （３）小数２つを入力して，その合計を表示するようにせよ
# （４）整数２つを入力して，その積を表示するようにせよ

# (1)
# x = int(input('please enter an interger >'))
# y = int(input('please enter an interger again >'))

# sum = x + y
# print(str(x)+'+'+str(y)+'='+str(sum))

# (2)
# x = int(input('please enter an interger >'))
# y = int(input('please enter an interger again >'))
# z = int(input('please enter an interger fainal >'))
# total = x + y + z
# print(str(x)+'+'+str(y)+'+'+str(z)+'='+str(total))

# # (3)
# # x = float(input('please enter an interger >'))
# # y = float(input('please enter an interger again >'))

# # sum = x + y
# # print(str(x)+'+'+str(y)+'='+str(sum))

# (4)
# x = int(input('please enter an interger >'))
# y = int(input('please enter an interger again >'))
# seki = x * y
# print(str(x)+'×'+str(y)+'='+str(seki))


# ●問題４－１
# （1）　入力した数が0ならzeroと表示するプログラムを作りましょう．
# （2）　入力した数が100以上ならOKと表示するプログラムを作りましょう．
# （3）　入力した数が0以上ならpositive，
# そうでなければnegativeと表示するプログラムを作りましょう．
# （4）　入力した2つの数が等しいならequalと表示するプログラムを作りましょう．

# (1)
# x = int(input('please enter an interger > '))

# if x == 0 :
#     print('zero')

# (2)
# x = int(input('please enter an interger > '))

# if x > 100 :
#     print('OK')


# (3)
# x = int(input('please enter an interger > '))
# if x > 0 :
#     print('positive')
# else :
#     print('negative')


# (4)
# x = int(input('please enter an interger > '))
# y = int(input('please enter an interger > '))

# if x == y :
#     print('equal')




# ■問題５－１３（▲参考：問題５－９）
# ２つの整数a,bをキーボードから入力し，
# 縦がa文字，横がb文字の*で出来た四角を描くプログラムを作りなさい．
# たとえば，a=2,b=5なら，
# *****
# *****
# と表示される．
# （１）forを１回だけ使用して作れ
# （２）２重のforループを使用して作れ　【やや難】

# a = int(input('please enter an interger > '))
# b = int(input('please enter an interger > '))

# (1)
# # for i in range(1,b+1):
# #     print('*'*a,sep='')

# (2)
# for i in range(1,b+1):
#     for h in range(1,a+1):
#         print('*',end='')
#     print()    




# ●問題６－２
# (1)　「入力した10個の数の最小」を表示するプログラムを作りなさい．
# (2)　「10以下の数の中での最大」を表示するようなプログラムを作りなさい．
# ただし，10以下の数は必ず1つは入力される，とみなして良いとします．

# lst = []

# for i in range(0,10):
#     n = int(input('please enter an interger > '))
#     if n < 10 :
#         lst.append(n)
# print('10以下の数字で最大の値は'+str(max(lst))+'です')



# ●問題６－５
# 数を10個入力してその合計を表示するプログラムを作りなさい．

total = 0 
lst = []
for i in range(10):
    n =int(input('please enter an interger > '))
    total += n
    lst.append(n)
print('合計値は'+str(total)+'です')

print('+'.join(str(lst)))