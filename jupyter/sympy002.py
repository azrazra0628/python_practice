###　式の操作

#1.式の単純化

# 変数 = simplify( 式オブジェクト )

#%%
from sympy import *

x = symbols('x')

re1 = (x + 1)**2
re2 = 2*x + 7

print(re1)
#(x + 1)**2
print(re2)
#2*x + 7
print(re1 + re2)#上記式を足しただけ
#2*x + (x + 1)**2 + 7  
print(simplify(re1 + re2))
#x**2 + 4*x + 8

#2.式の展開

#変数 = expand(式オブジェクト)
# 多項式を展開する
#%%
from sympy import *

x = symbols('x')
re = (x + 2)**3
print(re)
# (x + 2)**3
print(expand(re))
# x**3 + 6*x**2 + 12*x + 8

#3.他公式の因数分解

# 変数 = factor(式オブジェクト)
#%%
from sympy import *

x = symbols('x')
re = x**3 - x**2 - x + 1
print(factor(re))
# (x - 1)**2*(x + 1)

#4.シンボルに値を代入する

#式オブジェクト.subs(シンボル, 値)

複数のシンボルがある場合は各シンボルと値をタプルでまとめて、それをリスト化する
[(シンボル1,値1),(シンボル2,値2),…]

#%%
from sympy import *

x,y = symbols('x y')

re = x**2 - 2*y
print(re)
# x**2 - 2*y
print(re.subs([(x,10),(y,20)]))
#60

#5.方程式を解く

#solve(式オブジェクト)
# sympyの式は「=0」の式と考える
# リストで返ってくる

#%%
from sympy import *

x = symbols('x')

re = x **2 + 2*x - 8
print(re)
# x**2 + 2*x - 8
print(solve(re))
# [-4, 2]

#6.2元方程式を解く

#2元方程式もsolve関数でとくことができるが、solve関数の引数に式オブジェクトを指定しただけだと
#最初の式オブジェクトに指定された方しか返ってこない
#solve関数の第2引数に解を求めたいシンボルを入力すると,リストで戻ってくる

#%%
from sympy import *

x, y = symbols('x y')
re = (x + y)**2 - 9 

print(re)
# (x + y)**2 - 9
print(solve(re))
# [{x: -y - 3}, {x: -y + 3}]

print(solve(re,x))
#[-y - 3, -y + 3]
print(solve(re,y))
# [-x - 3, -x + 3]

#7.連立方程式を解く

# 複数の式オブジェクトをsolve関数の引数にしてすれば解が求められる

#%%
from sympy import * 

x, y = symbols('x y')

re1 = 2*x + 6* y + 4
re2 = (x + y)**2 - 9

print(re1)
# 2*x + 6*y + 4
print(re2)
# (x + y)**2 - 9
print(solve((re1,re2)))
# [{x: -7/2, y: 1/2}, {x: 11/2, y: -5/2}]
#solve関数の引数は2つ指定しているわけでなく、タプルで1つにまとめてある

print(solve(re1,re2))
#[]

#8.y = xは?

# y = x*2 + x + 1のような文にすると、代入されてしまうので、Eq関数を使用する

# 変数 = Eq(左辺, 右辺)

#%%
from sympy import * 

x, y = symbols('x y')
re1 = Eq(y, x**2 + 6*x + 2)
re2 = Eq(y, (x + 2)**2 )

print(re1)
#Eq(y, x**2 + 6*x + 2)
print(re2)
#Eq(y, (x + 2)**2)
print(solve((re1,re2)))
# [{x: 1, y: 9}]

#9.極限について

#limit(式, シンボル, 極限値)

#%%
from sympy import *

x, n = symbols('x n')
re = 1 / x **n  + 1

print(limit(re, n, oo))
#1
print(limit(re, n, 1))
# (x + 1)/x

#10.微分について

#diff(式, シンボル, 階数)

#%%
from sympy import *

x, y = symbols('x y')

re = 2*x**3
print(diff(re, x))
#6*x**2
print(limit((2*(x + y)**3 - 2*x**3)/y, y, 0))
#6*x**2
print(diff(re, x, 2))
# 12*x
print(limit((6*(x + y)**2 - 6*x**2)/y, y, 0))
# 12*x



