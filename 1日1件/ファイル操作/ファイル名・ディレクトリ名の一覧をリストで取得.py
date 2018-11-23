## ファイル名・ディレクトリ名の一覧をリストで取得

# Pythonでファイル名、ディレクトリ名（フォルダ名）の一覧を取得するには
# osモジュールの関数os.listdir()を用いる。

# osモジュールは標準ライブラリに含まれているのでインストールは不要（importは必要）。


#1.ファイル名とディレクトリ名の両方の一覧を取得

# os.listdir()をそのまま使うと、ファイル名とディレクトリ名の両方のリストが返る。

#%%
import os
os.chdir(r'c:\Users\azraz\pythoncode\1日1件')
print(os.getcwd())

path = r"c:\Users\azraz\pythoncode\1日1件"

files = os.listdir(path)

print(type(files)) 
# c:\Users\azraz\pythoncode\1日1件

print(files)
# ['ファイル操作', 'リスト', '文字列操作']

#2.ファイル名のみの一覧を取得

# ファイル名のみの一覧を取得したい場合は、
# path がファイルかどうかを判定するos.path.isfile()とリスト内包表記を用いる。
# os.path.isfile()にファイル名だけ渡すとうまくいかないので、
# 以下のようにos.path.isfile(os.path.join(path, f))としてフルパスにして渡す。

#%%
files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
print(files_file) 
# ['test.txt']


#3. ディレクトリ名のみの一覧を取得

#%%
files = os.listdir(path)
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(files_dir)   
# ['ファイル操作', 'リスト', '文字列操作']

# まとめ
# ①標準モジュールのOsモジュールを使用し、ファイル・ディレクトリの情報を取得できる
# ②対象OSによりパスの指定がことなるので注意
