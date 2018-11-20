## formatで書式変換（0埋め、指数表記、16進数など）

# Pythonで数値や文字列を様々な書式に変換（フォーマット）する場合、
# 組み込み関数format()または文字列メソッドstr.format()を使う

#1. 組み込み関数format()
# 概略は以下の通り。

# format(value, format_spec)
# 第一引数value: 元の値 / 文字列strや数値int, floatなど
# 第二引数format_spec: 書式指定文字列 / 文字列str
# 返り値: 書式化された文字列str

#%%
s = format(255, '04x')
print(s)
print(type(s))
# 00ff
# <class 'str'>

print(format('center', '*^16'))
# *****center*****

#2. 文字列メソッドstr.format()

# format()メソッドを呼び出す文字列str内の{}は置換フィールドと呼ばれ、
# format()メソッドの引数に置き換えられる。

# 返り値は書式化された文字列str。

s = '{:04x}'.format(255)
print(s)
print(type(s))
# 00ff
# <class 'str'>

print('{:*^16}'.format('center'))
# *****center*****

#3. 置換フィールドに対する引数の指定

# 順番通りに引数を指定（デフォルト）

# 置換フィールド{}は複数存在してもよく、
# デフォルトではメソッドの引数が順番に処理される。
# {}内の書式指定文字列を省略するとstr()で文字列に変換するだけになる。

# 文字列中に変数の値を挿入してprintで表示する場合などに便利。

#%%
print('{}-{}-{}'.format('100', '二百', 300))
# 100-二百-300

#%%
print('{}+{}={}'.format(100,200,300))
# 100+200=300

# 整数値に対して位置引数を指定

# {0}や{1}のように{}内に整数値を指定すると引数の順番に応じて出力される。
# 同じ番号を繰り返し使うこともできる。文字列中に同じ値を挿入したい場合は便利。

#%%
print('{1}--{0}--{1}'.format('foo', 'var'))
# var--foo--var

# 任意の名前（文字列）に対してキーワード引数を指定
# {}内に任意の名前を指定し、キーワード引数として入力することも可能。

#%%
print('{year}年{month}月{day}日'.format(year=1986,month=6,day=28))
# 1986年6月28日

# リスト、辞書を引数に指定

# 置換フィールド内でリストのインデックスや辞書のキーを[]で指定する。
# 辞書のキーの指定では引用符'や"は使わないので注意。

#%%
l = ['one', 'two', 'three']
print('{0[0]}--{0[1]}--{0[2]}'.format(l))
# one--two--three

d1 = {'name': 'Alice', 'age': 20}
d2 = {'name': 'Bob', 'age': 30}
print('{0[name]} is {0[age]} years old.\n{1[name]} is {1[age]} years old.'.format(d1, d2))
# Alice is 20 years old.
# Bob is 30 years old.

# リストに*をつけて引数に指定することで位置引数として展開したり、
# 辞書に**をつけて引数に指定することでキーワード引数として展開することも可能。

#%%
l = ['one', 'two', 'three']
print('{}-{}-{}'.format(*l))
# one-two-three

d = {'name': 'Alice', 'age': 20}
print('{name} is {age} years old.'.format(**d))
# Alice is 20 years old.

# 波括弧{}の記述
# format()メソッド内で波括弧{, }を書きたい場合は{{, }}のように2回繰り返して書く。
# バックスラッシュ\ ではエスケープできないので注意。

#%%
print('{{}}-{num}-{{{num}}}'.format(num=100))
# {}-100-{100}

# 書式指定文字列
#いずれの場合も、書式を指定するには{}内の整数値や名前の文字列のあと:書式指定文字列のように書く

#%%
print('{num:x}'.format(num=255))
# ff

print('{year}年{month:02}月{day:02}日'.format(year=2018, month=1, day=11))
# 2018年01月11日

#3. 左寄せ、中央寄せ、右寄せ

# <、^、>で左寄せ、中央寄せ、右寄せなどのアラインメントができる。全体の文字数を数値で指定する。

#%%
print('left  : {:<10}'.format(100))
print('center: {:^10}'.format(100))
print('right : {:>10}'.format(100))
# left  : 100       
# center:    100    
# right :        100

# 4. 0埋め

# ゼロ埋めして桁数を合わせたい場合は埋める文字を0として右寄せする。

# ゼロ埋めの場合はアラインメント記号を省略すると=を指定したものとして処理される。

#%%
print('zero padding:  {:0=10}'.format(100))
# zero padding:  0000000100

# =として処理されるので、上述のように引数に文字列を指定するとエラーになってしまう。注意。

#%%
print('zero padding: {:0=10}'.format('100'))
# ValueError: '=' alignment not allowed in string format specifier

#5. 符号（プラス、マイナス）
# デフォルトでは負の数にのみ符号（マイナス-）が表示される。

# 書式化指定文字列に+をつけると正の数にも符号（プラス+）が表示される。
# スペースをつけると正の数の先頭に一文字分のスペースが表示され、負の数と桁数が揃う。

#%%
print('sign: {}'.format(100))
print('sign: {}'.format(-100))
# sign: 100
# sign: -100

print('sign: {:+}'.format(100))
print('sign: {:+}'.format(-100))
# sign: +100
# sign: -100

print('sign: {: }'.format(100))
print('sign: {: }'.format(-100))
# sign:  100
# sign: -100

# 上述のゼロ埋めなど任意の文字で埋める場合は注意が必要。
# +もスペースもつけないデフォルトでは正の数が一文字多く埋められてしまう。

#%%
print('sign: {:06}'.format(100))
print('sign: {:06}'.format(-100))
# sign: 000100
# sign: -00100

print('sign: {:+06}'.format(100))
print('sign: {:+06}'.format(-100))
# sign: +00100
# sign: -00100

print('sign: {: 06}'.format(100))
print('sign: {: 06}'.format(-100))
# sign:  00100
# sign: -00100

#6. 桁区切り（カンマ、アンダースコア）

# 3ケタ毎にカンマ,またはアンダースコア_の区切りを入れる。
# 大きい数値が見やすくなる。
# なお、アンダースコア_はPython3.6で追加されたオプションなので、
# それより前のバージョンでは使えない。

#%%
print('{:,}'.format(1000000))
# 1,000,000

# 浮動小数点数float型の場合は整数部にのみ区切りが入る。

#%%
print('{:,}'.format(1234.56789))
# 1,234.56789

#7. 2進数、8進数、16進数

# 数値を2進数、8進数、16進数に変換して出力する。

# b: 2進数
# o: 8進数
# d: 10進数
# x, X: 16進数（大文字だとアルファベットが大文字表記）

#%%
print('bin: {:b}'.format(255))
print('oct: {:o}'.format(255))
print('dec: {:d}'.format(255))
print('hex: {:x}'.format(255))
print('HEX: {:X}'.format(255))
# bin: 11111111
# oct: 377
# dec: 255
# hex: ff
# HEX: FF

# 2進数や16進数ではアンダースコア_の桁区切りのみ挿入できる（Python3.6以降）。
# 4ケタ区切りとなる。0埋めの文字数はアンダースコアの数も考慮する必要がある。

#%%
print('hex: {:08x}'.format(255))
print('hex: {:09_x}'.format(255))
print('hex: {:#011_x}'.format(255))
# hex: 000000ff
# hex: 0000_00ff
# hex: 0x0000_00ff