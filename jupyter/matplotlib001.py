## matplotlib概要

# グラフ作成ライブラリ
# 他のモジュールで統計・分析を行ったデータを可視化する

#1. matplotlibでグラフを書く

# matplotlibライブラリのpyplotモジュールを使用する
# pltとしてインポートしておくと短くできる

#%%
import numpy as np 
import matplotlib.pyplot as plt

x = np.array(range(0, 10))
print(x)
# [0 1 2 3 4 5 6 7 8 9]

y = x*2

plt.plot(x, y)
plt.show()

# 下記でデータがグラフ化されて表示される
# plt.plot(横軸データ, 縦軸データ)
# plt.show()

# plotメソッドの使い方は「用意されたデータを元にグラフを書く」だけなので、
# 「式をそのままグラフにする」ような使い方はできない


#2. sin曲線を描く

# 数式をもとにグラフで使うデータを用意しておく必要がある

#%%
x = np.arange(-np.pi, np.pi, 0.1)
y = np.sin(x)

print(x[:10])
# [-3.14159265 -3.04159265 -2.94159265 -2.84159265 -2.74159265 -2.64159265
#  -2.54159265 -2.44159265 -2.34159265 -2.24159265]
print(y[:10])
# [-1.22464680e-16 -9.98334166e-02 -1.98669331e-01 -2.95520207e-01
#  -3.89418342e-01 -4.79425539e-01 -5.64642473e-01 -6.44217687e-01
#  -7.17356091e-01 -7.83326910e-01]

plt.plot(x, y)
plt.show()

#3. 複数のグラフを描く
# pyplotでは複数のグラフを1つのグラフエリア内に表示でさせることができる

#%%
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0)
plt.plot(x, y1)
plt.show()

# plotを複数回実行した後にshowメソッドを実行すれば実行回数分のグラフが色分けされて表示される
# 横軸、縦軸のどちらかは、共通の値にしておかないときれいにまとまらない



# plotで表示されるグラフは最低限の表示になっているので、見やすくするためにいくつか設定がある

#4. 凡例を表示させる

# plotメソッドの引数にlabelを指定する
# plt.legend()

#%%
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0, label='y = sin(x)')
plt.plot(x, y1, label='y = cos(x)')
plt.legend()
plt.show()

#5.グラフ表示の設定

# plotでグラフを作成した後、showメソッド使用前に実行する
# タイトルの設定
# plt.title(テキスト)

# x軸、y軸のラベル
# plt.xlabel(テキスト)
# plt.ylabel(テキスト)

#%%
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0, label='y = sin(x)')
plt.plot(x, y1, label='y = cos(x)')
plt.legend()
plt.title('sample graph')
plt.xlabel('degree')
plt.ylabel('value')
plt.show()

#6. grid表示について

# 縦横にgrid線を表示できるgrid関数を使用する

# plt.grid(引数)

# 引数として主なもので以下が指定可能
# color - グリッドの色。6桁の16進数で表記
# alpha - 透過度。0~1の実数で設定
# which - メジャーな線(major),マイナーな線(minor),両方(both)のいずれか
# axis - 描画する方向。xまたはy。省略すると両方表示
# linestyle - ラインの種類.　'-'だと直線。':'だと点線。
# linewidth - ラインの太さ

#%%
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0, label='y = sin(x)')
plt.plot(x, y1, label='y = cos(x)')
plt.legend()
plt.title('sample graph')
plt.xlabel('degree')
plt.ylabel('value')
plt.grid(which='both', axis='x', color='#0000ff', alpha=0.25, linestyle='-', linewidth=1)
plt.grid(which='major', axis='y', color='#00ff00', alpha=0.5, linestyle=':', linewidth=2)
plt.show()

#7. グラフの表示エリア

# グラフの縦横の描画範囲は自動調整される。
# 手動設定する場合には、axis, xlim, ylim関数を使用する

# 表示エリアを設定する
# plt.axis([ xmin, xmax, ymin, ymax ])

# X方向の表示エリアを設定する
# plt.xlim([xmin, xmax])

# y方向の表示エリアを設定する
# plt.ylim([ymin, ymax])

#%%
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0, label='y = sin(x)')
plt.plot(x, y1, label='y = cos(x)')
plt.legend()
plt.title('sample graph')
plt.xlabel('degree')
plt.ylabel('value')
plt.grid(which='both', axis='x', color='#0000ff', alpha=0.25, linestyle='-', linewidth=1)
plt.grid(which='major', axis='y', color='#00ff00', alpha=0.5, linestyle=':', linewidth=2)
plt.xlim([-7, 7])
plt.ylim([-1.5, 1.5])
plt.show()

#8.グラフの形状

# plotではデフォルトで折れ線グラフが表示される
# plt.plotで描画する際に、第3引数に表示に関する引数を指定する

#%%
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0, 'co', label='y = sin(x)')
plt.plot(x, y1, 'm^', label='y = cos(x)')
plt.legend()
plt.title('sample graph')
plt.xlabel('degree')
plt.ylabel('value')
plt.grid(which='both', axis='x', color='#0000ff', alpha=0.25, linestyle='-', linewidth=1)
plt.grid(which='major', axis='y', color='#00ff00', alpha=0.5, linestyle=':', linewidth=2)
plt.xlim([-7, 7])
plt.ylim([-1.5, 1.5])
plt.show()