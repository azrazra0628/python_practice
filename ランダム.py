####モジュール####
###組み込みでない関数を使うばあいには、その定義を含んだモジュールをインポートする必要がある
# import モジュール名

# モジュール内の関数を呼び出すときは以下の通り
# モジュール名.関数名()
# モジュール名.関数名(引数1, 引数2, …)


###ランダム関数###
##乱数を生成するモジュール

import random
random.random()

##整数Å～Bの範囲で整数乱数を生成する場合
# random.randint(整数A, 整数B)

random.randint(1, 6)

##モジュールをインポートし、別名をつける
# import モジュール名 as 名前

import random as r
r.randint(1, 10)

##モジュール内の機能をインポートして、モジュール名なしに使えるようにする
# from モジュール名 import 機能名

from random import randint
randint(1, 10)

##モジュール内の機能に別名を付けてインポートする
# from モジュール名 import 機能名　as 名前

from random import randint as ri
ri(1, 10)


###choice関数#＃＃
##シーケンス（文字列、リスト、タプル）からランダムに要素を選んで返す
import random
flavor = ['バニラ', 'ストロベリー', 'チョコレート']
random.choice(flavor)

###shuffle関数###
##シーケンス（リスト）内　に格納されている要素の位置をランダムに変更する
import random
card = ['A', 'B', 'C', 'D', 'E', 'F']
random.shuffle(card)
