###演算子のオーバーロード###
# +や＊といった演算子をプログラマが独自に定義するための機能


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def print(self):
        print(self.r, self.g, self.b)

c1 = Color(10, 20, 30)
c1.print()

c2 = Color(40, 50, 60)
c2.print()

c3 = c1 + c2

##下記のエラーが表示される
#TypeError: unsupported operand type(s) for +: 'Color' and 'Color'

# class クラス名:
#     def __add__(self,  other):
#         処理

# +  __add__   加算
# -  __sub__   減算
# *  __mul__   乗算
# /  __truediv__  除算
# // __floordi__  除算（小数点以下切り捨て）
# %  __mod__   剰余算
# ** __pow__ べき乗

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def print(self):
        print(self.r, self.g, self.b)
    
    def __add__(self, other):
        r = self.r + other.r
        g = self.g + other.g
        b = self.b + other.b
        return Color(r, g, b)

c1 = Color(10, 20, 30)
c1.print()

c2 = Color(40, 50, 60)
c2.print()

c3 = c1 + c2
c3.print()


###__str__メソッド###
##__str__メソッドを使うことで、print関数やformat関数にインスタンスを渡して出力できる
# class クラス名:
#     def __str__(self):
#         処理

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def print(self):
        print(self.r, self.g, self.b)
    
    def __add__(self, other):
        r = self.r + other.r
        g = self.g + other.g
        b = self.b + other.b
        return Color(r, g, b)
    
    def __str__(self):
        return str(self.r) + ' ' + str(self.g) + ' ' + str(self.b)

c1 = Color(10, 20, 30)
print(c1)
c2 = Color(40, 50, 60)
print(c2)

c3 = c1 + c2
print(c3)

##メソッドを使用しなくて通常の数値や文字列と同様に関数出力ができる


###ダックタイピング###
##あるインスタンスに対してある処理を行うと、その処置に必要な機能を備えていればどのクラスのインスタンスかは問わない

def sum(x, y, z):
    return x + y + z

sum(1, 2, 3)

s = sum('Hello', 'python', 'World')
print(s)

c = sum(Color(10, 20, 30), Color(40, 50, 60), Color(70, 80, 90))
print(c)

##いろいろな種類の値に対して、共通の処理を適用することができる



