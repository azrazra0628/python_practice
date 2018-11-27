## 複数のリストに共通する・しない要素とその個数を取得

# Pythonで複数のリスト（配列）から共通する要素・共通しない要素を抽出し、
# その個数をカウントする。各リストを集合型setに変換し集合演算を行う。

#%%
l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']
l3 = ['c', 'd', 'e']

#1. 複数のリストから共通する要素とその個数を取得

# 共通部分は&演算子で取得できる。

#%%
l1_l2_and = set(l1) & set(l2)
print(l1_l2_and)
# {'b', 'c'}

print(type(l1_l2_and))
# <class 'set'>

# リストlist型に変換したい場合はlist()を使う。

#%%
l1_l2_and = list(l1_l2_and)
print(l1_l2_and)
# ['b', 'c']

# 個数はlen()で取得可能。

#%%
print(len(l1_l2_and))
# 2

# 3個以上の場合も同様。

#%%
l1_l2_l3_and =  list(set(l1) & set(l2) & set(l3))
print(l1_l2_l3_and)
# ['c']

#2. 複数のリストから共通しない要素とその個数を取得

# 対称差集合（二つの集合のどちらか一方にのみ含まれる要素の集合）は^演算子で取得できる。

#%%
l1_l2_sym_diff = list(set(l1) ^ set(l2))
print(l1_l2_sym_diff)
# ['d', 'a']

# 元のリストが3個の場合に^演算子を使うと、すべてのリストに共通する要素も含まれる。

#%%
l1_l2_l3_sym_diff = list(set(l1) ^ set(l2) ^ set(l3))
print(l1_l2_l3_sym_diff)
# ['e', 'a', 'c']

# 各リストに一つだけ含まれる要素を抽出したい場合は
# 、すべてのリストを連結したリストの要素から個数が1個のものを抽出する。
# リスト内包表記およびリストから要素の個数を取得するメソッドcount()を使う。

#%%
l_all = l1 + l2 + l3
print(l_all)
# ['a', 'b', 'c', 'b', 'c', 'd', 'c', 'd', 'e']

l1_l2_l3_sym_diff = [x for x in l_all if l_all.count(x) == 1]
print(l1_l2_l3_sym_diff)
# ['a', 'e']

# なお、この方法だと元のリストが重複する要素を持っていた場合、その要素も除外される。

#%%
l1_duplicate = ['a', 'a', 'b', 'c']

l_duplicate_all = l1_duplicate + l2 + l3
l_duplicate_all_only = [x for x in l_duplicate_all if l_duplicate_all.count(x) == 1]
print(l_duplicate_all_only)
# ['e']

# 最初に各リストごとに重複した要素を削除してユニークな要素のみのリストにしてから処理すれば、
# 各リストにのみ含まれる要素を抽出可能。

#%%
l_unique_all = list(set(l1_duplicate)) + list(set(l2)) + list(set(l3))
print(l_unique_all)
# ['a', 'b', 'c', 'd', 'b', 'c', 'd', 'e', 'c']

l_all_only = [i for i in l_unique_all if l_unique_all.count(i) == 1]
print(l_all_only)
# ['a', 'e']

#3. 複数のリストからユニークな要素とその個数を取得

# 複数のリストから重複を取り除きユニークな（一意な）要素を抽出したい場合は、
# リストをすべて足し合わせてから集合set()型に変換する。

#%%
l1_l2_or = set(l1 + l2)
l1_l2_or = list(l1_l2_or)
print(l1_l2_or)
# ['d', 'a', 'b', 'c']

# まとめ
# ①複数のリストから重複・一意・共通の値を取得する場合には、一度集合にしてから各演算子を使用する
# ②3つ以上のリストで一意な値を取得する場合には、演算子での取得ができないので注意


