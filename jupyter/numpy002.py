##2## ベクトル・行列の演算


##1-1ベクトルの結合

# 四則演算ではなくravel関数を使用する
# 変数 = np.ravel([ベクトル1, ベクトル2, …])

#%%
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([5, 8, 13])
arr3 = arr1 + arr2 #ベクトルの各要素毎に値を加算する
arr4 = np.ravel([arr1, arr2]) #ベクトル同士を結合し、1つにまとめる
print(arr3)
print(arr4)

##2-1ベクトルの内積・外積
#内積とは
#2本のベクトルに対してスカラーを対応させる演算
#外積とは
#2本のベクトルに対してベクトルを対応させる演算

#ベクトルの内積計算
# 変数 = np.inner(ベクトル1, ベクトル2)

#ベクトルの外積計算
# 変数 = np.outer(ベクトル1, ベクトル2)

#%%
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([5, 8, 13])
arr3 = np.inner(arr1, arr2)
arr4 = np.outer(arr1, arr2)
print(arr3)
print(arr4)

##3-1行列の四則演算

#%%
import numpy as np

arr1 = np.matrix([[1, 2, 3],
                    [5, 8, 13],
                    [21, 34, 55]])

arr2 = np.identity(3)

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr2 / arr1)


#ndarrayだと以下の通り

#%%
import numpy as np

arr1 = np.array([[1, 2, 3],
                 [5, 8, 13],
                    [21, 34, 55]])

arr2 = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr2 / arr1)


#加算・減算・除算はndarrayとmatrixで差異ないが、乗算については
#matrixでは行列の積になるのに対し、ndarrayでは各要素を単純に掛け算して、行列にするだけ

##4-1行列の積

# 行列の積の求め方
# 変数 = np.dot(行列1, 行列2)

# 行列のテンソル積の求め方
# 変数 = np.outer(行列1, 行列2)

#ndarrayでもmatrixでも使用可能

#テンソル積
#outer関数ですべての要素を乗算する

#%%
import numpy as np


arr1 = np.matrix([[1, 2, 3],
                [5, 8, 13],
                [21, 34, 55]])
arr2 = np.matrix([[2, 1, 1],
                [1, 3, 1],
                [1, 1, 4]])
arr3 = np.dot(arr1, arr2)
arr4 = np.outer(arr1, arr2)
print(arr3)
print(arr4)



##5-1行列の結合

# 結合を行う場合には「水平か,垂直か」を考慮する必要がある

#水平結合
# 変数 = np.hstack([行列1, 行列2, …])

#垂直結合
# 変数 = np.vstack([行列1, 行列2, …])

#結合する面の要素数を一致させる必要がある

#%%
import numpy as np

arr1 = np.matrix([[1, 2, 3],
                [5, 8, 13],
                [21, 34, 55]])
arr2 = np.identity(3)

print(np.hstack([arr1, arr2]))
print(np.vstack([arr1, arr2]))

##5-2複数行列結合

# 変数 = np.bmat(行列の行列)

#%%
import numpy as np

arr1 = np.matrix([[1, 2, 3],
                [5, 8, 13],
                [21, 34, 55]])
arr2 = np.identity(3)
print(np.bmat([[arr1,arr2],
                [arr2,arr1]]))


##6-1行列の分割

#行列を縦もしくは横に分割する関数

#垂直分割
# 変数 = np.vsplit(行列, 分割数)

#水平分割
# 変数 = np.hsplit(行列, 分割数)

#変数に代入する場合には、変数をタプルとして値を用意しておく


#%%
import numpy as np

arr1 = np.arange(16).reshape(4, 4)
(v1, v2) = np.vsplit(arr1, 2)
(h1, h2) = np.hsplit(arr1, 2)
print(arr1)
print()
print(v1)
print(v2)
print(h1)
print(h2)


##7-1総和の計算

#行列の要素の総和を考えるときには「すべての総和か」「縦もしくは横方向の総和か」
#考える必要があるが、sum関数を1つの関数で処理可能

