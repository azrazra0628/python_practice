catalog = [('blue', 'hat'), ('red', 'shirt'), ('green', 'socks')]
catalog

#enumerte関数  
for index, item in enumerate(catalog, 1):
    print(index, item)


#可変長引数　　
#個数を変更できる
#def 関数名(*引数):
#    処理
     
def test(*x):
    print(x)


def sum(*number):
    s = 0
    for n in number:
        s += n
    return s


sum(1, 2)
sum(1, 2, 5)

