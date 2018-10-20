###ジェネレータ式###
#内包表記と似ているが（）で囲むことで処理が高速なので整数が大きくなる場合はジェネレータ式にする
#(式 for 変数 in イテラブル)

number = (x for x in range(10000))
for n in number:
    print(n)

#ジェネレータ　関数に似ているが、yield文を使って複数の値を順番に生成する
#yield 値

def do_yield():
    yield 1
    yield 2
    yield 'Fizz'
    yield 4
    yield 'Buzz'

do_yield

for i in do_yield():
    print(i)

list(do_yield())

#FizzBuzzゲーム

def fizzbuzz(n):
    for x in range(1, n):
        if x % 15 == 0:
            yield 'FIzzBuzz'
        elif x % 5 == 0:
            yield 'Buzz'
        elif x % 3 == 0:
            yield 'Fizz'
        else:
            yield x


print(list(fizzbuzz(50)))

