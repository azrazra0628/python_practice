## Pythonリスト内包表記の使い方
# Pythonでは、新しいリストを生成するときにリスト内包表記（List comprehension）を使うとシンプルに書ける。

#1.リスト内包表記の基本型

# 基本形は以下の通り
# [式 for 任意の変数 in イテラブルオブジェクト]

# テラブルオブジェクトというのは、シーケンス型や辞書型のような反復処理が可能なオブジェクトのこと

#%%
squares = [i**2 for i in range(5) ]
print(squares)
# [0, 1, 4, 9, 16]]

# 上記と等価なfor文は以下の通り
#%%
squares = []
for i in range(5):
    squares.append(i**2)

print(squares)
# [0, 1, 4, 9, 16]

#2.ifで条件分岐したリスト内包表記
# ifで条件分岐することも可能。以下のように後置でifを記述する。
# [式 for 任意の変数名 in イテラブルオブジェクト if 条件式]

# 条件式がTrueとなるイテラブルオブジェクトの要素のみ式で評価される。

#%%
odds = [i for i in range(10) if i % 2 == 1]
print(odds)
# [1, 3, 5, 7, 9]

# 上記と等価になるfor文は以下の通り
#%%
odd = []
for i in range(10):
    if i % 2 == 1:
        odd.append(i)

print(odd)
#[1, 3, 5, 7, 9]

#3.三項演算子との組み合わせ（if else的な処理）
# if elseのように条件を満たさない要素には別の処理を行いたい場合は三項演算子を使う

# [真のときの値 if 条件式 else 偽のときの値 for 任意の変数名 in イテラブルオブジェクト]

#%%
odd_even = ['odd' if i % 2 == 1 else 'even' for i in range(10)]
print(odd_even)
#['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# 上記と等価なfor文は以下の通り
#%%

odd_even = []
for i in range(10):
    if i % 2 == 1:
        odd_even.append('odd')
    else:
        odd_even.append('even')

print(odd_even)
#['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# 真のときの値, 偽のときの値に任意の変数名を使った式を記述することもできる

#%%
odd10 = [i * 10 if i % 2 == 1 else i for i in range(10)]
print(odd10)
#[0, 10, 2, 30, 4, 50, 6, 70, 8, 90]

# 上記と等価なfor文は以下の通り
#%%
odd10 = []
for i in range(10):
    if i % 2 == 1:
        odd10.append(i*10)
    else:
        odd10.append(i)

print(odd10)
#[0, 10, 2, 30, 4, 50, 6, 70, 8, 90]

# 4.ネストしたリスト内包表記
# forループをネストするように、複数のイテラブルオブジェクトを組み合わせることもできる。

#%%
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [x for row in matrix for x in row]
print(flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 上記と等価なfor文は以下の通り
#%%
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = []

for row in matrix:
    for x in row:
        flat.append(x)

print(flat)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]


#複数の変数を使うことも可能。
#%%
cells = [(row, col) for row in range(3) for col in range(2)]
print(cells)
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

# 上記と等価なfor文は以下の通り
#%%
# cells = []
# for row in range(3):
#     for col in range(2):
#         cells.append(row,col)

# print(cells)

# 5.辞書内包表記

# 辞書（dict型オブジェクト）も内包表記で生成できる。
# {}で囲み、式の部分でキーと値の2つをキー: 値のように指定する。

#%%
l = ['Alice', 'Bob', 'Charlie']

d = {s: len(s) for s in l}
print(d)
# {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# 上記と等価なfor文は以下の通り
#%%
l = ['Alice', 'Bob', 'Charlie']
d = {}
for s in l:
    d[s] = len(s)

print(d)
#{'Alice': 5, 'Bob': 3, 'Charlie': 7}

# キーと値それぞれのリストから新たな辞書を作成する場合は
# zip()関数を使う。

#%%
keys = ['k1', 'k2', 'k3']
values = [1, 2, 3]

d = {k: v for k, v in zip(keys, values)}
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

# 上記と等価なfor文は以下の通り
#%%
keys = ['k1', 'k2', 'k3']
values = [1, 2, 3]
d = {}

for k,v in zip(keys, values):
    d[k] = v

print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

# 6.ジェネレータ式
# リスト内包表記の角括弧[]を丸括弧()にした場合は
# タプルではなくジェネレータを返す。
# これをジェネレータ式（generator expression）という。

# ジェネレータ式を関数の唯一の引数とする場合は丸括弧()を省略できる。

#%%
print(sum([i**2 for i in range(5)]))
# 30

print(sum((i**2 for i in range(5))))
# 30

print(sum(i**2 for i in range(5)))
# 30

# タプル内包表記はないが、ジェネレータ式をtuple()の引数とすると
# 内包表記の書き方でタプルを生成することが可能。
#%%
t = tuple(i**2 for i in range(5))

print(t)
# (0, 1, 4, 9, 16)

print(type(t))
# <class 'tuple'>


# まとめ
# ①for文で書いていたものを内包表記に変更することでシンプルに記載し視認性の良い構文にできる
# ②リストだけでなく、集合や辞書にも使用可能
# ③()で囲むとジェネレータ式となるので、注意。メモリの消費を抑えることができる

