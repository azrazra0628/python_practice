## zip関数の使い方: 複数のリストの要素をまとめて取得

# Pythonの組み込み関数zip()は複数の
# イテラブルオブジェクト（リストやタプルなど）の要素をまとめる関数。
# forループで複数のリストの要素を取得する際などに使う。

#1. forループで複数のリストの要素を取得

# forループの中で複数のイテラブルオブジェクト（リストやタプルなど）
# の要素を同時に取得して使いたい場合は、zip()関数の引数にそれらを指定する。

# 変数 = zip(イテラブル1, イテラブル2)

#%%
names = ['Alice', 'Bob', 'Charlie']
ages = [20, 30, 40]

for name, age in zip(names, ages):
    print(name, age)
# Alice 20
# Bob 30
# Charlie 40

# 2つだけでなく、3つ以上でも同様。

#%%
names = ['Alice', 'Bob', 'Charlie']
ages = [20, 30, 40]
points = [80, 90, 100]

for name, age, point in zip(names, ages, points):
    print(name, age, point)
# Alice 20 80
# Bob 30 90
# Charlie 40 100

#2. 要素数が異なる場合の処理

# zip関数では多い分の要素が無視される

#%%
names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18

# 標準ライブラリitertoolsモジュールのzip_longest()を使うと、
# それぞれのリストの要素数が異なる場合に、足りない要素を任意の値で埋めることができる。
#デフォルトはnoneで埋められる

#%%
from itertools import zip_longest

names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]

for name, age in zip_longest(names, ages):
    print(name,age)
# Alice 24
# Bob 50
# Charlie 18
# Dave None

# 引数fillvalueを指定するとその値で埋められる

#%%
names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]

for name, age in zip_longest(names, ages, fillvalue=20):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18
# Dave 20 #fillvalueで指定した20になる

# 要素が足りないリストが複数ある場合も埋める値は一律。
# 別々の値を指定することはできない。

#%%
names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]
points = [80,90]

for name, age, point in zip_longest(names, ages, points, fillvalue=20):
    print(name, age, point)
# Alice 24 80
# Bob 50 90
# Charlie 18 20 #要素がない為、pointに20が埋まる
# Dave 20 20　#要素がない為、ageとpointに20が埋まる



# 要素数が不明の複数のリストをそれぞれ別の値で埋めたい場合は、

# すべてのリストに対して埋める値を定義しておく
# 最大の要素数を取得する
# すべてのリストを最大の要素数まで埋める
# zip()関数を使う


#%%
# すべてのリストに対して埋める値を定義しておく
fill_name = 'XXX'
fill_age = 20
fill_point = 50

# 最大の要素数を取得する
len_names = len(names)
len_ages = len(ages)
len_points = len(points)

max_len = max(len_names, len_ages, len_points)

# すべてのリストを最大の要素数まで埋める
names = names + [fill_name] * (max_len - len_names)
ages = ages + [fill_age] * (max_len - len_ages)
points = points + [fill_point] * (max_len - len_points)

print(names)
print(ages)
print(points)

# zip()関数を使う
for name, age, point in zip(names, ages, points):
    print(name, age, point)

# Alice 24 80
# Bob 50 90
# Charlie 18 50
# Dave 20 50

# これを関数化すると以下のようになる。
# 元のリストとリストを埋める値をそれぞれ
# イテラブル（リストやタプル）で引数に指定するようにしている。

#%%

def my_zip_longest(iterables, fillvalues):
    max_len = max(len(i) for i in iterables)
    return zip(*[list(i) + [v] * (max_len - len(i)) for i, v in zip(iterables, fillvalues)])

for name, age, point in my_zip_longest((names, ages, points), ('XXX', 20, 50)):
    print(name, age, point)
# Alice 24 80
# Bob 50 90
# Charlie 18 50
# Dave 20 50


#3. 複数のイテラブルの要素をタプルにまとめたリストを取得
# zip関数は複数のイテラブルオブジェクトの要素
# をタプルでまとめたイテレータ（zipオブジェクト）を返す関数。

# forループの外でも使えるし、対象はリストに限定されない。

#%%
names = ['Alice', 'Bob', 'Charlie']
ages = (24, 50, 18)

z = zip(names, ages)
print(z)
#<zip object at 0x000001CA43196E48>
print(type(z))
# <class 'zip'>

l = list(zip(names, ages))
print(l)
# [('Alice', 24), ('Bob', 50), ('Charlie', 18)]
print(type(l))
# <class 'list'>
print(type(l[0]))
# <class 'tuple'>


# まとめ
# ①複数のリストなどのイテラブルオブジェクトの中の要素をまとめて取得したい場合にはzip関数を使う
# ②要素の数が異なる場合には、itertoolsを使用するか、元の要素を最大要素数のものにあわせてzip関数を使用する
# ③zip関数はイテラブルオブジェクトであれば使用可能

