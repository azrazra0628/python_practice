# # リストはデータ構造の一つで、データを要素として登録できる。
# # 要素の数や肩に制限はない。

# 初期リストの作成
# [値, 値, …]

todo = [ 'プレゼン', '昼食' , ' 会議', ' メール対応' ]
print(todo)

# 空のリストも作成できる
# []

# リストはインデクスが使用可能。要素を取り出すことができる
# リスト[インデクス]

print(todo[0])

# リストはほかのリスト連結することができる
# リストの最後に追加される
# リストa + リストb

todo2 = ['営業']
todo += todo2
print(todo)

# 要素の追加はappendメソッドを使用する
# リスト.append(要素)

todo.append('定時退社')
print(todo)

# リストの途中に追加する場合にはincertメソッドを使用する
# リスト.insert(インデクス, 値)

todo.insert(1, 'PCチェック')
print(todo)

# 要素の変更はインデクスを使って、下記の書式で変更可能
# リスト[インデクス] = 値

todo[0] = '打合せ'
print(todo)


# 要素の削除はremoveメソッドを使用する
# リスト.remove(値)

todo.remove( ' 会議')
print(todo)

# 要素の個数を数えるときはlen関数を使用する
# len(リスト)

len(todo)

# リストの順番を任意で変更する
# リスト[インデクス]　= リスト[インデクス]
todo[0],todo[1] = todo[1],todo[0]
print(todo)


# # リストの要素の並び替え

# ①数値のリストの場合
# 最大値・最小値を取得: max(), min()

lst = [12, 23, 4, 9,56, -3]
print(max(lst))
print(min(lst))

# 最大値・最小値から順にn個の要素を取得: ソート
# くみこみ関数のsorted()を使用するか、sortメソッドを使用する

# sorted(リスト名, reverse=True)[:スライス]
# リスト名.sort(reverse=True)
# reverse=Trueは降順、reverse=Falseは昇順


lstd = sorted(lst, reverse=True)
print(lstd)
print(lstd[:3])


# 1行で書くと下記の通り

print(sorted(lst, reverse=True)[:3])


# # # 補足でリストの最大値、最小値から順に要素を取得する場合にはheapqモジュールを使うことも可能
# # # 元のリストの要素数に対して取得する個数が少ないときには、
# # # heapqモジュールを使ってソートしたほうが処理が早い

import heapq

# 最小値から順にn個の要素を取得したい場合
# heapq.nsmallest(n,リスト名)

# 最大値から順にn個の要素を取得したい場合
# heapq.nlargest(n,リスト名)

l = [3, 6, 7, -1, 23, -10, 18]
print(heapq.nlargest(3, l))

# リストの合計値を表示
# sum(リスト名)

print(sum(lst))





