## 文字列のリスト（配列）と数値のリストを相互に変換

# Pythonで文字列strのリスト（配列）と数値int, floatのリストを相互に変換する。

# リストから新たなリストを生成する場合はリスト内包表記を使うとforループよりもシンプルに書ける。

#1. 数値のリストを文字列のリストに変換

# 数値から文字列への変換はstr()関数を使う。
# Pythonでは数値を指数表記や16進数、
# 2進数など様々な形式で表現できるが、str()で変換した場合は通常の10進表記の文字列となる。

#%%
l_n = [-0.5, 0, 1.0, 100, 1.2e-2, 0xff, 0b11]

l_n_to_str = [str(s) for s in l_n]
print(l_n_to_str)
# ['-0.5', '0', '1.0', '100', '0.012', '255', '3']

#2. 数値を2進数、8進数、16進数の文字列に変換

# 2進数、8進数、16進数の文字列に変換する場合は、bin()やoct(), hex()関数を使うか、
# format()関数（または文字列strのformat()メソッド）を使う。

#%%
l_i = [0, 64, 128, 192, 256]
l_i_hex1 = [hex(i) for i in l_i]
print(l_i_hex1)
# ['0x0', '0x40', '0x80', '0xc0', '0x100']

#%%
l_i_hex2 = [format(i, '04x') for i in l_i]
print(l_i_hex2)
# ['0000', '0040', '0080', '00c0', '0100']

#%%
l_i_hex3 = [format(i, '#06x') for i in l_i]
print(l_i_hex3)
# ['0x0000', '0x0040', '0x0080', '0x00c0', '0x0100']


#3. 数値を指数表記の文字列に変換

# 桁数によって自動的に指数表記になる場合もあるが、常に指数表記の文字列に変換する場合は、
# format()関数（または文字列strのformat()メソッド）を使う。

# 仮数部の桁数を指定することができる。なお引数に大文字のEを使うと、出力文字列も大文字のEとなる。

#%%
l_f = [0.0001, 123.456, 123400000]

l_f_e1 = [format(f, 'e') for f in l_f]
print(l_f_e1)
# ['1.000000e-04', '1.234560e+02', '1.234000e+08']

l_f_e2 = [format(f, '.3E') for f in l_f]
print(l_f_e2)
# ['1.000E-04', '1.235E+02', '1.234E+08']

#4. 文字列のリストを数値のリストに変換

# 文字列から数値への変換はint()関数またはfloat()関数を使う。

# int()関数は整数int型への変換、float()関数は浮動小数点float型への変換となる。

# float()では、整数部が省略された文字列は整数部に0が補完される。

#%%
l_si = ['-10', '0', '100']

l_si_i = [int(s) for s in l_si]
print(l_si_i)
# [-10, 0, 100]

l_sf = ['.123', '1.23', '123']

l_sf_f = [float(s) for s in l_sf]
print(l_sf_f)
# [0.123, 1.23, 123.0]

#5. 2進数、8進数、16進数表記の文字列を数値に変換

# int()関数の第二引数には基数を指定できる。
# 2なら2進数、8なら8進数、16なら16進数として文字列を数値に変換する。

# 0を指定すると、0bや0o, 0xのプレフィックスが付いた文字列を
# それぞれ2進数、8進数、16進数として整数に変換する。

#%%
l_sb = ['0011', '0101', '1111']

l_sb_i = [int(s, 2) for s in l_sb]
print(l_sb_i)
# [3, 5, 15]

l_sbox = ['100', '0b100', '0o77', '0xff']

l_sbox_i = [int(s, 0) for s in l_sbox]
print(l_sbox_i)
# [100, 4, 63, 255]

#6. 指数表記の文字列を数値に変換

# 指数表記の文字列は特別な指定をする必要なくfloat()関数でそのまま変換できる。

#%%
l_se = ['1.23e3', '0.123e-1', '123']

l_se_f = [float(s) for s in l_se]
print(l_se_f)
# [1230.0, 0.0123, 123.0]


#7. 数値に変換できる文字列のみ変換
# 数値に変換できない文字列をint()やfloat()に渡すとエラーValueErrorになる。

# エラー時にFalseを返す関数を新たに定義すると、
# 変換できる要素のみ数値に変換してリストの要素とすることができる。

#%%
def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

def is_float(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

l_multi = ['-100', '100', '1.23', '1.23e2', 'one']

l_multi_i = [int(s) for s in l_multi if is_int(s)]
print(l_multi_i)
# [-100, 100]

l_multi_f = [float(s) for s in l_multi if is_float(s)]
print(l_multi_f)
# [-100.0, 100.0, 1.23, 123.0]

# まとめ
# ①数値の文字列変換はstr関数を使用し、文字列の数値変換はint関数を使う
