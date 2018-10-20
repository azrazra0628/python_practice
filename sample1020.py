# キーボードから１０個の数字を入力し，
# (1)　負の数がいくつ入力されたかを表示するプログラムを作りなさい．
# (2)　偶数がいくつ入力されたかを表示するプログラムを作りなさい．

# count = 0
# lst = []
# for i in range(10) :
#     n = int(input('please enter an interger > '))
#     if n % 2  == 0 :
#         count += 1
#         lst.append(n)
# print('偶数は、',count,'回表示されました。',sep='')
# print('合計値は,',sum(lst),'です。')


# ●問題６－４
# (1)　キーボードから入力した10個の数の中に5がなければ5 ga arimasenと表示するようにしましょう．
# (2)　入力した10個の数の中に負の数があるかどうかを表示するようにしましょう

# count = 0
# lst = []
# for i in range(10):
#     n = int(input('please enter an interger > '))
#     if n  < 0 :
#         count += 1
#         lst.append(n)
# if count == 0 :
#     print('5が入力されていません')
# else :
#     print('5が',count,'回入力されました。',sep='')


# 数を10個入力してその合計を表示するプログラムを作りなさい．

# lst = []
# for i in range(10) :
#     j = int(input('please enter an interger > '))
#     lst.append(j)
# print(sum(lst))

# 足し算だけの電卓を作りなさい．数を入力し，今まで入力した数の合計を表示する，
# という作業を繰り返すプログラムです．
# さらに，0 を入力したときは終了するようにしなさい．
# 例えば，10,20,63,0 と入力すると，このようになります．「10 10 20 30 63 93 0」


# lst =[]
# while True :
#     n = int(input('please enter an interger > '))
#     lst.append(n)
#     print('入力した数字の合計値は',sum(lst), 'です' ,sep='')
#     if n == 0 :
#         print('0が入力されたため、処理を終了します')
#         print('入力した数字の合計値は',sum(lst), 'です' ,sep='')
#         break

    
# 入力した10個の数の中に1と0，どちらが多いかを判定するプログラムを作りなさい．

# count0 = 0
# count1 = 0

# for i in range(10) :
#     n = int(input('please enter an interger > '))
#     if n == 0 :
#         count0 += 1
#     elif n == 1 :
#         count1 += 1
# if count0 > count1 :
#     print('0のほうが１より',count0 - count1,'回多く入力されています', sep='')
# elif count1 > count0 :
#     print('1のほうが0より',count1 - count0,'回多く入力されています', sep='')
# elif count0  == 0 :
#     print('0と1が入力されていません')
# else :
#     print('同じ回数入力されています')


# ●問題６－１０
# 最初の行でimport randomと入力した上で、
# x= random.randint(1,100)という命令は，
# xに0～99の適当な（ランダムな）数を代入するものです．
# これを100回行って，xに30以下の数が何回代入されたかを表示するプログラムを作りなさい．

# import random
# count = 0
# x = int(input('処理を開始します。\n開始してもよろしいでしょうか(1:yes 0:no)'))
# if x == 1 :
#     for i in range(100):
#         n = random.randint(1,100)
#         if n < 30 :
#             count += 1
#     print('30未満の数は',count,'回選択されました',sep='')
# else :
#     print('処理を中止します')


# 　うるう年というのは、四年に一度、二月が29日まである年のことをいうと思われていますが
# 、正確にはもっと複雑です。西暦の年に対して、
#     年が400で割り切れるなら、うるう年です。
#     そうではなくて年が100で割り切れるならば、うるう年ではありません。
#     そうでもなくて年が4で割り切れるならば、うるう年です。
# このルールに従って、西暦の年を入力してうるう年を判定するプログラムを書きなさい。

# seireki = int(input('西暦で年を入力してください > '))
# if seireki % 400 == 0 :
#     print(seireki,'年はうるう年です',sep='')
# elif seireki % 100 == 0 :
#     print(seireki,'年はうるう年ではありません',sep='')
# elif seireki % 4 == 0 :
#     print(seireki,'年はうるう年です',sep='')
# else :
#     print(seireki,'年はうるう年ではありません',sep='')


