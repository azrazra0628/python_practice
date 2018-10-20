#global文書かない場合
def cat():
    pet = 'cat'

pet = 'dog'
cat()
print(pet)

#global文書かくと…
def cat():
    global pet
    pet = 'cat'

pet = 'dog'
cat()
print(pet)


#nonlocal文
def dog():
    def cat():
        nonlocal pet
        pet = 'cat'

pet = 'dog'
cat()
print(pet)

dog()

