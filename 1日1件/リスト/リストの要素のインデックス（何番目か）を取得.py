## リストの要素のインデックス（何番目か）を取得
# Pythonのリスト（配列）の要素のインデックス、
# つまりその要素が何番目に格納されているかを取得する方法を説明する。

#1. リストの要素が重複していない場合: index()

# リストの要素が重複していない場合、index()メソッドを使う。
# index()の引数に調べたい値を指定すると0始まりのインデックスが取得できる。

#%%
l = list('abcde')
print(l)
# ['a', 'b', 'c', 'd', 'e']
print(l.index('a'))
# 0
print(l.index('e'))
# 4

# リストに含まれていない値を指定するとエラーValueErrorになるので注意

#%%
print(l.index('o'))
# ValueError: 'o' is not in list

# リストに含まれていない値に対して任意の値を返したい場合は、例えば以下のような関数を定義する。

#%%
def index_org(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

print(index_org(l, 'a'))
# 0
print(index_org(l, 'x'))
# False

#2. リストの要素が重複している場合: index(), enumerate(), リスト内包表記

# リストの要素が重複している場合、index()メソッドは最初のインデックスのみを返す。

#%%
l_dup = list('abcba')
print(l_dup)
# ['a', 'b', 'c', 'b', 'a']

print(l_dup.index('a'))
# 0

print(l_dup.index('b'))
# 1

# それで問題なければindex()をそのまま使えばいいが、
# すべてのインデックスをリストで取得したい場合は、
# 組み込み関数enumerate()とリスト内包表記を利用する。

#%%
print([i for i, x in enumerate(l_dup) if x == 'a'])
# [0, 4]

print([i for i, x in enumerate(l_dup) if x == 'b'])
# [1, 3]

# 要素が一つだけ含まれている場合もリストを返す。

#%%
print([i for i , x in enumerate(l_dup) if x == 'c' ])
# [2]

# リストに含まれていない値に対しては空のリストを返す。

#%%
print([i for i ,x in enumerate(l_dup) if x == 'x'])
# []

# 繰り返し使う場合は関数にしておくと便利

#%%
def index_multi(l, s, default=False):
    if s in l:
        return [i for i, x in enumerate(l) if x == s ]
    else:
        return default

print(index_multi(l_dup, 'a'))
# [0, 4]

print(index_multi(l_dup, 'c'))
# [2]

print(index_multi(l_dup, 'x'))
# False

# # まとめ
# # ①リストやタプルのイミュータブルオブジェクトの要素のインデクスを調べる場合は、index関数を使う
# # ②要素の重複がある場合や、要素がない可能性があるばあいには、関数を用意して内包表記で抽出するのがよい


