###正規表現###
##文字列のパターンを記述するためのもの。
#「0~9までの数字が7つ続く」
[0-9]{7}
r'[0-9]{7}'


##文字列の先頭部分がパターンにマッチしているか調べる
# re.match(パターン, 文字列)

import re
re.match(r'[0-9]{7}', '1234567')

#<re.Match object; span=(0, 7), match='1234567'>が表示される
#match関数を呼び出したときにパターンが文字列にマッチしていると、戻り値のマッチオブジェクトが表示される

##パターンマッチを行う関するは以下の通り
# match   文字列の先頭部分にマッチ
# search  文字列の任意部分にマッチ
# fullmatch 　文字列の全体にマッチ

r'[0-9]{3}-[0-9]{4}'

import re
re.fullmatch(r'[0-9]{3}-[0-9]{4}', '123-4567')

#<re.Match object; span=(0, 8), match='123-4567'>が表示される

##文字列のパターンマッチを確認する
##「8文字以上で、英小文字、英大文字、数字をすべて使う」
# (?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[0-9][a-zA-Z0-9]{8,})
# (?=.*[A-Z])    英大文字が使われている
# (?=.*[a-z])　　英子文字が使われている
# (?=.*[0-9])    数字が使われている
# [a-zA-Z0-9]　　英小文字、英大文字、数字のいずれか1文字
# {8,}　　　　　　直前の文字が8文字以上続く

pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[a-zA-Z0-9]{8,}'

re.match(pattern, 'Konsai123')
re.match(pattern, 'wadasatoshi')

import re
import sys
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[a-zA-Z0-9]{8,}'
if re.fullmatch(pattern, sys.argv[1]):
    print('good password')
else:
    print('bad password')

