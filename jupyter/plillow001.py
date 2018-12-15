# pillowの基礎

## イメージ処理を行うモジュール

#3. イメージを読み込む

# PILモジュールのimageクラスを用いる。
# Imageのopenメソッドを使用

# 変数 = Image.open(ファイルパス)
相対passでイメージを指定する

戻り値としてJpegImageFileクラスのインスタンスが返ってくる

#%%
from PIL import Image

img = Image.open('img.jpg')
img

#2, イメージの情報を得る

# イメージのピクセルに直接アクセスするオブジェクトとして、PixelAccessクラスの
# loadメソッドを使用する

# 変数 = [イメージ].load()

# PixelAccessクラスは二次元リストのように各ピクセルにアクセスできる
# 色の指定をRGB0~255の整数でタプルでまとめる

#%%
from PIL import Image

im_file = Image.open('img.jpg')
(w, h) = im_file.size
img = im_file.load()
for m  in range(w //4, w // 4 * 3):
    for n in range(h // 4, h // 4 * 3):
        (r, g, b) = img[m, n]
        img[m, n] = (255-r, 255-g, 255-b)
im_file