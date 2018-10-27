##3 データ連携 ##

#1-1 データ読み込み
# 変数 = np.loadtxt('ファイル名',delimiter= データの区切り)


#%%
import numpy as np

arr1 = np.loadtxt('data.txt', delimiter=',')
print(arr1)
print()
print('平均（縦）:'+str(np.mean(arr1,axis=0)))
print('平均（横）:'+str(np.mean(arr1,axis=1)))
print('中央（縦）:'+str(np.median(arr1,axis=0)))
print('中央（横）:'+str(np.median(arr1,axis=1)))
print('偏差（縦）:'+str(np.std(arr1,axis=0)))
print('偏差（横）:'+str(np.std(arr1,axis=1)))

##ファイルパスは下記の通り
##C:\Users\azraz\pythoncode\

#1-2ファイルへの書き込み
# np.savetxt('ファイル名',データ,delimiter=',')

#savetxt関数で行列を保存すると、各値は実数値として保存されるため、視認性は悪い

#%%
import numpy as np

arr1 = np.random.randint(0, 100, (10, 10))
print(arr1)
print()
np.savetxt('data2.txt', arr1, delimiter=',')
print('データをファイルに保存しました')

##バイナリファイルで保存・読み込み場合

# ファイルから読み込む
# 変数 = np.load(ファイルパス)

# ファイルに保存する
# np.save(ファイルパス)

#上記で保存するとnpy拡張子のバイナリファイルとなるため、あまり使わない



##2-1ソートについて

#行列に保管されたデータを横または縦にソートしたい場合に使用する

# 変数 = np.sort(行列, axis=方向)

#%%
import numpy as np

arr1 = np.random.randint(0, 100, (10, 10))
arr2 = np.sort(arr1, axis=0)
arr3 = np.sort(arr1, axis=1)
print(arr1)
print()
print(arr2)
print()
print(arr3)

#2-2 逆順

#sort関数には並び順に関する引数は用意されていないので、
#逆順にするには、行列の後に以下の記号を付与する

# 縦に逆順
# 行列 [::-1]

# 横に逆順
# 行列 [::, ::-1]

# 縦・横に逆準
# 行列 [::-1, ::-1]


#%%
import numpy as np

arr1 = np.random.randint(0, 100, (5,5))
arr2 = np.sort(arr1, axis=1)
print(arr1)
print()
print(arr2)
print()
print(arr2 [::-1])
print()
print(arr2 [::, ::-1])
print()
print(arr2 [::-1, ::-1])


##3-1ビューとスライス

# スライス[]を使用することで行列やベクトルの一部だけを取り出すことができる

ベクトルの一部を取り出す
変数 = ベクトル[開始位置: 終了位置: ステップ]

行列の一部を取り出す
変数 = 行列[開始位置: 終了位置: ステップ]
変数 = 行列[開始位置1: 終了位置1: ステップ1, 開始位置2: 終了位置2: ステップ2]

#%%
import numpy as np

arr1 = np.arange(100).reshape(10,10)

print(arr1)
print()
print(arr1[0:5:1, 0:5:1])
print()
print(arr1[5:10:1, 5:10:1])
print()
print(arr1[0:10:2, 0:10:2])

#スライスは引数で指定したデータのビューを作成しているため、元のデータが変更になるとそのビューも
#表示が変わる

#参照しているだけなので、非常に高速で大量のデータを使う場合にビュー関数は協力な機能