# year,month,day = (int(input('年 > ')),int(input('月 > ')),int(input('日 > ')))
# detestr = str(year)+'年'+str(month)+'月'+str(day)+'日'
# if month == (1 or 2) :
#     month = month + 12
#     year = year - 1
# weekday = (year + (year // 4) - (year // 100) + \
#   (year // 400) + ((13*month+8) // 5) + day) % 7
# # weekday = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7
# if weekday == 0 :
#     weekstr = '日曜日'
# elif weekday == 1 :
#     weekstr = '月曜日' 
# elif weekday == 2 :
#     weekstr = '火曜日'  
# elif weekday == 3 :
#     weekstr = '水曜日'  
# elif weekday == 4 :
#     weekstr = '木曜日'  
# elif weekday == 5 :
#     weekstr = '金曜日'  
# elif weekday == 6 :
#     weekstr = '土曜日'
# print(detestr,'は',weekstr,'です',sep='')


# year = int(input('年> '))
# month = int(input('月> '))
# day = int(input('日> '))
# datestr = str(year)+'年'+str(month)+'月'+str(day)+'日'
# if month == 1 or month == 2 :
#     year = year - 1
#     month = month + 12
# weekday = (year + (year // 4) - (year // 100) + \
#   (year // 400) + ((13*month+8) // 5) + day) % 7
# if weekday == 0 :
#     weekstr = '日曜日'
# elif weekday == 1 :
#     weekstr = '月曜日'
# elif weekday == 2 :
#     weekstr = '火曜日'
# elif weekday == 3 :
#     weekstr = '水曜日'
# elif weekday == 4 :
#     weekstr = '木曜日'
# elif weekday == 5 :
#     weekstr = '金曜日'
# elif weekday == 6 :
#     weekstr = '土曜日'
# print(datestr+'は'+weekstr+'です。')


# 　計算機とジャンケンをするプログラムを書きましょう
# 。グー、チョキ、パーをそれぞれ0,1,2の整数で表すとします。
# あなたの出す手を整数で入力し、勝負するようにします。
# コンピュータの出す手は乱数（同じ確率ででたらめに数を自動的に生成する仕組み）を使って作り出します。
# 具体的には、random.randint(最小値, 最大値)という式を使うと
# 自動的に最小値から最大値までのでたらめな整数を作ってくれます。
# (プログラムの始めに、'import random'の宣言が必要)
#  comp=random.randint(0,2)
# こうすると、このcompに0か1か2の整数がでたらめに代入されます。
# 入力したあなたの手とこのcompを比較して、
# ジャンケンの勝負を判定するプログラムを作りなさい。

# ３つの数を入力し、数を昇順に並べ替えてから出力するプログラムを作成してください。
# 実行結果
# 数1> 55
# 数2> 25
# 数3> 13
# 13 25 55

# n1,n2,n3 = (int(input('数1 > ')),int(input('数2 > ')),int(input('数3 > ')))
# lst = [n1,n2,n3]
# print(sorted(lst,reverse=True))

# 　1以上の整数を入力し、
# その数までのべき乗を計算するプログラムを作成せよ。


# n = int(input('数　> '))
# fac = 1
# for i in range(1,n+1):
#     fac *= i
# print(str(n)+'! =',fac,sep=' ')




# 　数字を入力し、
# 入力した数だけ画面に■印を表示するプログラムを書きなさい。

# n = int(input('数 > '))
# print(str(n)+':',end='')
# for i in range(1,n+1) :
#     print('■',end='')

# print(str(n)+':'+('■'*n))

    # 数字を入力して、
    # 1からその数までの棒グラフを順に表示するプログラムを書きなさい。
count = 0
n = int(input('数 > '))
for i in range(1,n+1):
    print(str(i),':','■'*i,sep='')
