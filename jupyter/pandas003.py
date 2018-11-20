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
# は下記の通り記載が必要

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

#2. CSVファイルに保存する
# to_csvメソッドを使用して、作成したDataFrameをCSV形式で保存する

# データフレーム名.to_csv(ファイルパス)

# 保存の際にインデクスが自動的に保存される

#%%
sorted_df = csv_df.sort_values('点数')
sorted_df.to_csv('mydata_sort.csv')

# インデクスの自動付与が不要な場合には下記の通り第二引数に、index=Falseを付与

#%%
sorted_df = csv_df.to_csv('mydata_sort2.csv',index=False)

#3. excelファイルを利用する
#excelファイルの読み込みはread_excelメソッドを使用する

# 変数 = pd.read_excel('ファイルパス')

#%%
xl_df = pd.read_excel('mydata.xlsx')
xl_df[:5]
# 	教科	氏名	点数
# 0	国語	山田	13
# 1	数学	山田	54
# 2	英語	山田	37
# 3	理科	山田	74
# 4	社会	山田	54

# excelファイルに保存する場合には、to_excelメソッドを使用する

# データフレーム名.to_excel(ファイルパス)

#%%
sorted_df2 = xl_df.sort_values('教科')
sorted_df2.to_excel('mydata_to_excel.xlsx')

#4. タブ区切りのデータについて

# データを「,」ではなく「タブ」で区切ったテキストデータを読み込む場合には、
# read_tableメソッドを使用する

# 変数 = pd.read_table(ファイルパス)

# タブ区切りのテキストファイルへの保存は、直接テキストファイルにするメソッドはない
# to_csvメソッドを使用して、引数にsep='\t'を指定することで、可能
#%%
sorted_df3 = xl_df.sort_values('教科')
sorted_df3.to_csv('mydata_table.tsv', sep='\t', index=False )

#%%
