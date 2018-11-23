## 半角1文字、全角2文字として文字数（幅）カウント

#1. unicodedata.east_asian_width()を使う
# 半角を1文字、全角を2文字として文字列の文字数（文字幅）をカウントしたい場合、
# 標準モジュールunicodedataの関数east_asian_width()を使う。

# このunicodedata.east_asian_width()を使うことで
# Unicode文字に割り当てられたEast Asian Widthの値が取得できる。
# この値を使うと、その文字が半角か全角かを判定できる。

#2. 半角を1文字、全角2を文字としてカウントするコード例

# まず、unicodedata.east_asian_width()の動きを確認してみる。
# 全角かなを渡すとWが文字列（str）として返ってくる。

#%%
import unicodedata

print(unicodedata.east_asian_width('あ')) 
print(type(unicodedata.east_asian_width('あ')))
# W

# 半角英数はNa、全角英数はF、半角カナはH、特殊な文字はAが返ってくる。

#%%
print(unicodedata.east_asian_width('a'))  # 半角英数
# Na

print(unicodedata.east_asian_width('Ａ'))  # 全角英数
# F

print(unicodedata.east_asian_width('ｱ'))  # 半角カナ
# H

print(unicodedata.east_asian_width('Å'))  # 特殊文字（例: オングストローム）
# A

# 以下のような関数を定義すると、半角を1文字、全角2を文字として文字列の文字数をカウントできる。
# F, W, Aは全角 (= 2文字分)、H, Na, Nは半角 (= 1文字分) として数えている。

#%%
import unicodedata

def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

print(get_east_asian_width_count('あいうえお'))
# 10

print(get_east_asian_width_count('abcde'))
# 5

print(get_east_asian_width_count('ｱｲｳｴｵ'))
# 5

print(get_east_asian_width_count('ａｂｃｄｅ'))
# 10

print(get_east_asian_width_count('あｱaａ'))  # 全角2文字（あ, ａ）、半角2文字（ｱ, a）
# 6


# まとめ
# ①全角か半角かで文字数を分ける場合には、unicodedataモジュールを使う
# ②あんま使わないかも…

