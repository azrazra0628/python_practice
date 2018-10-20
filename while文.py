##while文　指定した式の値がTrueの間処理を繰り返す
#break文　繰り返しの中断
stage = 1 
while stage <=  8:
    print(stage)
    if stage == 4:
        break
    stage += 1

#continue文　繰り返しの先頭に戻って継続
stage = 1 
while stage <=  8:
    print(stage)
    if stage == 4:
        stage = 8
        continue
    stage += 1


#ネスト　繰り返し構文の中に別の繰り返し構文を入れる




# 数当てゲームを作りたい．
# １から100までのランダムな整数を用意し，
# キーボードから入力した数がその数と同じならば
# 終了するプログラムを作成する．

# ただし，はずれたときは，
# 正解よりも大きかったか小さかったかを表示して
# ヒントを出すようにすること．　【やや難】


import random

x = random.randint(1, 100)
turn = 0
print('数あてゲームだよ')


while True :
    n = int(input('1~100までの整数を入力してね  ＞　'))
    turn += 1
    if x > n :
        print('相手の数の方が大きいよ')
    elif x < n :
        print('相手の数より大きいよ')
    else :
        print('正解だよ')
        break
print('答えは{}でした.正解までに{}ターンかかりました。'.format(x, turn))

