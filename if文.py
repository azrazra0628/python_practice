#比較演算子
#
#
#
#
#
123*45 > 5000
678 * 90 <= 60000
1*2*3*4*5 ==120
if temp < 20:
    print('heater')
elif temp >= 30:
    print('cooler')
else:
    print('stop')

#メンバーシップ

'力' not in 'ヵヵヵヵヵ'

card = [1,2,3,4,5,6,7,8]
9 in card
9 not in card

#論理演算子
temp = 31
if 15 <= temp and temp < 25:
    print('go outside')

if 15 <= temp or  temp < 25:
    print('stay inside')

if not (15 <= temp and temp < 25):
    print('stay inside')



