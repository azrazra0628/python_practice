# Pythonで大文字・小文字を操作する文字列メソッド一覧

# Pythonには文字列の大文字・小文字を操作する便利なメソッドが標準で用意されている。

#1. 大文字と小文字の変換

# str.capitalize(): 先頭の一文字を大文字、他を小文字にする

#%%
str = 'python is a good programing language'
print(str.capitalize())
# Python is a good programing language

# str.lower(): すべての文字を小文字にする

#%%
print(str.lower())
# python is a good programing language

# str.upper(): すべての文字を大文字にする

#%%
print(str.upper())
# PYTHON IS A GOOD PROGRAMING LANGUAGE

# tr.title(): 単語の先頭の一文字を大文字、他を小文字にする

#%%
print(str.title())
# Python Is A Good Programing Language

# str.swapcase(): 大文字を小文字に、小文字を大文字にする

#%%
str_org = "pYthon iS a gooD proGramming laNguage"
print(str_org.swapcase())
# PyTHON Is A GOOd PROgRAMMING LAnGUAGE

#2. 大文字と小文字の判定

# str.islower(): すべての文字が小文字かどうか判定する
# 小文字と大文字の区別がある文字が少なくとも一文字以上含まれていて、
# その全てが小文字のときはTrue、それ以外はFalseを返す。

#%%
str_org = "pYthon iS a gooD proGramming laNguage"
str_org.islower()
# False

# str.isupper(): すべての文字が大文字かどうか判定する

#%%
str_org.isupper()
# False

# まとめ
# ①小文字・大文字の変換には.upper,lowerのメソッドを使用する