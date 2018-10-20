###オブジェクト指向###

##クラスとは　　データと操作をまとめた構造のこと

#class クラス名:     #命名規則は以下の通り
#半角の英文字を使用する
#クラスの２文字目以降は半角の数字を使用することもある
#英単語の区切りは各単語の先頭を大文字にする

##メソッドとは　　　操作のこと　各インスタンス毎に共通のメソッドを使用する
#クラスの内側はインデントしてメソッドの定義を記述する

#class クラス名:
#   def メソッド名(self, 引数, …):
#        処理

##クラスと関数の組み合わせも可能だが、名前の衝突を避けるため

class player:
    def display(self):
        print('name:', self.name)
        print('Level:', self.level)

##インスタンス　クラスで定義した構造をメモリ上に生成したもの
#インスタンスの生成
#クラスで定義したデータ属性を保存するためのメモリを確保し、データ属性の地を書き込むこと
# 変数 = クラス名()

#データ属性の参照
#変数.データ属性名

#データ属性の変更
#変数.データ属性名 = 値

#メソッドの呼び出し
#変数.メソッド名(引数, …)

p1 = player()
p1.name = 'satoshi'
p1.level = 1
p1.display()

#一つのクラスを使って複数のインスタンスの作成が可能

p2 = player()
p2.name = 'satoshi'
p2.level = 35
p2.display()

#クラスは設計図、インスタンスは設計図から生成された製品に相当する


##__init__メソッド
#インスタンスの生成と同時にデータ属性の設定ができる
#class クラス名:
#   def __init__(self, 引数, …):
#       self.データ属性名 = 値

class player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display(self):
        print('Name:', self.name)
        print('Level', self.level)

#__init__メソッドを使用したインスタンスの生成
#変数 = クラス名(引数, …)

p1 = player('satoshi', 1)
p1.display()

p2 = player('neko', 2)
p2.display()

##メソッドの追加
#クラスには複数のメソッドが追加可能

class player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def display(self):
        print('Name:', self.name)
        print('Level:', self.level)
    
    def level_up(self, number):
        self.level += number

p1 = player('satoshi', 1)
p1.level_up(2)
p1.display()

##マングリング
#メソッドはクラスの外部かも呼び出しが可能だが、クラスの内部だけで使うメソッドを定義
#__メソッド名とすることで、自動的に「_クラス名__メソッド名」という名前に変換される

class player:
    LEVEL_LIMIT = 10
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def display(self):
        print('Name:', self.name)
        print('Level:', self.level)
    
    def level_up(self, number):
        self.level += number
        self.__check_level()
    
    def __check_level(self):
        if self.level > player.LEVEL_LIMIT:
            self.level = player.LEVEL_LIMIT


p1 = player('satoshi', 1)
p1.level_up(2)
p1.display()
 
##定数##
#複数個所で使う値は変数や定数にする　　定数とは変更しない値のこと
#半角英大文字で記載する
#英単語の区切りはアンダーバーで示す


##継承##
#既存クラスを拡張して既存クラスの持つすべての機能を引き継いで定義すること
#class 派生クラス名(基底クラス名):
#   メソッドや変数の定義
#基底クラスにあるメソッドを派生クラスで再定義することをオーバーライドという

#基底クラスのメソッドの呼び出しは以下のとおり
#基底クラス名.メソッド名(self, 引数, …)

class player:
    LEVEL_LIMIT = 10
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def display(self):
        print('Name:', self.name)
        print('Level:', self.level)
    
    def level_up(self, number):
        self.level += number
        self.__check_level()
    
    def __check_level(self):
        if self.level > player.LEVEL_LIMIT:
            self.level = player.LEVEL_LIMIT

class fighter(player):
    def __init__(self, name, level, sword):
        player.__init__(self, name, level)
        self.sword = sword
    
    def display(self):
        player.display(self)
        print('Sword:', self.sword)
    
    def slash(self):
        print('slashing!')

class wizard(player):
    def __init__(self, name, level, wand):
        player.__init__(self, name, level)
        self.wand = wand
    
    def display(self):
        player.display(self)
        print('Wand:', self.wand)
    
    def magic(self):
        print('Casting a magic!') 


f = fighter('neko', 1, 'iron')
f.display()
f.slash()

w = wizard('inu', 3, 'wood')
w.display()
w.magic()

##多重継承##
#派生クラスを定義する際に複数の基底クラスを指定することができる
#class 派生クラス名.(基底クラス名, 基底クラス名, …)
#   メソッドや変数の定義

class MagicKnight(fighter, wizard):
    def __init__(self, name, level, sword, wand):
        player.__init__(self, name, level)
        self.sword = sword
        self.wand = wand
    
    def display(self):
        player.display(self)
        print('Sword:', self.sword)
        print('Wand:', self.wand)

mk = MagicKnight('wada', 1 ,'silver','glass')
mk.display()
mk.slash()
mk.magic()


