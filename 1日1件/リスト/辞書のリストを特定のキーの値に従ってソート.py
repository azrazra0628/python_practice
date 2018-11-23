## 辞書のリストを特定のキーの値に従ってソート

# Pythonで共通のキーを持つ辞書を要素とするリストをsort()メソッド
# やsorted()関数でソートしようとすると、
# デフォルトではエラーTypeErrorになってしまう。

# sort()メソッドやsorted()関数の引数keyを指定することで
# 辞書のリストを特定のキーの値に従ってソートできる。

#%%
import pprint

l = [{'Name': 'Alice', 'Age': 40, 'Point': 80}, 
     {'Name': 'Bob', 'Age': 20},
     {'Name': 'Charlie', 'Age': 30, 'Point': 70}]

#1. デフォルトでは辞書のリストをソートするとエラー

# 辞書（dict型オブジェクト）のリストをsort()メソッドや
# sorted()関数でソートしようとすると
# 、デフォルトではエラーTypeErrorになってしまう。
# これは辞書オブジェクトの大小比較（<や>などでの演算）がサポートされていないため。

#%%
l_sorted = sorted(l)
# TypeError: '<' not supported between instances of 'dict' and 'dict'

#2. 引数keyに無名関数（ラムダ式）を指定

# 辞書のリストを特定のキーの値に従ってソートしたい場合は、
# sort()メソッドやsorted()関数の引数keyを指定する。

# keyには、ソートされる（各要素が比較される）前にリストの各要素に適用される関数を指定する。
# keyに指定した関数の結果に従ってソートされる。

#%%
l.sort(key=lambda x: x['Age'])

pprint.pprint(l)
# [{'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

l.sort(key=lambda x: x['Name'])
pprint.pprint(l)
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70}]

#3. 共通のキーを持たない要素が存在する場合

# 上で示した方法だと、共通のキーを持たない要素が存在する場合にエラーとなる。

#%%
l.sort(key=lambda x: x['Point'])
# KeyError: 'Point'

# そのような場合は、存在しないキーに対しても値を取得できる辞書のget()メソッドを使う。
# 第二引数に存在しないキーに対して返す値を指定できる。
# キーが存在しない要素は第二引数に指定した値に置き換えられてソートされる。

#%%
l.sort(key=lambda x: x.get('Point', 0))

pprint.pprint(l)
# [{'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

#%%
l.sort(key=lambda x: x.get('Point', 100))

pprint.pprint(l)
# [{'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 20, 'Name': 'Bob'}]

#4. 引数reverseで降順・昇順を指定

# 降順・昇順は引数reverseで指定する。

#%%
l.sort(key=lambda x: x.get('Age'),reverse=True)
pprint.pprint(l)
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 20, 'Name': 'Bob'}]

#5. sort()メソッドでもsorted()関数でも同様

#%%
l_sorted = sorted(l,key=lambda x: x['Age'],reverse=False)
pprint.pprint(l_sorted)
# [{'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

# まとめ
# ①辞書のキーの値によってsortする場合には、ラムダ関数でkeyを指定してソートする
# ②sortメソッドでもsorted関数でも同様

