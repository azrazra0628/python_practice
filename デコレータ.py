###デコレータ###
##デコレータは関数やメソッドを加工し、機能を追加する
#@デコレータ名

#デコレータは自分で定義できる
#import functools
#def デコレータ名(f):
#   @functools.wraps(f)
#   def wrapper(*x, **y):
#       前処理
#       f(*x, **y)
#       後処理
#   returun wrapper

#importはモジュールをインポートする構文

import functools

def deco(f):
    @functools.wraps(f)
    def wrapper(*x, **y):
        print('BEGIN!!')
        f(*x, **y)
        print('END!!')
    return wrapper

@deco
def hello():
    print('Hello')

hello()














