# Python, splitでカンマ区切り文字列を分割、空白を削除しリスト化

#カンマ（コンマ）区切りの文字列を分割しリスト化する場合、
# 間に空白（スペース）がないとsplit()だけで上手くいく。

# 空白がある場合は、strip()と組み合わせると余分な空白を除去できるので便利。
# さらにリスト内包表記を使うとスマートに書ける。

#1.split(): 指定の区切り文字で文字列を分割しリストとして返す

#メソッドsplit()を使うと、文字列を指定の区切り文字で分割し、
# リストとして取得できる

変数 = 対象文字列.split(sep='区切り文字')
#　引数sepを指定しないと、デフォルト空白で区切る
# タブ区切り文字列も引数を省略したsplit()で問題ない

#%%
s = 'one two three'
l = s.split()
print(l)
# ['one', 'two', 'three']

#タブ区切りも対応可能
#%%
s = 'one two        three'
l = s.split()
print(l)
# ['one', 'two', 'three']

#\tも対応可能
#%%
s = 'one\ttwo\tthree'
l = s.split()
print(l)
# ['one', 'two', 'three']

#%%
s = 'one::two::three'
l = s.split('::')
print(l)
# ['one', 'two', 'three']

#カンマ区切りの文字列の場合、余分な空白が無ければ問題ない.
#カンマ+空白で区切られた文字列についても引数を指定しないと先頭に空白が入ったリストになる
#%%
s = 'one, two, three'
l = s.split(',')
print(l)
# ['one', ' two', ' three']

#カンマ＋空白を区切り文字にしてもいいが、スペースの量が均等でないと、対応できない
#%%
s = 'one, two,  three'
l = s.split(', ')
print(l)
# ['one', 'two', ' three']

#2.strip(): 文字列の先頭・末尾の余分な文字を削除する

#strip()は文字列の先頭・末尾の余分な文字を削除するメソッド。
#引数を省略すると空白文字が除去された新たな文字列を返す。元の文字列自体は変更されない。

# 変数 = 文字列.strip(省略文字)

#引数に文字列を指定するとその文字列に含まれる文字が除去される

#%%
s = '  one  '
print(s.strip())
# one

#%%
s = '-+-one-+-'
print(s.strip('-+'))
# one

# 引数を指定した場合には、空白は削除されないので、省略文字に空白を追加する

#%%
s = ' +-+one--+'
print(s.strip(' +-'))
# one

#3.リスト内包表記: リストの要素に関数・メソッドを適用

# 最終的にリストを取得したい場合、内包表記を使用するのがベター
#%%
s = 'one, two, three'
l = [x.strip() for x in s.split(',')]
print(l)
# ['one', 'two', 'three']

# 'one, , three'のように、
# カンマ区切りの要素が欠落している場合、
# 最初の方法だと空文字列''の要素としてリスト化される。

#%%
s = 'one, , three'
l = [x.strip() for x in s.split(',')]
print(l)
# ['one', '', 'three']
print(len(l))
# 3

# このような場合if文を使うことで空の部分を省略することが可能

#%%
s = 'one, , three'
l = [x.strip() for x in s.split(',') if not x.strip() == '' ]
print(l)
# ['one', 'three']
print(len(l))
# 2

#4.数値のリストとして取得

もし取得したいリストが数値の場合には、リスト内包表記の中でint()やfloat()を使用する
#%%
s = '1,2,  3,4'

l = [int(x.strip()) for x in s.split(',')]
print(l)
#[1, 2, 3, 4]
print(type(l[0]))
#<class 'int'>

#5.join(): リストを結合して文字列として取得

# 逆の手順でリストを結合して文字列を取得したい場合には,join()メソッドを使用する
# joinメソッドが文字列のメソッドの為、リストは引数で指定する。

変数 = 文字列.join(引数)
#%%
s = '----one----,  two-+-+,+++three++'
l = [x.strip(' +-') for x in s.split(',')]

print(l)
#['one', 'two', 'three']
s = ','.join(l)
print(s)
#one,two,three

#1行で書くと下記の感じ

#%%
s = '----one----,  two-+-+,+++three++'
s_new = '-'.join([x.strip(' +-') for x in s.split(',')])
print(s_new)
#one-two-three


#固定の区ごり文字を変更するだけならreplace()メソッドを使うほうが簡単
#%%
s = 'one,two,three'

s_new = s.replace(',','-')
print(s_new)
#one-two-three

まとめ

# ①文字列をリストかするときは、きれいな文字列なら、split()メソッドを使えばOK
# ②きれいなならびでない場合には、内包表記でsplit()メソッドとstrip()メソッドを使用する