#総和
# 変数 = np.sum(行列, axis= 方向)
# or 
# 変数 = 行列.sum(axis= 方向)
#  方向は0 = 縦　、1 = 横に総和する
#  引数axisを指定しなければ、行列の要素の総和となる

#%% 
import numpy as np

arr1 = np.arange(16).reshape(4, 4)

print(arr1)
print()
print(arr1.sum())
print(np.sum(arr1,axis=0))
print(np.sum(arr1,axis=1))

#8-1最大値・最小値

# 基本的にはsum関数と同じ使い方

# 最大値
# 変数 = np.max(行列, axis=方向)
# 変数 = 行列.max(axis=方向)

# 最小値
# 変数 = np.min(行列, axis=方向)
# 変数 = 行列.min(axis=方向)


#%%
import numpy as np

arr1 = np.arange(16).reshape(4, 4)

print(arr1)
print()
print(arr1.min())
print(np.min(arr1,axis=0))
print(np.min(arr1,axis=1))
print(arr1.max())
print(np.max(arr1,axis=0))
print(np.max(arr1,axis=1))


##9-1統計計算

# 多量のデータを扱い場合に統計計算は必須

# 平均
# 変数 = np.mean(行列, axis=方向)
# 変数 = 行列.mean(axis=方向)

# 中央値
# 変数 = np.median(行列, axis=方向)
# 変数 = 行列.median(axis=方向)

# median関数のみaxisによる方向指定が必須

# 分散
# 変数 = np.var(行列, axis=方向)
# 変数 = 行列.var(axis=方向)

# 標準偏差
# 変数 = np.std(行列, axis=方向)
# 変数 = 行列.syd(axis=方向)


#%%
import numpy as np

arr1 = np.array(np.random.randint(0, 100, (10, 10)))

print(arr1)
print()
print('平均:'+str(np.mean(arr1)))
print('平均:'+str(np.mean(arr1, axis=0)))
print('平均:'+str(np.mean(arr1, axis=1)))
print('中央:'+str(np.median(arr1, axis=0)))
print('中央:'+str(np.median(arr1, axis=1)))
print('分散:'+str(np.var(arr1)))
print('分散:'+str(np.var(arr1, axis=0)))
print('分散:'+str(np.var(arr1, axis=1)))
print('標準偏差:'+str(np.std(arr1)))
print('標準偏差:'+str(np.std(arr1, axis=0)))
print('標準偏差:'+str(np.std(arr1, axis=1)))


##9-2乱数とrandomモジュール

# numpyにはrandomモジュールが用意されている

# 整数の乱数行列の作成
# 変数 = np.random.randint(下限, 上限,(行数, 列数))


#%%
import numpy as np

arr1 = np.array(np.random.randint(0, 100, (10, 10)))

print(arr1)

##10-1 linalgについて

# linear algebra(線形代数)の略.

## 一一般的な積の計算
#積(ドット積)
# 変数 = np.linalg.dot(値1,値2)

# 積(多要素の積)
# 変数 = np.linalg.multi_dot([値1, 値2, …])

# ベクトル積
# 変数 = np.linalg.vdot(値1, 値2)

# 内積
# 変数 = np.linalg.inner(値1, 値2)

# 外積
# 変数 = np.linalg.outer(値1, 値2)

#上記はnumpyにあるものとlinalgで結果は相違ない

#行列のべき乗
# 変数 = np.linalg.matrix_power(行列, べき数)

#%%

import numpy as np

arr1 = np.matrix([[1,2,3],
                    [5,8,13],
                    [21,34,55]])
re0 = np.linalg.matrix_power(arr1,0)
re1 = np.linalg.matrix_power(arr1,1)
re2 = np.linalg.matrix_power(arr1,2)
print(re0)
print(re1)
print(re2)



#10-2 逆行列と行列式
# linalgには行列関係の重要な処理が関数としてまとめられている

# 逆行列
# 変数 = np.linalg.inv(行列)

# 行列式
# 変数 = np.linalg.det(行列)

#%%
import numpy as np
arr1 = np.matrix([[0, 1, 2],
                    [3, 5, 8],
                    [21, 34, 55]])

print(np.linalg.inv(arr1))
print(np.linalg.det(arr1))





