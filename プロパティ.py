###プロパティ###
##データ属性の参照や設定に関する機能　　
#データ属性の設定をする際に値のチェックにより不正な値が設定できないように防止する
#class クラス名:
#   @property
#   def プロパティ名(self):
#       処理A
#   
#   プロパティ名.setter
#   def プロパティ名(self. 変数)：
#       処理B



class player:
    LEVEL_LIMIT = 10
        
    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, value):
        if value > player.LEVEL_LIMIT:
            value = player.LEVEL_LIMIT
        self.__level = value

p = player
p.level = 1000
print(p.level)




class player:
    LEVEL_LIMIT = 10
        
    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, value):
        if value < 1:
            value = 1
        if value > player.LEVEL_LIMIT:
            value = player.LEVEL_LIMIT
        self.__level = value

p = player
p.level = 0
print(p.level)
