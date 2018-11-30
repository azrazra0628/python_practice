## 改行を含む文字列の出力、連結、分割、削除、置換

# Pythonにおける改行を含む文字列の操作

#1. 改行を含む文字列を作成、print出力（表示）
# 改行コード \n（LF）, \r\n（CR+LF）

# 文字列内に改行コード\nや\r\nを挿入すると改行される。

#%%
s = 'line1\nline2\nline3'
print(s)
# line1
# line2
# line3

s = 'Line1\r\nLine2\r\nLine3'
print(s)
# Line1
# Line2
# Line3

# トリプルクォート ''' or """
# トリプルクォート'''または"""で囲むと改行も含めてそのままの文字列となる。

#%%
s = '''line1
line2
line3'''
print(s)
# line1
# line2
# line3

# インデントを付けたい場合

# トリプルクォートはスペースもそのまま文字列となるので、
# コード上でキレイに書こうとして以下のようにインデントを入れると不要なスペースが挿入されてしまう。

#%%
s = '''
    Line1
    Line2
    Line3
    '''
print(s)
# Line1
#     Line2
#     Line3

# バックスラッシュ\を使ってコード中の改行を無視して継続行とすることで以下のように書ける。

# 各行を''または""で囲み、文末に改行文字\nを加える。

#%%
s = 'Line1\n'\
    'Line2\n'\
    'Line3'
print(s)
# Line1
# Line2
# Line3


# また、括弧（()）で囲まれている部分では自由に改行できるので、
# バックスラッシュを使わずに括弧()を使って以下のように書くこともできる。

#%%
s = (
    'line1\n'
    'line2\n'
    'line3\n'
)
print(s)
# line1
# line2
# line3

#%%
s = (
    'line1\n'
    '   line2\n'
    '       line3\n'
)
print(s)
# line1
#    line2
#        line3

#2. 文字列のリスト（配列）を改行して連結（結合）

# 文字列メソッドjoin()を使うと、文字列のリスト（配列）を一つの文字列に連結（結合）することができる。
# 改行文字\nや\r\nを使えば文字列要素ごとに改行されて連結される。

#%%
s = '\n'.join(['line1','line2','line3'])
print(s)
# line1
# line2
# line3

#3. 文字列を改行ごとに分割、リスト化: splitlines()

# 文字列メソッドsplitlines()で文字列を改行ごとに分割し、リスト化できる。

#%%
s = 'line1\nline2\nline3'
l = s.splitlines()
print(l)
# ['line1', 'line2', 'line3']

#4. 改行コードの削除、置換k

# splitlines()とjoin()を組み合わせることで、
# 改行を含む文字列から改行コードを削除（除去）したり他の文字列に置換したりすることができる。
# 改行コードの変更も可能。

#%%
s = 'line1\nline2\nline3'

s_new = ''.join(s.splitlines())
print(s_new)
# Line1Line2Line3

s_new = ' '.join(s.splitlines())
print(s_new)
# Line1 Line2 Line3

s_new = ','.join(s.splitlines())
print(s_new)
# Line1,Line2,Line3

s_new = '\r\n'.join(s.splitlines())
print(s_new)
# Line1
# Line2
# Line3

# 改行コードがはっきりしている場合は、文字列を置き換えるreplace()メソッドでもOK。

#%%
s = 'line1\nline2\nline3'

s_new = s.replace('\n','')
print(s_new)
# line1line2line3

s_new = s.replace('\n',' ')
print(s_new)
# line1 line2 line3

s_new = s.replace('\n', ',')
print(s_new)
# line1,line2,line3

# 末尾の改行なしでprint出力する
# 文字列を指定するprint()の引数endのデフォルト値が改行記号'\n'になっているから。
# 末尾で改行させないようにするには引数endを空文字列''とすればOK。末尾の改行なしで出力される。

#%%
print('a', end='')
print('b', end='')
print('c', end='')
# abc

print('a', end='-')
print('b', end='-')
print('c')
# a-b-c

# まとめ
# ①改行をする場合には文字列の改行したい部分で\nをかく
# ②splitlinesメソッドやreplaceメソッドを使用することでリストの文字列を改行を削除することができる