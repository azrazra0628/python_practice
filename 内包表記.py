###内包表記###

a = []
for x in range(1, 10):
    a.append(x ** 2)

a
#上記リスト作成プログラムを内包表記で簡潔に記述可能
#[式 for 変数 in イテラブル]

a = [x ** 2 for x in range(1, 10)]
a

[x ** 3 for x in range(1, 10)]

#if文と組み合わせて条件に合う値だけをリストに追加することができる
#[式 for 変数 in イテラブル if 条件]

[x for x in range(1, 10) if x % 3 == 0]

##内包表記を使って辞書やリストの作成も可能

#三項演算子
#条件がtrueの時にはtrueの値、falseの時にはfalseの値を返す
# trueの値 if 条件 else falseの値

['Fizz' if x % 3 == 0 else x for x in range(1, 10)]
