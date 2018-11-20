## pandas.DataFrame, SeriesとPython標準のリストを相互に変換

# pandas.DataFrame, pandas.SeriesとPython標準のリスト型listは相互に変換できる

#1. リストをpandas.DataFrame, pandas.Seriesに変換

# それぞれのコンストラクタpandas.DataFrame(), pandas.Series()の引数に
# リスト型のオブジェクトを渡すと、リストを元にpandas.DataFrame, pandas.Seriesが生成される。

#%%
import pandas as pd

l_1d = [0, 1, 2]

s = pd.Series(l_1d)

print(s)
# 0    0
# 1    1
# 2    2
# dtype: int64
#%%
s = pd.Series(l_1d, index=['row1', 'row2', 'row3'])

print(s)
# row1    0
# row2    1
# row3    2
# dtype: int64

# 二次元配列からpandas.DataFrameを生成する例。引数indexで行名（行ラベル）、引数columnsで列名（列ラベル）を指定することもできる。二次元配列からpandas.DataFrameを生成する例。
# 引数indexで行名（行ラベル）、引数columnsで列名（列ラベル）を指定することもできる。
#%%
l_2d = [
    [0,1,2],
    [3,4,5]
    ]

df = pd.DataFrame(l_2d,index=['row1', 'row2'], columns=['col1', 'col2', 'col3'])
df

# col1	col2	col3
# row1	0	1	2
# row2	3	4	5

# ラベルと値がペアとなったリストからpandas.Seriesを生成する場合。
# ラベルの配列と値の配列に分解し、それをpandas.Series()の引数に渡す。

#%%
l_1d_index = [
    ['Alice', 0],
    ['Bob', 1],
    ['Charlie', 2]]

index, value = zip(*l_1d_index)
print(index)
# ('Alice', 'Bob', 'Charlie')
print(value)
# (0, 1, 2)

s_index = pd.Series(value, index=index)

print(s_index)
# Alice      0
# Bob        1
# Charlie    2
# dtype: int64

# 同様に、ラベルと複数の値からなるリストからpandas.DataFrameを生成する場合。
# 上述のpandas.Seriesのように配列を分解してもいいが、
# 全体を読み込んでからset_index()メソッドでindex列を指定したほうが簡単。

#%%
l_2d_index = [['Alice', 0, 0.0], ['Bob', 1, 0.1], ['Charlie', 2, 0.2]]

df_index = pd.DataFrame(l_2d_index, columns=['name', 'val1', 'val2'])
df_index
# name	val1	val2
# 0	Alice	0	0.0
# 1	Bob	1	0.1
# 2	Charlie	2	0.2

df_index_set = df_index.set_index('name')
df_index_set

# val1	val2
# name		
# Alice	0	0.0
# Bob	1	0.1
# Charlie	2	0.2

# 列ごとにデータ型dtypeが異なる場合も
# それぞれの列に最適なデータ型dtypeが自動で選ばれる。

#%%
print(df_index_set.dtypes)
# val1      int64
# val2    float64
# dtype: object

#2. pandas.DataFrame, pandas.Seriesをリストに変換

# pandas.DataFrame, pandas.Seriesをリスト型に直接変換するメソッドは無いため、
# values属性で取得できるNumPy配列ndarrayを経由して、
# ndarrayのtolist()メソッドでリストに変換する。

#%%
s = pd.Series([0, 1, 2])

print(s)
# 0    0
# 1    1
# 2    2
# dtype: int64

l_1d = s.values.tolist()
print(l_1d)
# [0, 1, 2]

#%%
df = pd.DataFrame([[0, 1, 2], [3, 4, 5]])
df

# 0	1	2
# 0	0	1	2
# 1	3	4	5

l_2d = df.values.tolist()
print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

# values属性ではラベル（行名、列名）があっても無視される。

#%%
s_index = pd.Series([0, 1, 2], index=['row1', 'row2', 'row3'])
print(s_index)
# row1    0
# row2    1
# row3    2
# dtype: int64

l_1d = s_index.values.tolist()
print(l_1d)
# [0, 1, 2]

#%%
df_index = pd.DataFrame([[0, 1, 2], [3, 4, 5]],
                        index=['row1', 'row2'],
                        columns=['col1', 'col2', 'col3'])

print(df_index)
#       col1  col2  col3
# row1     0     1     2
# row2     3     4     5

l_2d = df_index.values.tolist()

print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

# ラベルもリストのデータとして残したい場合は、
# reset_index()メソッドでindex列をリセットしてデータ列にする。

#%%
l_1d_index = s_index.reset_index().values.tolist()
print(l_1d_index)
# [['row1', 0], ['row2', 1], ['row3', 2]]

# 列名（列ラベル）をリセットするメソッドは無いため、pandas.DataFrameで行名も列名もリストのデータとして残したい場合は、reset_index()メソッドを適用したあと.
# Tで転置して再度reset_index()メソッドを適用し、さらに.Tで元に戻す。

#%%
l_2d_index = df_index.reset_index().T.reset_index().T.values.tolist()
print(l_2d_index)
# [['index', 'col1', 'col2', 'col3'], ['row1', 0, 1, 2], ['row2', 3, 4, 5]]

# まとめ
# ①DataFrameやSeriesを1次元リストや2次元リストにする場合には、直接はできないので、
#  valuesでとりだして、リストにする
# ②2次元リストで、列名やインデクスもリストにしたい場合はちょっとめんどくさい


