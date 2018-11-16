## 文字列のリスト（配列）の条件を満たす要素を抽出、置換

# 文字列を要素とするリスト（配列）から、
# 特定の条件を満たす文字列の要素のみを抽出したり、
# 置換や変換などの処理をしたりして新たなリストを生成する。

#1. 特定の文字列を含む（部分一致） / 含まない: in

# 特定の文字列 in 元の文字列で、
# 元の文字列に特定の文字列が含まれるとTrueを返す。これを条件式とする。

#%%
l = ['oneXXXaaa', 'twoXXXbbb', 'three999aaa', '000111222']

l_in = [s for s in l if 'XXX' in s]
print(l_in)
# ['oneXXXaaa', 'twoXXXbbb']


# inの否定はnot inを使う
#%%
l_in_not = [s for s in l if 'XXX'not in s]
print(l_in_not)
# ['three999aaa', '000111222']

#2. 特定の文字列を置換

# リストの要素の文字列を置換したい場合、
# リスト内包表記で各要素に文字列メソッドreplace()を使う。

# 置換対象の文字列がない場合はreplace()を適用しても変更しないので、
# if 条件式で要素を選択する必要はない。
#%%
l = ['oneXXXaaa', 'twoXXXbbb', 'three999aaa', '000111222']

l_replace = [s.replace('XXX','YYY') for s in l ]
print(l_replace)
# ['oneYYYaaa', 'twoYYYbbb', 'three999aaa', '000111222']

# 特定の文字列を含む要素をまるごと置き換えたい場合はinで抽出して三項演算子で処理する。

# 三項演算子は真の値 if 条件式 else 偽の値という形で書く。
# リスト内包表記の式の部分を三項演算子とすればOK。

#%%
l_replace_all = ['ZZZ' if 'XXX' in s else s for s in l]
print(l_replace_all)
 # ['ZZZ', 'ZZZ', 'three999aaa', '000111222']

#3. 特定の文字列で始まる / 始まらない: startswith()

# 文字列メソッドstartswith()は、文字列が引数に指定した文字列で始まるとTrueを返す。

#%%
l_start = [s for s in l if s.startswith('t')]
print(l_start)
# ['twoXXXbbb', 'three999aaa']
#%%
l_start_not = [s for s in l if not s.startswith('t')]
print(l_start_not)
# ['oneXXXaaa', '000111222']


#4. 特定の文字列で終わる / 終わらない: endswith()

# 文字列メソッドendswith()は、文字列が引数に指定した文字列で終わるとTrueを返す。

#%%
l_end = [s for s in l if s.endswith('aaa')]
print(l_end)
# ['oneXXXaaa', 'three999aaa']

#5. 大文字・小文字で判定し抽出

# 文字列メソッドisupper(), islower()で文字列がすべて大文字か小文字かを判定できる。

#%%
l_lower = [s for s in l if s.islower()]
print(l_lower)
# ['three999aaa']

#%%
l_upper = [s for s in l if s.isupper()]
print(l_upper)
# []

#6. 大文字・小文字を変換

# すべての文字を大文字や小文字に変換したい場合は、文字列メソッドupper()やlower()を使う。
# そのほか、最初の一文字だけ大文字にするcapitalize()や、
# 大文字と小文字を入れ替えるswapcase()などもある。
#%%
l_upper_all = [s.upper() for s in l ]
print(l_upper_all)
# ['ONEXXXAAA', 'TWOXXXBBB', 'THREE999AAA', '000111222']

#%%
l_lower_to_upper = [s.upper() if s.islower() else s for s in l]
print(l_lower_to_upper)
# ['oneXXXaaa', 'twoXXXbbb', 'THREE999AAA', '000111222']

#7. 英字か数字か判定し抽出

# 文字列メソッドisalpha()やisnumeric()で、
# 文字列がすべて英字か数字かなどを判定できる。
#%%
l_isalpha = [s for s in l if s.isalpha()]
print(l_isalpha)
# ['oneXXXaaa', 'twoXXXbbb']

l_isnumeric = [s for s in l if s.isnumeric()]
print(l_isnumeric)
# ['000111222']

#8. 正規表現

# 正規表現を使うと自由度の高い処理が可能。

# まとめ
# ①内包表記と合わせて条件にあう要素を抽出するモジュールはたくさんある
