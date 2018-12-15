# matplotlib003
## 様々なグラフ

# plot - 折れ線グラフ
# bar - 棒グラフ

# 1. 棒グラフを作る

# plt.bar([Xデータ], [Yデータ])

#%%
import numpy as np
import matplotlib.pyplot as plt

x = list('abcdefg')
y = np.array([np.random.randint(75) + 25 for i in range(7)])

plt.bar(x, y, label='random.value')
plt.legend()
plt.show()

# 棒グラフは、折れ線グラフと異なり、1つのグラフに無数のデータを表示させることはないので、
# 必ずしもx、y軸の値は数値でなければいけないことはない

# 2. グラフを重ねる

# 複数のデータを重ねる（スタックする）方法

# bottomオプションを使用して、描く棒の下位置を最初のグラフの上端に設定する
# 二つ目のグラフのbottomオプションに1つ目のグラフのy値を指定する

#%%
import numpy as np
import matplotlib.pyplot as plt

x = list('abcdefg')
y0 = np.array([np.random.randint(75) + 25 for i in range(7)])
y1 = np.array([np.random.randint(75) + 25 for i in range(7)])

plt.bar(x, y0, label='random A')
plt.bar(x, y1, bottom=y0, label='random B')
plt.legend()
plt.show()

# 3. 棒グラフを横に並べる
# 普通にbarを複数回実行するとグラフが重なる。

# X軸の値が交互に並ぶようにすればよい

#%%
import numpy as np
import matplotlib.pyplot as plt

x0 = np.arange(0, 13, 2)
x1 = np.arange(1, 14, 2)

y0 = np.array([np.random.randint(75) + 25 for i in range(7)])
y1 = np.array([np.random.randint(75) + 25 for i in range(7)])

lb =list('abcdefg')

plt.bar(x0, y0, tick_label=lb, label='random A')
plt.bar(x1, y1, label='random B')
plt.legend()
plt.show()

# X軸の表示ラベルを別途表示させる場合には、tick_labelオプションを指定して別途用意したリストを指定する

# グラフを半分だけ重ねる場合には、x値の間隔を0.5だけずらして表示させる

#%%
import numpy as np
import matplotlib.pyplot as plt

x0 = np.arange(0, 10, 1.5)
x1 = np.arange(.5, 11, 1.5)

y0 = np.array([np.random.randint(75) + 25 for i in range(7)])
y1 = np.array([np.random.randint(75) + 25 for i in range(7)])

lb =list('abcdefg')

plt.bar(x0, y0, tick_label=lb, label='random A')
plt.bar(x1, y1, label='random B')
plt.legend()
plt.show()

# 4. 円グラフを描く

# pie - 円グラフ作成

# 引数には、グラフ化する値をリストにまとめて指定する

# 以下指定可能なオプション引数
# labels - 表示するデータのラベル
# shadow - true指定で影をつけることができる
# explode - 特定のデータを円弧から話て表示させる、各データの表示位置数値をリストにまとめて指定する
# startangle - 円のスタート位置。デフォルトは三時から
# autopct - 各円弧にパーセントを表示する。'%1.1f%%'というフォーマットで記載する

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.array([np.random.randint(75) + 25 for i in range(7)])
y = list('abcdefg')
ex = [0, 0, 0, 0.25, 0, 0, 0]
plt.pie(x, labels=y, shadow=True, explode=ex, autopct='%1.1f%%')
plt.legend()
plt.show()

#labelsやexpoldeオプションで指定するリストの要素数は表示するデータ数と一致している必要がある

# 5. ヒストグラムの作成

# ヒストグラムは多数のデータを整理するのに使用される
# hist関数を使用し、描画する

# (n, bins, patches) = plt.hist(データ, 分割数)

# グラフ調整のオプションは以下
# range - グラフ化する範囲を指定する,(最小値, 最大値)というタプルを用意
# orientation - グラフの方向を指定する, horizontalまたはverticalを指定する
# stacked - データを積み重ねるか指定する
# comulative - 累積ヒストグラム(値をすべて加算していく)とするか指定する
# density - 確率密度関数の近似値を返す
# histtype - バーのスタイルを指定する
# color - バーの色を指定する


# hist関数は3つの値を戻り値として返す。
# n - 各バーのデータ数のリスト
# bins - 各バーの境界の値のリスト 
# patches - 表示される各バーのオブジェクトのリスト


#%%
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm

(sigma, mu) = (10, 50)
value = np.random.randn(1000)*sigma+mu
plt.hist(value, 25)
plt.show()

# 6. 確率密度曲線を描く
# ヒストグラムではオプションで確率密度曲線という線グラフを表示することもある

#%%
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm

(sigma, mu) = (10, 50)
value = np.random.randn(1000)*sigma+mu
(n, bins, patches) = plt.hist(value, 50, density=True)
plt.plot(bins, norm.pdf(bins, loc=mu, scale=sigma))
plt.show()

# 7. 複数データの利用

# 複数データの利用がある場合には、hist関数の第一引数に表示したいデータをリストでまとめたものを
# 指定する
# stackedオプションの指定があると、積み重なって表示される

#%%
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm

(sigma, mu) = (10, 50)
value0 = np.random.randn(1000)*sigma+mu
value1 = np.random.randn(1000)*sigma+mu
(n, bins, patches) = plt.hist([value0, value1], 25, stacked=True, density=True)
plt.plot(bins, norm.pdf((bins-mu)/sigma)/sigma)
plt.show()

#8. 散布図の作成

# 散布図 - scatter関数

# plt.scatter(Xデータ, Yデータ)

# Xデータ、Yデータそれぞれ座標の値をリストにまとめて用意する

# s - サイズデータ
# c - 色データ
# marker - 描く図形の形状を指定する

#%%
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm

(n, sigma, mu) = (300, 10, 50)

x = np.random.randn(n) * sigma + mu
y = np.random.randn(n) * sigma + mu
c = np.random.randn(n)
s = np.random.randn(n) **2 * np.pi *100

plt.scatter(x, y, s=s, c=c, alpha=0.25)
plt.show()

