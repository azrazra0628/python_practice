## グラフを使いこなす

#1. axesの分割

# pyplotでグラフを描くためのエリアをfigureオブジェクト
# その中に表示される座標軸をaxesオブジェクトという
# デフォルトでpyplotでは1つのfugureオブジェクトとaxesオブジェクトで構成される

# fugureを分割し、複数のaxesを用意し、複数のグラフを表示させることができる

#2. subplotで分割
# figureの分割には,subplot関数で分割する

# 変数 , (変数) = plt.subplot(整数(x軸), 整数（Y軸）)

# 引数に分割する条件を記載し、戻り値なる変数に,figureオブジェクトと、分割された
# axesオブジェクトが格納される

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y0 = np.sin(x)
y1 = np.cos(x)

fig, (p_a1, p_a2) = plt.subplots(2, 1)

p_a1.plot(x, y0, 'r', label='y = sin(x)')
p_a1.legend()
p_a2.plot(x, y1, 'b', label='y = cos(x)')
p_a2.legend()
plt.show()

#3. figureのaxesを追加する
# メインのグラフを作成した後に、新たにaxesを追加する場合に使用する

# 変数 = plt.axes([横位置, 縦位置, 幅, 高さ])

# 大きさはfigure全体を1.0とする相対的な値で指定する

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0, 'r', label='y = sin(x)')
plt.legend()

ax2 = plt.axes([0.3, 0.3, 0.4, 0.4])
ax2 = plt.plot(x, y1, 'b', label='y = cos(x)')
ax2.legend()

plt.show()

#4. テキストを追加する

# グラフの中にテキストを表示させるには以下の通り
# 変数 = plt.text(x値, y値, テキスト)

# 引数のオプションに,以下の指定が可能
# fontsize - テキストのサイズ指定
# color - テキストのカラー指定

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0, 'r', label='y = sin(x)')
plt.legend()

plt.text(-6, 0.8, 'This is sample', fontsize=16, color='r')

plt.show()

#5. →の追加

# 変数 = plt.arrow(X値, Y値, X幅, Y幅)
# 以下のオプションあり
# width = 矢印の太さ
# head_width = 矢印の頭部分の幅
# head_length = 矢印の頭部分の長さ
# color = 矢印の色

# arrow矢印はピンポイントで矢印の先端を指定するのが難しい
#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0, 'b', label='y = sin(x)')
plt.legend()

plt.arrow(2., 0., -1.5, 0., width=0.05, head_width=0.2, head_length=0.5, color='y')

plt.show()

#6. 注釈をつける


# 矢印とテキストを合体させてもの
# annotate関数で作成する
# 変数 = plt.annotate(テキスト)

# 以下のオプション指定でこまやかな設定をする

# xy = (x値, y値)　- 矢印の先端の位置を指定する
# xytext = (x値, y値) - テキストの表示位置を指定する
# fontsize = 数値 - テキストのフォントサイズを指定する
# color = 色の指定 = 表示するテキストの色の指定をする
# arrowprops = dict(属性=値, …)　- 辞書のインスタンスを作成し、矢印のこまやかな設定をする


#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y0 = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y0, 'b', label='y = sin(x)')
plt.legend()

plt.annotate('here!!', xy=(0,0), xytext=(1, -0.5), \
        arrowprops=dict(arrowstyle='simple', color='c'), \
        fontsize=18, color='r')

plt.show()

# arrowよりも指定の位置を指定しやすい

#7． 線の描画

# 縦横に直線を引く場合、「axhline」「axvline」関数を使用する

# plt.axhline(y=値)
# plt.axvline(x=値)
# 以下のオプション指定可能
# color - 線分の色
# alpha - 透過度。0から1の実数で指定
# linewidth - 線の太さ
# xmin, xmax - axhlineで横線を引く際のXの最小値と最大値
# ymin, ymax - axvlineで縦線を引く際のYの最小値と最大値

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y, 'b', label='y = sin(x)')
plt.legend()

plt.axhline(y=0., linewidth=2, color='y')
plt.axvline(x= -np.pi * 1.5, ymin=0.5, ymax=1., linewidth=5, color='r')
plt.axvline(x= -np.pi * 0.5, ymin=0., ymax=0.5, linewidth=5, color='r')
plt.axvline(x= np.pi * 0.5, ymin=0.5, ymax=1., linewidth=5, color='r')
plt.axvline(x= np.pi * 1.5, ymin=0., ymax=0.5, linewidth=5, color='r')

plt.show()

#8. 一定の幅で塗りつぶす

# 一定の範囲を色付けし、その範囲を注目させる
# 「axhspan」「axvspan」関数を使用する

# plt.axhspan(Y最小値,Y最大値)
# plt.axvspan(X最小値,X最大値)

# オプションはaxhlineとほぼ一緒

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y, 'b', label='y = sin(x)')
plt.legend()

plt.axhspan(0., 1., color='g', alpha=0.25)
plt.axvspan(-np.pi, 0., color='c', alpha=0.25)

plt.show()

# #9. 指定領域の塗りつぶし
# グラフの線い沿って一定の領域ないを塗りつぶす際には「fill」関数を使用する

# plt.fill([Xリスト], [yリスト])

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, np.pi /20)
y = np.sin(x)

s_x = np.arange(-np.pi, np.pi+0.001, np.pi /20)
s_y = np.sin(s_x)
c_x = np.arange(-np.pi, np.pi+0.001, np.pi /20)
c_y = np.cos(c_x)

plt.plot(x,y, 'b', label='y = sin(x)')
plt.legend()

plt.fill(s_x, s_y, color='m', alpha=0.2)
plt.fill(c_x, c_y, color='c', alpha=0.2)

plt.show()