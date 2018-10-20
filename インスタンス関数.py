###インスタンス関数###
##インスタンス関数を使用すると、あるインスタンスが指定したクラスのインスタンスか調べることができる##
#isinstance(変数, クラス名)
#派生クラスのインスタンスが基底クラスのインスタンスか調べることができる
class player:
    pass

class fighter(player):
    pass

class wizard(player):
    pass

f = fighter()

print(isinstance(f, player))
print(isinstance(f, fighter))
print(isinstance(f, wizard))
