

a = 5
b = 2
wa = a + b
sa = a - b
kakeru = a * b
waru1 = a // b
amari = a % b
waru2 = a / b
print(a, '+', b, '=', wa, sep=' ')
print(a, '-', b, '=', sa, sep=' ')
print(a, '×', b, '=', kakeru, sep=' ')
print(a, '÷', b, '=', waru1, ' 余り', amari, sep=' ')
print(a, '÷', b, '=', waru2,sep=' ')


a = 65
b = 88

total = a + b
avg = a/2 + b/2

print('英語の成績を入力してください>', a,sep=' ')
print('数学の成績を入力してください>', b,sep=' ')
print('英語の得点: ', a, sep=' ')
print('数学の得点: ', b, sep=' ')
print('合　　　計: ', total, sep=' ')
print('平　　　均: ', avg, sep=' ')


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

jisoku = float(input('時速(km/h)>'))

byousoku = jisoku /3600 * 1000
print('秒速　= ', byousoku, 'm/s', sep=' ')


en = int (input('金額（円）>'))

print('金額:', en, sep=' ')
maisuu = en // 10000
en = en % 10000
print('1万円札=', maisuu, '枚', sep=' ')
maisuu = en // 5000
en = en % 5000
print('5千円札=', maisuu, '枚', sep=' ')
maisuu = en // 1000
en = en % 1000
print('千円札=', maisuu, '枚', sep=' ')
maisuu = en // 500
en = en % 500
print('500円玉=', maisuu, '枚', sep=' ')
maisuu = en // 100
en = en % 100
print('100円玉=', maisuu, '枚', sep=' ')
maisuu = en // 50
en = en % 50
print('50円玉=', maisuu, '枚', sep=' ')
maisuu = en // 100
en = en % 100
print('10円玉=', maisuu, '枚', sep=' ')
maisuu = en // 5
en = en % 5
print('5円玉=', maisuu, '枚', sep=' ')

print('1円玉=', en, '枚', sep=' ')

num = int(input('数（0－6）>'))
if num == 0:
    print('日曜日')
elif num == 1:
    print('月曜日')
elif num == 2:
    print('火曜日')
elif num == 3:
    print('水曜日')
elif num == 4:
    print('木曜日')
elif num == 5:
    print('金曜日')
elif num == 6:
    print('土曜日')
else:
    print('0から6までの数字を入力してください')

seireki = int(input('西暦で年を入力してください>'))

leap = False
if seireki % 400 == 0:
    leap = True
elif seireki % 100 == 0:
    leap = False
elif seireki % 4 == 0:
    leap = True


if leap:
    print(str(seireki)+'年はうるう年です。'
else:
    print(str(seireki)+'年はうるう年ではありません。')




year = int(input('年>'))
month = int(input('月>'))
day = int(input('日>'))
datestr = str(year)+'年'+str(month)+'月'+str(day)+'日'
if month == 1 or month ==2:
    year = year -1
    month = month + 12
weekday = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7
 if weekday == 0:
    weekstr = '日曜日'
elif weekday == 1:
    weekstr = '月曜日'
elif weekday == 2:
    weekstr = '火曜日'
elif weekday == 3:
    weekstr = '水曜日'
elif weekday == 4:
    weekstr = '木曜日'
elif weekday == 5:
    weekstr = '金曜日'
elif weekday == 6:
    weekstr = '土曜日'
print(datestr+'は'+weekstr+'です。')




import random

print('ジャンケンポン！')
yours = int(input('あなたは？(0:グー、　1:チョキ、2:パー)>'))
comp =random.randint(0,2)
if comp == 0:
    compstr = 'わたしはグー。'
    if yours == 0:
        yourstr = 'あなたもグー。'
        result = 'あいこです。'
    elif yours == 1:
        yourstr = 'あなたはチョキ。'
        result = 'わたしの勝ちです。'
    elif yours == 2:
        yourstr = 'あなたはパー。'
        result = 'あなたの勝ちです。'
elif comp == 1:
    compstr = 'わたしはチョキ。'
    if yours == 0:
        yourstr = 'あなたはグー。'
        result = 'あなたの勝ちです。'
    elif yours == 1:
        yourstr = 'あなたもチョキ。'
        result = 'あいこです。'
    elif yours == 2:
        yourstr = 'あなたはパー。'
        result = 'わたしの勝ちです。'
elif comp == 2:
    compstr = 'わたしはパー。'
    if yours == 0:
        yourstr = 'あなたはグー。'
        result = 'わたしの勝ちです。'
    elif yours == 1:
        yourstr = 'あなたはチョキ。'
        result = 'あなたの勝ちです。'
    elif yours == 2:
        yourstr = 'あなたもパー。'
        result = 'あいこです。'
print(compstr+yourstr+result)

n = int(input('数>'))
fac = 1
for i in range(1,n+1):
    fac *= i
print(str(n)+'! =', fac, sep=' ')


n = int(input('数>'))
temp = 1
for i in range(n):
    i = '■'

n = int(input('数> '))
print(str(n)+':',end='') # 改行しない出力
for i in range(0,n) :
    print('■',end='')
print() # 改行だけ出力
# Python3による別解
print(str(n)+':'+('■'*n))


n = int(input('数> '))
# print(str(n)+':',end='') # 改行しない出力
# for i in range(0,n) :
#     print('■',end='')
# print() # 改行だけ出力
# # Python3による別解
print(str(n)+':'+('■'*n))


n = int(input('数>'))
for j in range(1,n+1):
    print(str(j)+':', end='')
    for i in range(0,j):
        print('■', end='')
print()




counter = 0
goukei = 0
data = int(input('データ入力(負の数で終了)>'))
while data >= 0:
    counter += 1
    goukei += data
    data = int(input('データ入力(負の数で終了)>'))
heikin = goukei /counter
print('データ数:',counter,'合計:',goukei,'平均:',heikin)






shakkin = int(input('借金> '))
riritsu = float(input('年利率(%)> '))
hensai =  int(input('返済額> '))
total = 0
month = 0
while shakkin > hensai :
    month += 1
    shakkin = shakkin*(1 + riritsu/12/100) - hensai
    print(str(month)+'月: 返済額',hensai,'円','残り',\
    int(shakkin),sep=' ')
    total += hensai
month += 1
shakkin = shakkin*(1 + riritsu/12/100)
total += shakkin
print(str(month)+'月: 返済額',int(shakkin),'円','これで完済。','返済総額: ',\
int(total),'円',sep=' ')
