## pprintの使い方（リストや辞書を整形して出力）

# Pythonの標準ライブラリであるpprintモジュールを使うと、
# リスト（list型）や辞書（dict型）などのオブジェクトをきれいに整形して出力・表示したり、
# 文字列（str型オブジェクト）に変換したりすることができる。
# pprintは「pretty-print」の略。

# リストや辞書ではなく長い文字列を整形（折り返し・省略）して
# 出力するにはtextwrapモジュールが便利。

#%%
import pprint

l = [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]}, 
     {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]},
     {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]

#1. pprintの基本的な使い方
#通常のprint()関数ではリストや辞書の要素が改行されることなく1行で出力される。

#%%
print(l)
# [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]}, {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]}, {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]

# pprint.pprint()を使うと、以下のようにリストの要素ごとに改行されて見やすくなる。

#%%
pprint.pprint(l)
# [{'Age': 40, 'Name': 'Alice XXX', 'Points': [80, 20]},
#  {'Age': 20, 'Name': 'Bob YYY', 'Points': [90, 10]},
#  {'Age': 30, 'Name': 'Charlie ZZZ', 'Points': [70, 30]}]

# どこで改行されるかは以下で説明する引数の設定によって決まる


#2. 出力幅（文字数）を指定: 引数width

# 出力する幅（文字数）を引数widthで指定できる。

# 1行が指定の文字数に収まるようにリストや辞書の要素で改行される。
# デフォルトはwidth=80。

#%%
pprint.pprint(l, width=40)
# [{'Age': 40,
#   'Name': 'Alice XXX',
#   'Points': [80, 20]},
#  {'Age': 20,
#   'Name': 'Bob YYY',
#   'Points': [90, 10]},
#  {'Age': 30,
#   'Name': 'Charlie ZZZ',
#   'Points': [70, 30]}]

# 大きい値を指定すると、改行が挿入されずprint()と同様の出力になる。

#%%
pprint.pprint(l,width=200)
# [{'Age': 40, 'Name': 'Alice XXX', 'Points': [80, 20]}, {'Age': 20, 'Name': 'Bob YYY', 'Points': [90, 10]}, {'Age': 30, 'Name': 'Charlie ZZZ', 'Points': [70, 30]}]

# 改行されるのはリストや辞書の要素ごとで、
# 辞書のキーkeyと値valueで改行されたり、数値の途中で改行されたりはしない。

#%%
pprint.pprint(l, width=1)
# [{'Age': 40,
#   'Name': 'Alice '
#           'XXX',
#   'Points': [80,
#              20]},
#  {'Age': 20,
#   'Name': 'Bob '
#           'YYY',
#   'Points': [90,
#              10]},
#  {'Age': 30,
#   'Name': 'Charlie '
#           'ZZZ',
#   'Points': [70,
#              30]}]

#3. 出力する要素の深さを指定: 引数depth

# 出力する要素の深さを引数depthで指定できる。ここでいう深さは入れ子になったデータの深さのこと。
# 指定した値より深い要素は省略記号...で出力される。

#%%
pprint.pprint(l,depth=1)
# [{...}, {...}, {...}]

pprint.pprint(l,depth=2)
# [{'Age': 40, 'Name': 'Alice XXX', 'Points': [...]},
#  {'Age': 20, 'Name': 'Bob YYY', 'Points': [...]},
#  {'Age': 30, 'Name': 'Charlie ZZZ', 'Points': [...]}]

#4. インデント幅を指定: 引数indent

# インデント幅を引数indentで指定できる。デフォルトはindent=1。

#%%
pprint.pprint(l,indent=4,width=20)
# [   {   'Age': 40,
#         'Name': 'Alice '
#                 'XXX',
#         'Points': [   80,
#                       20]},
#     {   'Age': 20,
#         'Name': 'Bob '
#                 'YYY',
#         'Points': [   90,
#                       10]},
#     {   'Age': 30,
#         'Name': 'Charlie '
#                 'ZZZ',
#         'Points': [   70,
#                       30]}]

#5. 改行を最小限にする: 引数compact

# 引数compactをTrueとすると出力幅widthに収まらない分だけが改行される。
# 要素数の多いリストなどがある場合はcompact=Trueのほうが見やすい。

#%%
l_long = [list(range(10)), list(range(100, 110))]

pprint.pprint(l_long,width=40,compact=True)
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [100, 101, 102, 103, 104, 105, 106,
#   107, 108, 109]]

#6. 文字列に変換: pprint.pformat()
# 辞書やリストはstr()で文字列（str型）に変換できる。

# この場合、通常のprint()関数での出力のように
# リストや辞書の要素が改行されることなく1行の文字列となる。

#%%
s_normal = str(l)
print(s_normal)
# [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]}, {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]}, {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]

#%%
s_pp = pprint.pformat(l)
print(s_pp)
# [{'Age': 40, 'Name': 'Alice XXX', 'Points': [80, 20]},
#  {'Age': 20, 'Name': 'Bob YYY', 'Points': [90, 10]},
#  {'Age': 30, 'Name': 'Charlie ZZZ', 'Points': [70, 30]}]

# pprint.pformat()の引数はpprint.pprint()と共通。


#7. 例: 二次元配列（リストのリスト）を整形して表示

# pprintは二次元配列（リストのリスト）を表示する場合に使うと便利。

# 通常のprint()関数だと見にくいが、pprintを使うと見やすい。

#%%
l_2d = [list(range(10)), list(range(10)), list(range(10))]

print(l_2d)
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

pprint.pprint(l_2d)
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

# まとめ
# ①pprintモジュールのpprint関数を使用することで、視認性を良くすることができる
# ②二次元配列などはpprintを使用するとすっきりする

