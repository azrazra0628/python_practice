###抽象クラス###
##インスタンスを作れないクラスのこと
##抽象クラスを基底クラスにすることで抽象基底クラスとして使用する
# import abc
# class クラス名(abc.ABC):
#     @abc.abstractmethod
#     def メソッド名(self, 引数, …):
#         pass

import abc
class player(abc.ABC):
    @abc.abstractmethod
    def battle(self):
        pass

class fighter(player):
    def battle(self):
        print('slash')

class wizard(player):
    def battle(self):
        print('magic')

for p in [fighter(), wizard()]:
    p.battle()

##抽象クラスと抽象メソッドを使用して以下の事柄を実現できる
# (1)インスタンスを生成しないクラスを定義することができる
# (2)派生クラスにメソッドのオーバーライドを義務付けることができる



