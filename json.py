###json###
##データ形式の一つでプログラミング間でデータを交換する為に使用される
##配列##
# [値A, 値B, 値C]
##オブジェクト##
# [名前A:値A, 名前B:値B, 名前C:値C]
# 行を区切ってかける
# {
#     名前A: 値A,
#     名前B: 値B,
#     名前C: 値C
# }
##jsonとpythonのデータ構造は似ており、jsonモジュールを使えば、pythonのデータ構造を
##jsonい変換してファイルに書き込んだり、ファイルから読み込んだjsonをpythonの
##データ構造に変換したりといった処理が簡単に行うことができる

import json
menu = [
    {'name': 'ハンバーガー', 'price': 100, 'calorie': 260},
    {'name': 'チーズバーガー', 'price': 130, 'calorie': 310},
    {'name': 'フライドポテト', 'price': 150, 'calorie': 420}
]
with open('menu.txt', 'w') as  file:
    json.dump(menu, file, indent=4)

##ファイルから読み込んだjsonをpythonのデータ構造に変換

import json
with open('menu.txt', 'r') as file:
    menu = json.load(file)

print(menu)

