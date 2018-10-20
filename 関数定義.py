def trip(dist, speed):
    """距離と速度から所要時間を計算します.
    
    引数:
    dist --- 距離(distance)
    speed --- 速度
    """
    time = dist / speed
    return time
    

def sum(n):
    if n > 0:
        return n + sum(n-1)
    return 0


def lunch(main, side, drink):
    print('今日の夕食')
    print('main :', main)
    print('side :', side)
    print('drink :', drink)

#位置引数
lunch('steak', 'salad',  'coffee')

#キーワード引数
lunch(side='salad', main='steak', drink='coffee')

#位置引数とキーワード引数の組み合わせ
#併用する場合には位置引数を左にキーワード引数を右に記述
lunch('steak', drink='coffee', side='salad')

#デフォルト引数を指定
def lunch(main='beef', side='salad', drink='coffee'):
    print('main :', main)
    print('side :', side)
    print('drink :', drink)

lunch('steak')



list(map(lambda x: x*x, [1, 2, 3, 5, 5]))

a = []
for x in [1, 2, 3, 4, 5]:
    a.append(x*x)

print(a)


