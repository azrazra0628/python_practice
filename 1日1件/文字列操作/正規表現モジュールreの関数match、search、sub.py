## 正規表現モジュールreの関数match、search、sub

#Pythonには正規表現の操作を提供するモジュールreが用意されている。

#%%
import re

s = 'one two one two'

#1. 文字列の先頭がパターンにマッチするかを調べるmatch()

# re.match()は文字列の先頭がパターンにマッチするかどうかを調べる。

#%%
m = re.match('one',s)
print(m)
# <_sre.SRE_Match object; span=(0, 3), match='one'>

# マッチする場合はmatchオブジェクトを返す。
# matchオブジェクトはgroup()、start()、end()、span()などのメソッドを持ち、
# マッチした文字列やその位置などを返す。

#%%
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# group()メソッドはパターンにマッチした全体を返すが、
# パターンの一部分を()で囲んでおくと、groups()メソッドを使って、
# ()で囲まれた部分にマッチしたそれぞれの文字列をタプルで取得できる。

#%%
m = re.match('(one) (two)', s)
print(m)
print(m.group())
print(m.groups())
# <_sre.SRE_Match object; span=(0, 7), match='one two'>
# one two
# ('one', 'two')

# 先頭にマッチする文字列がない場合はNoneを返す。

#%%
m = re.match('two',s)
print(m)
# None

#2. 先頭に限らずパターンにマッチするかを調べるsearch()

# re.search()は先頭にない文字列も探すことができる。
# re.match()と同じく、マッチする場合はmatchオブジェクトを返す。

#%%
m = re.search('one',s)
print(m)
# <_sre.SRE_Match object; span=(0, 3), match='one'>

#文字列中にマッチする部分が複数あっても、返すのは最初にマッチした部分のみ。

#3. マッチする部分すべてをリストで返すfindall()

# re.findall()は、マッチする部分が複数ある場合、マッチした文字列すべてをリストにして返す。
# 返すのはmatchオブジェクトではないので注意。

#%%
m = re.findall('one', s)
print(m)
# ['one', 'one']

#4. マッチする部分すべてをイテレータで返すfinditer()

# re.finditer()はマッチする部分すべてをmatchオブジェクトのイテレータで返す。
# ただのリストを返すre.findall()とは違い、
# matchオブジェクトを得られるので、マッチした位置なども取得することができる。

#%%
m = re.finditer('one',s)
print(m)
# <callable_iterator object at 0x10e786470>

for match in m:
    print(match)
# <_sre.SRE_Match object; span=(0, 3), match='one'>
# <_sre.SRE_Match object; span=(8, 11), match='one'>

#5. マッチした部分を置換するsub()、subn()

# re.sub()を使うと、マッチした部分を他の文字列に置換することができる。

#%%
m = re.sub('one','ONE',s)
print(m)
# ONE two ONE two

m = re.sub('one two', 'xxx', s)
print(m)
# xxx xxx

# パターンの一部を()で囲むと、置換後の文字列の中でマッチした文字列を使用することができる。

#%%
m = re.sub('(one) (two)', '\\1X\\2', s)
print(m)
# oneXtwo oneXtwo

m = re.sub('(one) (two)', r'\1X\2', s)
print(m)
# oneXtwo oneXtwo

# 置換後の文字列と置換された部分の個数とのタプルで返すre.subn()関数もある。

#%%
m = re.subn('one','ONE',s)
print(m)
# ('ONE two ONE two', 2)

# パターンで文字列を分割するsplit()

#5. re.split()はパターンにマッチした部分で文字列を分割し、リストにして返す。

#%%
m = re.split(' ', s)
print(m)
['one', 'two', 'one', 'two']

#6. 正規表現オブジェクトをコンパイルするcompile()

# 同じパターンを繰り返し使用する場合は、re.compile()で、
# あらかじめパターンをコンパイルして正規表現オブジェクトを生成したほうがよい。

#%%
p = re.compile('one')
m = p.match(s)
print(m)
# <_sre.SRE_Match object; span=(0, 3), match='one'>

m = p.findall(s)
print(m)
# ['one', 'one']

m = p.sub('ONE', s)
print(m)
# ONE two ONE two

# まとめ
# ①s正規表現のreモジュールの各種メソッドを使用して、パターンマッチを検索したり、置換したりする
# ②重複して使用する場合にはコンパイルして使用すると視認性がよい



