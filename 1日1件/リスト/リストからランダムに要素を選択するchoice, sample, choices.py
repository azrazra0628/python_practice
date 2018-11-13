## リストからランダムに要素を選択するchoice, sample, choices

# n標準ライブラリのrandomモジュールの関数choice(), sample(), choices()を使うと、
# リストやタプル、文字列などのシーケンスオブジェクトから
# ランダムに要素を選択して取得（ランダムサンプリング）できる。

# 1.ランダムに要素を一つ選択: random.choice()

# randomモジュールの関数choice()で、
# リストからランダムで要素が一つ選択され取得できる。

#%%
import random

l = [0, 1, 2, 3, 4]

print(random.choice(l))
#　ランダムで要素のうちの1つが抽出される

# タプルや文字列でも同様。文字列の場合は一文字が選択される。

#%%
print(random.choice(('xxxxx', 'yyyyyy', 'zzzzz')))

#%% 
print(random.choice('abcde'))

# 空のリストやタプル、文字列を引数として指定するとエラー。

#%%
print(random.choice([]))
# IndexError: Cannot choose from an empty sequence

#2. ランダムに複数の要素を選択（重複なし）: random.sample()

# randomモジュールの関数sample()で、
# リストからランダムで複数の要素を取得できる。要素の重複はなし（非復元抽出）。

# 第一引数にリスト、第二引数に取得したい要素の個数を指定する。リストが返される。

#%% 
import random

l = [0, 1, 2, 3, 4]

print(random.sample(l,2))
# 第一引数のリストから第2引数で指定した数抽出する

# 第一引数に指定したリストの要素数を超える値だとエラーとなる。

#%%
print(random.sample(l, 10))
# ValueError: Sample larger than population or is negative

# 第一引数をタプルや文字列にした場合も返されるのはリスト。

#%%
print(random.sample(('xxxx', 'yyyyyy', 'zzzzz'), 2))
# ['yyyyyy', 'zzzzz']

#%%
print(random.sample('abcde', 2))
# ['d', 'c']

# タプルや文字列に戻したい場合はtuple(), join()を使う。

#%%
print(tuple(random.sample(('xxxx', 'yyyyyy', 'zzzzz'), 2)))
# ('xxxx', 'yyyyyy')

#%%

print(''.join(random.sample('abcde', 3)))
# aeb

#3. ランダムに複数の要素を選択（重複あり）: random.choices()

# randomモジュールの関数choices()で、リストからランダムで複数の要素を取得できる。
# sample()とは異なり、要素の重複を許して選択される（復元抽出）。
# choices()はPython3.6から追加された関数。それより前のバージョンでは使えない。

# 重複が認められているので、取得する要素数kを元のリストの要素数より大きくすることもできる。

#%%
import random

l = [0, 1, 2, 3, 4]
print(random.choices(l,k=3))
# [1, 3, 3]

print(random.choices(l,k=10))
# [2, 1, 4, 0, 2, 4, 0, 0, 0, 0]

# kのデフォルトは1。省略した場合は要素数1のリストが返される。
#%%
print(random.choices(l))

# 引数weightsでそれぞれの要素が選ばれる重み（確率）を指定できる。
# 0にするとその要素は選ばれない。
#%%
print(random.choices(l,weights=[1, 1, 1, 10, 1], k=3))
# [1, 3, 3]

#引数cum_weightsに累積的な重みとして指定することもできる
#%%
print(random.choices(l, k=3, cum_weights=[1, 2, 3, 13, 14]))
#上のweightと等価

#　引数weightsまたはcum_weightsの長さ（要素数）が元のリストと異なるとエラーが発生する。
#%%
print(random.choices(l, k=3, weights=[1, 1, 1, 10, 1, 1, 1]))
# ValueError: The number of weights does not match the population

# まとめ
# ①ランダムに要素を抽出するには,choice,sample,choicesを使う
# ②choices関数は、重みづけをして使用することも可能


