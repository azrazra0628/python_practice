## enumerateの使い方: リストの要素とインデックスを取得

#1. forループでインデックスを取得できるenumerate関数

# enumerate()関数を使うと、forループの中でリスト（配列）などの
# イテラブルオブジェクトの要素と同時にインデックス番号（カウント、順番）を取得できる

# 通常のforループ

#%%
l = ['Alice', 'Bob', 'Charlie']

for i in l:
    print(i)
# Alice
# Bob
# Charlie

# enumerate関数を使ったforループ
# 引数にリストなどのイテラブルオブジェクトを指定する。

#%%

l = ['Alice', 'Bob', 'Charlie']

for i, name in enumerate(l):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie

# インデックス番号, 要素の順に取得できる。

#2. enumerate関数のインデックスを1から開始
# デフォルトでインデクス番号は０から始まる
# インデクスを1から開始したいときは、enumerate()関数の第二引数に
# 開始インデクスを数値を指定する

#%%
l = ['Alice', 'Bob', 'Charlie']

for i, name in enumerate(l, 1):
    print(i, name)
# 1 Alice
# 2 Bob
# 3 Charlie

#3. 増分（step）を指定
# 増分stepを指定する引数はないが、以下の方法で実現可能

#3づつ増やしたい場合
#%%
l = ['Alice', 'Bob', 'Charlie']
step = 3

for i, name in enumerate(l, 1):
    print(i * 3,name)
# 3 Alice
# 6 Bob
# 9 Charlie


まとめ
# ①リストのfor文を回すときにインデクスも併せて出力したい場合にenumerate関数が便利


