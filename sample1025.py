# ●問題４－２
# 例題４－３のサンプルコードを用いて，
# （1）　入力した数が10か10より大きいか10未満かを判定するプログラムを作りましょう．
# （2）　入力した数が1なら1，2なら2，それ以外ならetcと表示させましょう．
# （3）　最初のifの条件式を(x<0)とすると，実行結果は元のプログラムと変わってしまいます．
#      そこで，この条件式以外の部分を修正して，
# 元のプログラムと同じ実行結果を出すプログラムに修正しましょう．
(1)

# n = int(input('please enter an integer > '))
# if n == 10:
#     print(str(n)+'は10です')
# elif n > 10 :
#     print(str(n)+'は10より大きいです')
# elif n < 10 :
#     print(str(n)+'は10より小さいです')


(2)
# if n == 1:
#     print(n)
# elif n == 2 :
#     print(n)
# else :
#     print('etc')


# ●問題４－８
# キーボードから数を入力し，その数が正ならその数を表示．
# そうでなければ，もうひとつ数を入力し，最初の数との積を表示するプログラムを作りなさい．
# 表示結果例
# x = :-3
# y = :2
# seki  -6


# x = int(input('please enter an integer > '))

# if x > 0 :
#     print('x', '=', ':', str(x))
# elif x < 0 :
#     y = int(input('please enter an integer > '))
#     print('y','=','=',str(y))
#     print('seki','=', ':',str(x*y))


# ■問題５－５（for文）（▲参考：例題５－７）
# （１）1から10までの整数を表示するプログラムを作りなさい．
# （２）1から20までの整数を表示するように書き換えよ．
# （３）-10から10までの整数を表示するように書き換えよ．
# （４）2,4,6,8,10 を表示するように書き換えよ．
# 　　（ヒント：iを2つずつ大きくすると…）
# （５）while i<=10: を while i<10: とするとどうなるか，試せ．
# 　　　また，どうしてそうなるのか，考察せよ．
# （１）問題５－４の各問をforループを用いて書き換えよ
# （２）10から1までの整数を大きい順で（10,9,8,… ）表示せよ．
# （３）1から100までの偶数を表示せよ．
(1)

# n =  0
# while n < 10:
#     n+= 1
#     print(n)

(2)
# while n < 20:
#     n+= 1
#     print(n)

(3)
# n = -11
# while n < 10 :
#     n+= 1
#     print(n)

(4)
# n = 0 
# while n < 10 :
#     n += 2
#     print(n)

(1)
# i = 0
# for i in range(10):
#     i += 1
#     print(i)

(2)
# n = 11
# for i in range(10):
#     n -= 1
#     print(n)

# n = 0 
# for i in range(10,0,-1):
#     print(i)

n = 0 
# for i in range(2,101,2):
#     print(i)
# for i in range(50):
#     n += 2
#     print(n)




# ●問題６－１
# (1)　前回入力した数より倍以上大きな数を入力したら終了するようなプログラムを作りなさい．
# (2)　前回入力した負の数と同じ数を入力したら終了するようにしましょう
# （1,-1,4,-4,5 と入力した時点では，前回入力した負の数は-4です）．
#    （ヒント：xが負のときだけ，yにxを代入しましょう．）
# (3)　2回前に入力した数と同じ数を入力したら終了するようにしましょう．

# x = int(input('please enter an integer > '))
# # y = int(input('please enter an integer > '))
# # while x > y/2 :
# #     x = y 
# #     y = int(input('please enter an integer > '))

# y = None
# while x != y:
#     if x > 0:
#         x = int(input('please enter an integer > '))
#     elif x < 0:
#         y = x
#         x = int(input('please enter an integer > '))
        
        

x = int(input('please enter an integer > '))    
y = int(input('please enter an integer > '))
z = int(input('please enter an integer > '))

while x != z :
    x = y
    y = z
    z = int(input('please enter an integer > '))