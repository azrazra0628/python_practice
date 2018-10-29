##4 numpy 補足 ##

##1-1 numpyのバージョン確認

# 使用中のnumpyのバージョン情報を確認する
#print(np.__version__)

##1-2 numpyのコンフィギュレーションを確認する

# np.show_config()
# どの行列ライブラリを使用しているか確認できる

##1-3 データサイズの確認

# 行列.itemsize * 行列.size

#%%
import numpy as np
arr1 = np.arange(10000)
print(arr1.itemsize * arr1.size)


#2-1 0以外の要素の抽出

# 0以外の要素のインデクスを表示する
#行列.nonzero()
#np.nonzero(行列)

#どちらでも同じ結果が取得可能

#%%
a = np.random.randint(0, 10, size=20)
print(a)
print(a.nonzero())


#3-1パディングについて

# pad関数を使用することで、ベクトルや行列に任意の個数要素を追加することができる

# パディング(ベクトル)
# 変数 = np.pad(ベクトル, [前に追加する要素数,後ろに追加する要素数],"constant")

# 引数にconstantを渡すことで、同一の要素を追加する(デフォルトで0が追加される)
# 引数にedgeを指定すれば、両端の数字をコピーして追加可能
# 埋め込む値を指定する場合にはconstant_valuesを指定して、追加する
#%%
arr1 = np.array([1,2,3])
print(np.pad(arr1,(2,2),"constant"))
print()
print(np.pad(arr1,(2,2),"edge"))
print()
print(np.pad(arr1,(2,2),"constant",constant_values=(8,9)))
print()

#パディング(行列)

# 変数 = np.pad(行列, [前(上)に追加する要素数,後ろ(下)に追加する要素数],"constant")

# [前(上)に追加する要素数,後ろ(下)に追加する要素数]が一致しない場合には、下記の通り分割できる
# [[上に追加する要素数,下に追加する要素数],[前に追加する要素数,後ろに追加する要素数]]

#%%
arr1 = np.array([[1,2,3],
                [4,5,6]])
print(arr1)
print(np.pad(arr1,[2,3],"constant"))
print()
print(np.pad(arr1,[[3,3],[2,2]],"constant"))
print()
print(np.pad(arr1,[5,3],"edge"))
print()
print(np.pad(arr1,[5,3],"constant",constant_values=(0,9)))


#4-1 対角行列

# diag関数を使用することで、対角行列を作成可能

# 変数 = np.diag([要素1,要素2,要3,…])
# 引数にkを付与することで、縦（+),横（-)に0の要素を追加可能


#%%
arr1 = np.diag([1,2,3])
print(arr1)

#下記でも同様の結果を出力可能
#%%
Z = np.diag(np.arange(1,4))
print(Z)

#%%
arr2 = np.diag(1+np.arange(4),k=1)
print(arr2)


##5-1

# unravel_index関数により、引数で指定した値がベクトル、行列内のどのindexに位置するか戻り値として返す

# 変数 = np.unravel_index(要素,(リスト) )
# 戻り値として要素が第2引数のどの位置に存在するか返ってくる
# 第1引数をリストとした場合には、すべての要素のインデクスが返ってくる
# →　(array([要素1, 要素2], dtype=int64),\  #何個目の行列か
#    array([要素1, 要素2], dtype=int64),\　 #何行目か
#    array([要素1, 要素2], dtype=int64))    #何列目か

#%%
print(np.arange(6*7*8).reshape(6,7,8))
print()
arr1 = np.unravel_index(99,(6,7,8))
print(arr1)
print()
arr2 = np.unravel_index([4,20],(6,7,8))
print(arr2)


##6-1 タイル状の配列

##配列を指定し、タイル状に並べる

# 変数 = np.tile(配列,(横にいくつか,縦にいくつか))

#%%
import numpy as np

arr1 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
arr2 = np.tile(arr1,(3,3))
print(arr1)
print()
print(arr2)

##7-1同一の要素を取り出す

# 指定した配列から同一の要素を取り出す
#引数となる配列は2つまで

# 変数 = np.intersect1d(配列1,配列2)

#%%
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(Z1)
print()
print(Z2)
print()
print(np.intersect1d(Z1,Z2))


##8-1日付取得

# datetimeモジュールをインポートしなくても、numpyの関数で取得可能

# 本日の日付の取得方法

# np.datetime64('today', 'D') 

# 昨日や明日も以下の通り

# yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
# tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')

##8－2月の日付確認

# 任意の年の日付を確認する

# 変数 = np.arange('yyyy-mm', 'yyyy-mm+1', dtype='datetime64[D]')

#%%
Z = np.arange('2016-07', '2016-09', dtype='datetime64[D]')
print(Z)