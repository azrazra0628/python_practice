### sympyの基本

##1 sympy概要
# 代数計算が可能なモジュール
# 基本的な演算に加えて、基本的な数学関数を備えている。
# シンボルやそれらを使って立てた式の展開や簡略化などの代数計算で必要な基本的な機能が備わっている

##2.整数・実数・分数
# 値として「整数」「実数」「分数」の三種類の値が用意されている
# Integer - 整数クラス
# Float - 実数クラス
# Rational - 分数クラス
# pythonで使われるintやfloatとは違うもの。
# これらはすべてNumberクラスの派生クラスの為、共通のメソッドが利用可能

##3.intとIntegerの違い

#%%
from sympy import *

a = Integer(100)
b = 100
print(type(a))
#<class 'sympy.core.numbers.Integer'>
print(type(b))
#<class 'int'>
print(a.evalf(10))
#100.0000000
prime(b.evalf(10))
#AttributeError: 'int' object has no attribute 'evalf'  
##intクラスにはevalfメソッドが用意されていないため、使用できない

##4.分数について
# 分数の表記の方法は下記の通り
# Rational（分子, 分母)
# Rationalは分数を計算した実数ではなく、分数そのものである。

#%%
from sympy import *

a = 1 / 3
b = Rational(1, 3)

print(a)
#0.3333333333333333
print(b)
#1/3

##5.N,evalfによる実数換算

# Rationalの値を実数換算する場合には下記の二つの方法がある
# N(元値, 桁数)
# インスタンス.evalf(桁数)

#%%
from sympy import *

a = Rational(1, 3)

print(N(a,10))
#0.3333333333
print(a.evalf(10))
#0.3333333333

##6.定数(π,e,無限大)について

# 下記定数もsympyで用意されている
# pi - 円周率の定数 - Pi
# E - 自然対数の定数　- Exp1
# oo - 無限大の定数 - Infinity
# IntegerやFloatと同様にNumberクラスの派生クラスの為、共通のメソッドが使用可能

#%%
from sympy import *

print(N(pi,30))
#3.14159265358979323846264338328
print(N(E,30))
#2.71828182845904523536028747135
print(N(oo,30))
#inf

##7.基本的な計算
# 四則演算、優先順位の（）など問題なく使用可能
#%%
from sympy import *

a = Rational(1,3)
b = Rational(5,6)
print((a + b)**2)
#49/36

整数との計算も可能
#%%
from sympy import *

a = Rational(1,3)
b = (a + 3)**2 -4
print(b)
#64/9

# 式の中に一つでもsympyの派生クラスが使用されていれば、結果はいずれかの値になる
print(type(b))
#<class 'sympy.core.numbers.Rational'>

##8.平方根について
# mathパッケージにあるsqrtとsympy独自のsqrt関数の差異について

#sympy独自のsqrt関数の場合はRationalクラスと同様に平方根そのもので返し、実数にする場合にはNやevalfが必要
#%%
from sympy import *

a1 = sqrt(32)
b1 = sqrt(24)
pprint(a1)
#4⋅√2
pprint(b1)
#2⋅√6

pprint(a1 *b1)
#16⋅√3

mathモジュールを使用する場合には実数で返ってくる
#%%
import math

a2 = math.sqrt(32)
b2 = math.sqrt(24)
print('a2=%s , b2=%s' %(a2,b2))
#a2=5.656854249492381 , b2=4.898979485566356
print(a2 * b2)
#27.712812921102035

##9.変数とシンボル
# プログラミング言語で使う変数とは異なり、シンボルを作成し、代数として扱う

# シンボルの作成(1)
# 変数 = symbols(変数名)
#symbols関数を使用して変数名で引数に指定した名前のシンボルを作成する

#%%
x = symbols('x')
(x,y) =symbols('x,y')
print(x)
#x
print(type(x))
#<class 'sympy.core.symbol.Symbol'>

# シンボルの作成(2)
# 変数 = Symbol(変数名)
#Symbolクラスとして用意されているため、symbolインスタンスを作成することもできる　

#%%
z = Symbol('z')
print(z)
#z
print(type(z))
#<class 'sympy.core.symbol.Symbol'>

#シンボルで式を作成すると、式の結果ではなく式そのものが変数に代入される

#%%
from sympy import *
import math

x = symbols('x')
res = x**2 +4*x -6
print(res)
#x**2 + 4*x - 6

print(type(res))
#<class 'sympy.core.add.Add'>
