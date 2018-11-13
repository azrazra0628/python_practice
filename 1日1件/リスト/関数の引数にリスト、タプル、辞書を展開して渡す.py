## 関数の引数にリスト、タプル、辞書を展開して渡す
# Pythonではリスト（配列）、タプル、辞書を展開して、
# それぞれの要素を関数の引数にまとめて渡すことができる。

# 関数呼び出し時に、リストとタプルには*、辞書には**をつけて引数に指定する。


# 1.リストやタプルに*を付けて展開
# リストlistやタプルtupleに*を付けて引数に指定すると、
# 展開されてそれぞれの要素が個別の引数として渡される。
#%%
def func(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

l = ['one', 'two', 'three']

func(*l)
# one
# two
# three

func(*['one', 'two', 'three'])
# one
# two
# three

t = ('one', 'two', 'three')
func(*t)
# one
# two
# three

func(*('one', 'two', 'three'))
# one
# two
# three

# 要素数と引数の数が一致していないとエラーTypeErrorになる。
#%%
func(*['one', 'four'])
# TypeError: func() missing 1 required positional argument: 'arg3'

# 2.デフォルト引数が設定されている関数の場合

# デフォルト引数が設定されている場合、要素数が足りないとデフォルト引数が使われる。
# 要素数が多いとエラーTypeError。

#%%
def func_default(arg1=1, arg2=2, arg3=3):
    print(arg1)
    print(arg2)
    print(arg3)

func_default(*['one', 'four'])
# one
# two
# 3

func_default(*['one', 'two', 'three', 'four'])
# TypeError: func_default() takes from 0 to 3 positional arguments but 4 were given

# 3.可変長引数が設定されている関数の場合
# 可変長引数が設定されている場合、
# 位置引数分の要素以降の要素がすべて可変長引数に渡される。

#%%
def func_args(arg1, *args):
    print(arg1)
    for arg in args:
        print(arg)

func_args(*['one', 'two'])
# one
# two

func_args(*['one', 'two', 'three'])
# one
# two
# three

func_args(*['one', 'two', 'three', 'four'])
# one
# two
# three
# four

# 4.辞書に**を付けて展開

# 辞書dictに**を付けて引数に指定すると、要素のキーkeyが引数名、
# 値valueが引数の値として展開されて、それぞれ個別の引数として渡される。
#%%
def func(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

d = {'arg1': 'one', 'arg2': 'two', 'arg3': 'three'}

func(**d)
# one
# two
# three

# 引数名と一致するキーが無かったり、一致しないキーがあったりするとエラーTypeErrorになる。

#%%
func(**{'arg1': 'one', 'arg2': 'two'})
# TypeError: func() missing 1 required positional argument: 'arg3'

func(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three', 'arg4': 'four'})
# TypeError: func() got an unexpected keyword argument 'arg4'

#5. 可変長引数が設定されている関数の場合
# 可変長引数が設定されている場合、
# 引数として指定されている引数名以外のキーを持つ要素はすべて可変長引数に渡される。

#%%
def func_kwargs(arg1, **kwargs):
    print('arg1', arg1)
    for k, v in kwargs.items():
        print(k, v)

func_kwargs(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three'})
# arg1 one
# arg2 two
# arg3 three

func_kwargs(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three', 'arg4': 'four'})
# arg1 one
# arg2 two
# arg3 three
# arg4 four

func_kwargs(**{'arg1': 'one', 'arg3': 'three'})
# arg1 one
# arg3 three

# まとめ
# ①リストやタプルを展開して関数の引数として渡す場合には*を引数の前につける
# ②辞書の場合は**をつける
# ③要素が足りなかったり、多かったりしたときにエラーとなるので、可変長引数を使うとよい

