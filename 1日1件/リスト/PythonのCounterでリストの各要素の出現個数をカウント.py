##PythonのCounterでリストの各要素の出現個数をカウント

# Pythonでリストやタプルの全要素の個数は組み込み関数len()
# 、各要素の個数（要素ごとの出現回数）はcount()メソッドで取得できる。

#1.全要素数をカウント: len()
変数 = len(リストやタプル、文字列)

#　リスト
#%%
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
print(len(l))
#7


# 文字列
#%%
str = 'abcde'
print(len(str))

#2.各要素の個数（要素ごとの出現回数）をカウント: count()メソッド

# 変数.count(要素)
# 要素として存在しない値を引数に渡すと0が返る。


#%%
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
print(l.count('a'))
# 4
print(l.count('b'))
# 1
print(l.count('c'))
# 2
print(l.count('d'))
# 0

#3.各要素の出現回数を一括で　取得：collectionsモジュールのCounterクラス

# import collections
# 変数 = collections.Counter(リスト,タプル,文字列)

#%%
import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)

print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})

# 生成されたcounterオブジェクトに要素をしてするとその個数を取得できる

#%%
print(c['a'])
# 4

print(c['b'])
# 1

print(c['c'])
# 2

print(c['d'])
# 0

# キーのリスト（keys()メソッド）、値のリスト（values()）、
# キーと値のペアのタプルのリスト（items()メソッド）を取得したりできる。

#%%
print(c.keys())
# dict_keys(['a', 'b', 'c'])

print(c.values())
# dict_values([4, 1, 2])

print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])

# 出現回数順に要素を取得: most_common()メソッド

# Counterにはmost_common()メソッドがあり、
# (要素, 出現回数)という形のタプルを出現回数順に並べたリストを返す。

#%%
print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)]

# 出現回数の少ない順に並べ替えたい場合は増分を-1としたスライスを使う。
#%%
print(c.most_common()[::-1])

# メソッドに引数nを指定すると
# 出現回数の多いn要素のみを返す。省略するとすべての要素。

#%%
print(c.most_common(2))

#3.重複しない要素（一意な要素）の個数（種類）をカウント

# 集合型setのコンストラクタset()を使用

#%%
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
print(set(l))


#4.条件を満たす要素の個数をカウント
# 条件を満たす要素のリストをリスト内包表記で生成して
# 、その個数をlen()で取得する

#%%
l = list(range(-5, 6))

print(l)
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

print([i for i in l if i < 0])
# [-5, -4, -3, -2, -1]

print(len([i for i in l if i < 0]))
# 5

print([i for i in l if i % 2 == 1])
# [-5, -3, -1, 1, 3, 5]

print(len([i for i in l if i % 2 == 1]))
# 6

文字列のリストに対する条件も可能
#%%

l = ['apple', 'orange', 'banana']
print([s for s in l if s.endswith('e')])
#['apple', 'orange']

print(len([s for s in l if s.endswith('a')]))
#1

# 出現回数の条件でカウントする場合、
# 目的によってcount()メソッドとcollections.Counterを使い分ける。
# 出現回数が条件を満たす要素の種類をカウントする場合は
# collections.Counterを使う。

# リスト内の要素で2回以上出現する要素をすべて抽出し、その回数を表示
#%%
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
print([i for i in l if l.count(i) >= 2])
#['a', 'a', 'a', 'a', 'c', 'c']

print(len([i for i in l if l.count(i) >= 2]))
#6

# リスト内の要素で2回以上出現する要素を抽出し、その個数を表示
#%%
import collections
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)

print([i[0] for i in c.items() if i[1] >= 2])
#['a', 'c']

print(len([i[0] for i in c.items() if i[1] >= 2]))
#2

# 内包表記を使用しないとこんな感じ
#%%
import collections
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)

ans = []
for i in c.items():
    if i[1] >= 2:
       ans.append(i[0]) 
print(ans)
#['a', 'c']

print(len(ans))

#5.文字列の単語の出現個数をカウント
# 文字列に登場する単語の出現個数を数えてみる。

# まず、不必要なカンマ,や.をreplace()メソッドで空文字列と置換し、削除する。
# さらにsplit()メソッドで空白で区切ってリスト化する。

#%%
s = 'government of the people, by the people, for the people.'
print(s)
#government of the people, by the people, for the people.

s_remove = s.replace(',','').replace('.','')
print(s_remove)
#government of the people by the people for the people

word_list = s_remove.split()
print(word_list)
#['government', 'of', 'the', 'people', 'by', 'the', 'people', 'for', 'the', 'people']

#リスト化できれば以後は今までと同様にcountメソッドやmost_common()メソッドを使用する

#%%
print(word_list.count('people'))
#3

print(len(set(word_list)))
#6

c = collections.Counter(word_list)
print(c)
#Counter({'the': 3, 'people': 3, 'government': 1, 'of': 1, 'by': 1, 'for': 1})

print(c.most_common()[0][0])
#the

#文字列の文字の出現個数をカウント
# 文字列もシーケンス型なので、count()メソッドを使ったり、
# collections.Counter()のコンストラクタの引数に渡したりすることができる。

#%%
s = 'supercalifragilisticexpialidocious'
print(s.count('p'))
#2
c = collections.Counter(s)
print(c)
#Counter({'i': 7, 's': 3, 'c': 3, 'a': 3, 'l': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'o': 2, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1})\

# 出現回数の多い順トップ5で並べる方法
print(c.most_common(5))
#[('i', 7), ('s', 3), ('c', 3), ('a', 3), ('l', 3)

#### まとめ #####
リスト・タプルともにcountメソッドやmost_commonメソッドを使用して、出現回数を取得可能
リスト内包表記により、条件に当てはまる要素の抽出も可能





