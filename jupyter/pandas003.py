## DataFrameとファイルアクセス

# pandasでは大量のデータをDataFrameでまとめて処理するため、
# ファイルなどに保存しておき、それを読み込んで利用するのが一般的

# 作成したデータはCSVフォーマットのファイルで保存する

# CSVファイルの読み込みにはread_csvメソッドを使用する

# 変数 = pd.read_csv(ファイルパス)
# # カレントディレクトリにファイルが保存されている場合には、パス指定はいらないが、
# # 別のディレクトリにある場合には、絶対パスを指定する
#%%
import pandas as pd 
csv_df = pd.read_csv('mydata.csv')
csv_df[:5]
# 	教科	氏名	点数
# 0	国語	山田	13
# 1	数学	山田	54
# 2	英語	山田	37
# 3	理科	山田	74
# 4	社会	山田	54

#　ヘッダ情報は容易されている場合には指定は必要ないが、データだけしか記載されていないときなどは
  は下記の通り記載が必要

# 変数 = pd.read_csv(ファイルパス, header=none, names=[列のラベル])

#%%
csv_df2 = pd.read_csv('mydata.csv',header=None, names=['A', 'B', 'C'])
csv_df2[:5]
# 	A	B	C
# 0	教科	氏名	点数
# 1	国語	山田	13
# 2	数学	山田	54
# 3	英語	山田	37
# 4	理科	山田	74
# 本来ヘッダであった行が、データとして表示されている

