###ファイル入出力###
##プログラムの実行結果をファイルに出力することができる　　以下のようなプログラム
# (1)ファイルを開く
# (2)ファイルにデータを書き込む
# (3)ファイルを閉じる

##ファイルを開くにはopen関数を使う
# 変数 = open(ファイル名, 'w')
file = open('greeting.txt', 'w', encoding='utf_8')
file.write('お久し振りです。\nお元気ですか。\n')
file.close()

##ファイルに書き込みを行った場合にはとじる必要がある
##with文を組み合わせると、closeメソッドの呼び出しが不要
# with open(ファイル名, 'w', encoding='文字エンコーディング') as 変数:
#     ファイルへの書き込み処理

with open('neko.txt', 'w', encoding='shift_jis') as file:
    file.write('猫です。\n犬じゃありません\n')

##ファイル読み込み
# with open(ファイル名, 'r', encoding='文字エンコーディング') as 変数:
#     ファイルの読み込み処理
##変数にファイルオブジェクトが代入されているときに、そのファイルを読み込んで、
##文字列として返す
# 変数.read()

with open('neko.txt', 'r', encoding='shift_jis') as file:
    text = file.read()

text
##書き込み時と読み込み時で同じ文字エンコーディングを指定する必要がある

