##Pythonでリストをソートするsortとsortedの違い

# Pythonでリストを昇順または降順にソートするにはsort()とsorted()の2つの方法がある。文字列やタプルをソートしたい場合はsorted()を使う。

# ここでは以下の内容について説明する。

# 1,リスト型のメソッドsort(): 元のリストをソート

# もとのリストが書き換えられる

#%%
sample_list = [1,3,5,2,4]
sample_list.sort()
print(sample_list)
##[1, 2, 3, 4, 5]

# sort()が返すのはNoneなので注意。

#%%
print(sample_list.sort())
#None

#デフォルトは昇順。降順にソートしたい場合は引数reverseをTrueとする。

#%%
sample_list.sort(reverse=True)
print(sample_list)
#[5, 4, 3, 2, 1]

##組み込み関数sorted(): ソートした新たなリストを生成

# 引数にソートしたいリストを指定するとソートされたリストを返す。元のリストは変更されない非破壊的処理。

#%%
sample_list = [1,3,5,2,4]
new_list = sorted(sample_list)
print(new_list)
#[1, 2, 3, 4, 5]
print(sample_list)
#[1, 3, 5, 2, 4]  ←そのまま

# sorted()が返すのは、変更後
#%%
print(sorted(sample_list))
#[1, 2, 3, 4, 5]


# 文字列、タプルをソートする方法

# 文字列、タプルはイミュータブル（更新不可）なので、元のオブジェクトを書き換えるsort()メソッドは用意されていない。

# 一方、ソートしたリストを新たなオブジェクトとして生成するsorted()関数の引数にはリストだけでなく文字列やタプルも指定できる。
# ただし、sorted()が返すのはリストなので、文字列やタプルに変換する処理が必要となる。

#%%
sample_str = 'abdec'
new_str = sorted(sample_str)
print(sample_str)
#abdec
print(new_str)
#['a', 'b', 'c', 'd', 'e']  ←リストになってしまう

#文字列のリストを連結して一つの文字列にするにはjoin()メソッドを使う。

#%%
sample_str = 'abdec'
new_str = ''.join(new_str) #文字列に変換
print(new_str)
#abcde  

# joinメソッドの使い方
#'間に挿入する文字列'.join([連結したい文字列のリスト])
#%%
satoshi = ''.join(['sa','to','shi'])
print(satoshi)

# まとめて書いてもOK。降順にソートしたい場合は引数reverseをTrueとする。
#%%
org_str = 'abdec'
new_str = ''.join(sorted(org_str))
print(new_str)
# abcde

new_str_reverse = ''.join(sorted(org_str, reverse=True))
print(new_str_reverse)
# edcba

# タプルのソート
# タプルについても文字列と同様。
# sorted()関数の引数にタプルを指定すると、要素がソートされたリストが返される。

#%%
org_tuple = (3, 1, 4, 5, 2)

new_tuple_list = sorted(org_tuple)
print(org_tuple)
# (3, 1, 4, 5, 2)
print(new_tuple_list)

# [1, 2, 3, 4, 5]

# リストからタプルへの変換はtuple()を使う。
#%%
new_tuple = tuple(new_tuple_list)
print(new_tuple)
# (1, 2, 3, 4, 5)


# まとめて書いてもOK。降順にソートしたい場合は引数reverseをTrueとする。

#%%
new_tuple = tuple(sorted(new_tuple_list))
print(new_tuple)
# (1, 2, 3, 4, 5)

new_tuple_reverse = tuple(sorted(new_tuple_list, reverse=True))
print(new_tuple_reverse)
# (5, 4, 3, 2, 1)


# まとめ
# 1,sortを使うと、元のリストまで変更されてしまう、sortedを使えば変更されない
# 2,リスト以外ではsoredメソッドを使用する。一度リストになってしまうので、変換が必要　（文字列　→　リスト　→　文字列)

# 練習問題
# ランダムに出力された10個の数字を昇順,降順で表示する

#%%
import random

org_list = []
for i in range(10):
    org_list.append(random.randint(1,100))
print(org_list)

print(sorted(org_list))
print(sorted(org_list,reverse=True))

# ランダムに出力された文字列を昇順,降順で表示する

#%%
import random, string

def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

org_str = randomname(10)
print(org_str)

new_str = ''.join(sorted(org_str))
print(new_str)




