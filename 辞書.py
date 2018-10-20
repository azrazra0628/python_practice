####辞書####
#辞書の特徴
#格納する要素はキーと値のペアでキーは重複できない
#順序の指定はできず、インデクスやスライスは使用できない
#指定したキーの要素を素早く取り出し、検索にはハッシュが使用される

#辞書の作成
#{キー:値, キー:値, …}

topping = {'bacon':210, 'mushroom':140, 'onion':100, 'tomato':130}
topping

#要素の取得
#辞書[キー]

topping['bacon']

#for文を用いて辞書のすべてのキーを取り出すことができる
for key in topping:
    print(key)

#すべてのキーと値のペアを取り出すにはitemsメソッドを利用する
#for 変数A, 変数B in 辞書.items():
#    処理

for key, value in topping.items():
    print(key, value)

#要素の追加または変更　辞書はミュータブルなので、要素の追加、変更、削除が可能
#辞書[キー] = 値

topping['cheese'] = 160
topping

topping['tomato'] = 150
topping

#要素の削除
#del 辞書[キー]

del topping['bacon']
topping

#可変長引数と辞書

def test(**y):
    print(y)

test(a=4, b=5)



