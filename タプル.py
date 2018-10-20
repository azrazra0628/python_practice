#タプル
item = ('blue', 'hat')
item

#リストの場合には要素の追加とかができるがタプルはできない
item = ['blue', 'hat']
item

#実は（）で括らなくてもタプルは作成可能（明示的にタプルだとわかりやすくするため
item2 = 'red', 'shirt'
item2

#アンパック  タプルから要素を取り出して複数の変数に代入可能
color, name = item2
color
name

#タプルのリスト 
catalog = [('blue', 'hat'), ('red', 'shirt')]
catalog


#上記と一緒
item = ('blue', 'hat')
item
item2 = 'red', 'shirt'
item2
catalog = [item, item2]
catalog

catalog[1]
catalog[1][1]