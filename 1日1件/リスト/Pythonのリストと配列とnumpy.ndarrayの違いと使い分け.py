# Pythonのリストと配列とnumpy.ndarrayの違いと使い分け

# Pythonには、組み込み型としてリストlist、標準ライブラリに配列arrayが用意されている。
# さらに数値計算ライブラリNumPyをインストールすると多次元配列numpy.ndarrayを使うこともできる。

#1. リストと配列とnumpy.ndarrayの違い

# リスト - list
# 組み込み型
# 何もimportせずに使える
# 異なる型を格納できる
# リストのリストによって多次元配列を表現することも可能
# 厳密には配列と異なるが、配列ライクな簡単な処理を行うのであればリストlistで十分な場合が多い

l = ['apple', 100, 0.123]
print(l)
# ['apple', 100, 0.123]

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(l_2d[1][1])
# 4

# 組み込み関数のmax(), min(), sum(), len()を使って、
# 最大値や最小値、合計、平均などを算出する例。len()は要素数を返す関数。

#%%
l_num = [0, 10, 20, 30]

print(min(l_num))
# 0
print(max(l_num))
# 30
print(sum(l_num))
# 60
print(len(l_num))
# 4

# for文によるループ処理の例。
#%%
l_str = ['apple','orange', 'banana']

for i in l_str:
    print(i)
# apple
# orange
# banana

# 配列 - array
# 標準ライブラリのarrayモジュールをimportして使う
# 8.7. array — 効率のよい数値アレイ — Python 3.6.5 ドキュメント
# 同じ型しか格納できない
# 一次元配列のみ
# 型に制限がある以外はリストと同様の処理が可能

# 型コードと一致しない型の要素は格納できない。

#%%
import array

arr_int = array.array('i', [0, 1, 2])
print(arr_int)
# array('i', [0, 1, 2])

arr_float = array.array('f', [0.0, 0.1, 0.2])
print(arr_float)
# array('f', [0.0, 0.10000000149011612, 0.20000000298023224])

arr_int = array.array('i', [0, 0.1, 2])
#TypeError: integer argument expected, got float

# リストと同様の処理が可能。

#%%
print(arr_int[1])
# 1

print(sum(arr_int))
# 3

# 多次元配列 - numpy.ndarray

# NumPyをインストール、importして使う
# 同じ型しか格納できない
# object型で様々な型へのポインタを格納することはできる
# 関連記事: NumPyのデータ型dtype一覧とastypeによる変換（キャスト）
# 多次元配列を表現できる
# 数値計算のためのメソッド・関数が豊富で、高速な演算が可能
# 行列演算や画像処理など様々な場面で使える


#%%
import numpy as np

arr = np.array([0, 1, 2])
print(arr)
# [0 1 2]

arr_2d = np.array([[0, 1, 2], [3, 4, 5]])
print(arr_2d)
# [[0 1 2]
#  [3 4 5]]

#%%
arr_2d_sqrt = np.sqrt(arr_2d)
print(arr_2d_sqrt)
# [[0.         1.         1.41421356]
#  [1.73205081 2.         2.23606798]]

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

arr_product = np.dot(arr_1, arr_2)
print(arr_product)
# [[ 9 12 15]
#  [19 26 33]]

