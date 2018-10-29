###1,numpy 基本
#numpyの特徴は多次元配列によるベクトルや行列の処理。

##1-1  ベクトルの作成

#必ず全体をリストでまとめて記述する
#変数 = np.array(リスト)

#%%
#下記のように別名のnpでインポートしておく
import numpy as np
arr = np.array([10,20,30.])
print(arr)

##1-2 等差数列の作成

#ステップ数で作成
# いくつずつ増加するかを指定する
# 変数 = np.arange(開始数, 終了数, ステップ)

#　分割数で作成
# 範囲内をいくつに分割するかを指定する
# 変数 = np.linspace(開始数, 終了数, 分割数)

#均等分割と一定数での増加では上限の取り扱いが異なることに注意
#一定数での増加 →　終了値は含まれない
#均等分割　→　終了値も含まれる

#%%
import numpy as np
arr1 = np.arange(0, 100, 20)
arr2 = np.linspace(0, 100, 5)
print(arr1)
print(arr2)

##2-1 ベクトルと数値の演算

#専用のメソッドを使用しなくても、四則演算は可能

#%%
import numpy as np

arr1 = np.array([1,2,3,5,8])
print(arr1)
print(arr1+10)
print(arr1-10)
print(arr1*2)
print(arr1/2)
print(arr1%2)

##3-1 ベクトル同士の演算

#ベクトル同士の演算の場合、ndarrayではベクトルの各値同士が演算される
#%%
import numpy as np

arr1 = np.array([1,2,3,5])
arr2 = np.array([8,13,21,34])
print(arr1+arr2)
print(arr2-arr1)
print(arr2*arr1)
print(arr2/arr1)
print(arr2%arr1)

##4-1 行列の作成


# matrixの作成
# 変数 = np.matrix(2次元リスト)

#%%
import numpy as np
arr1 = np.matrix([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
print(arr1)

##4-2単位行列の作成

#正方の単位行列の作成
#引数に指定した数値を一辺とした正方行列を作成
#変数 = np.identity(要素数)


#%%
arr1 = np.identity(3)
arr2 = np.identity(10)
print(arr1)
print(arr2)

##4-3非正方の単位行列

#非正方の単位行列の作成
#変数 = np.eye(行数, 列数, オフセット)
#オフセットはずれ幅

#%%
arr1 = np.eye(5,7,0)
arr2 = np.eye(5,7,2)
print(arr1)
print(arr2)

##5-1対角行列

#対角行列の作成
#変数 = np.diag(リスト)
#リストには行列に配置する値をまとめたものを用意し、主対角線上の要素に設定される

#%%
arr1 = np.diag([1,2,3])
arr2 = np.diag([3,5,8,13,21])
print(arr1)
print(arr2)

##6-1ベクトル⇔行列変換

#ベクトルから行列への変換
#変数 = [ndarray].reshape((行数, 列数))
#reshapeを実施する際には、元になるベクトルと、変換後に作成される行列で要素の数がイコールでないといけない

#%%
arr1 = np.array([1,2,3,5,8,13,21,34,55])
arr2 = arr1.reshape((3,3))
print(arr1)
print(arr2)

#行列からベクトルに変換
# 変数 = np.ravel([matrix])

#%%
import numpy as np

arr1 = np.diag([1,2,3,5])
arr2 = np.ravel(arr1)
print(arr1)
print(arr2)


##7-1転置について

#専用のメソッドなどは使用せず、作成したmatrix値のTプロパティの値の取り出しによって実現

#%%
import numpy as np

arr1 = np.array([1,2,3,5,8,13,21,34,55])
arr2 = arr1.reshape((3,3))
print(arr1)
print(arr2)
print(arr2.T)





