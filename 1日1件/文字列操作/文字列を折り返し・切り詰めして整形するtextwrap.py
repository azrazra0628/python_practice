## 文字列を折り返し・切り詰めして整形するtextwrap

# Pythonで文字列を任意の文字数で折り返し（改行）、切り詰め（省略）して整形するには、
# 標準ライブラリのtextwrapモジュールを使う。

#1. 文字列を折り返し（改行） : wrap(), fill()

# textwrapモジュールの関数wrap()で、
# 任意の文字数に収まるように単語の切れ目で分割したリストが取得できる。

#%%
import textwrap
s = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages"

s_wrap_list = textwrap.wrap(s, 40)
print(s_wrap_list)
# ['Python can be easy to pick up whether', "you're a first time programmer or you're", 'experienced with other languages']

print('\n'.join(s_wrap_list))
# Python can be easy to pick up whether
# you're a first time programmer or you're
# experienced with other languages

# 関数fill()は、リストではなく改行された文字列を返す。
# 上の例のようにwrap()のあとで'\n'.join(list)するのと同じ。

#%%
print(textwrap.fill(s, 40))
# Python can be easy to pick up whether
# you're a first time programmer or you're
# experienced with other languages

# 引数max_lineを指定すると、それ以降の行数は省略される。

#%%
s_wrap_list2 = textwrap.wrap(s,40, max_lines=2)
print(s_wrap_list2)
# ['Python can be easy to pick up whether', "you're a first time programmer or [...]"]

print(textwrap.fill(s, 40, max_lines=2))
# Python can be easy to pick up whether
# you're a first time programmer or [...]


# 省略される場合、デフォルトでは' [...]'が最後に出力される。
# 引数placeholderで任意の文字列に置き換えることができる。
#%%
print(textwrap.fill(s, 40, max_lines=2, placeholder=' ~'))
# Python can be easy to pick up whether
# you're a first time programmer or ~

# また、引数initial_indentで最初の行の先頭に加えられる文字列を指定できる。
# 段落の最初に字下げしたい場合などに使う。

#%%
print(textwrap.fill(s, 40, max_lines=2, placeholder=' ~',initial_indent='  '))
#    Python can be easy to pick up whether
# you're a first time programmer or ~

# 注意点: 全角半角
# textwrapでは文字幅ではなく文字数で制御しており、半角も全角も一文字としてみなされる。




#2. 文字列を切り詰め（省略） : shorten()

# 文字列を切り詰めて省略したい場合は、textwrapモジュールの関数shorten()を使う。
# 任意の文字数に収まるように単語単位で省略される。省略を示す文字列
# （デフォルトでは' [...]'、引数placeholderで設定可能）も含めて任意の文字数に収まる

#%%
s = 'Python is powerful'

print(textwrap.shorten(s,12))
# Python [...]

print(textwrap.shorten(s, 12, placeholder=' ~'))
# Python is ~

#3. TextWrapper オブジェクト
# 決まった設定で何度もwrap()やfill() を行う場合は、
# TextWrapperオブジェクトを生成しておくと効率が良い。

#%%
wrapper = textwrap.TextWrapper(width=30, max_lines=3, placeholder=' ~', initial_indent='  ')

print(wrapper.wrap(s))
# ['  Python can be easy to pick', "up whether you're a first time", "programmer or you're ~"]

print(wrapper.fill(s))
#   Python can be easy to pick
# up whether you're a first time
# programmer or you're ~


# まとめ
# ①文字列を特定の条件で折り返したり、切り詰めたりしたい場合にはtextwarpモジュールを使用する
# ②何度も同じ条件で処理する場合にはtextwarpオブジェクトを作成しておくと便利


