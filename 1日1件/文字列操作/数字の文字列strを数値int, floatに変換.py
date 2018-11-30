## 数字の文字列strを数値int, floatに変換

# Pythonで数字の文字列strを数値に変換したい場合、
# 整数に変換するにはint()、浮動小数点に変換するにはfloat()を使う。

#1. 数字の文字列を整数に変換: int()

# int()関数で数字の文字列を整数int型の数値に変換できる。

#%%
print(int('100'))
# 100
print(type(int('100')))
# <class 'int'>

# .を含む小数、,で桁区切りされた文字列はエラーValueErrorとなる。

#%%
print(int('1.23'))
# ValueError: invalid literal for int() with base 10: '1.23'
print(int('10,000'))
# ValueError: invalid literal for int() with base 10: '10,000'

# カンマ区切りされた文字列はreplace()メソッドで,を削除すれば変換可能。

#%%
print(int('10,000'.replace(',','')))
# 10000

#2. 数字の文字列を浮動小数点に変換: float()

# float()関数で数字の文字列を浮動小数点float型の数値に変換できる。

#%%
print(float('1.23'))
# 1.23
print(type(float('1.23')))
# <class 'float'>

# 整数部が省略された文字列は整数部に0が補完される。

#%%
print(float('.23'))
# 0.23

# 2進数、8進数、16進数表記の文字列を数値に変換

# int()関数の第二引数に基数を指定すると、
# 文字列を2進数、8進数、16進数などとみなして整数intに変換できる。
# 省略した場合は10進数とみなされる。

#%%
print(int('101', 2))
# 5
print(int('70', 8))
# 56
print(int('ff', 16))
# 255

# 基数を0とすると、文字列のプレフィックス（0b, 0o, 0x）をもとに変換される。

#%%
print(int('0b101', 0))
print(int('0o70', 0))
print(int('0xFF', 0))
# 5
# 56
# 255

#4. 指数表記の文字列を数値に変換
# 指数表記の文字列はfloat()でそのままfloat型に変換できる。

#%%
print(float('1.23e-4'))
print(type(float('1.23e-4')))
# 0.000123
# <class 'float'>

print(float('1.23e4'))
print(type(float('1.23e4')))
# 12300.0   
# <class 'float'>

#5. 全角アラビア数字の文字列を数値に変換

# 全角のアラビア数字はint()やfloat()でそのまま数値に変換できる。

#%%
print(int('１００'))
print(type(int('１００')))
# 100
# <class 'int'>

print(float('１００'))
print(type(float('１００')))
# 100.0
# <class 'float'>   

# ただし、マイナス-や小数点のピリオド．などの記号が全角だとエラーValueErrorになる。

#%%
print(float('ー１．２３'))
# ValueError: could not convert string to float: '１．２３'

# 数字が全角でマイナス-、小数点のピリオド.が半角だと問題なく変換できる。
# replace()メソッドで全角の記号を半角の記号に置換すれば変換可能。

#%%
print(int('ー１２３'.replace('ー', '-')))
# -123


#6. 漢数字の文字列を数値に変換

# unicodedataモジュールのunicodedata.numeric()関数を使うと
# Unicodeの漢数字一文字を浮動小数点float型の数値に変換できる。

# 一文字じゃないとエラーTypeError、数字ではない文字もエラーValueErrorになる。

#%%
import unicodedata

print(unicodedata.numeric('五'))
print(type(unicodedata.numeric('五')))
# 5.0
# <class 'float'>

print(unicodedata.numeric('十'))
# 10.0

print(unicodedata.numeric('参'))
# 3.0

print(unicodedata.numeric('億'))
# 100000000.0

# まとめ
# ①数字の文字列をintやfloatに変更できる
# ②漢字や指数表記も可能
