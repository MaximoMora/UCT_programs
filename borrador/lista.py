import random


def crea_ruts():
    letra = ["1","2","3","4","5","6","7","8","9","k"]
    numeros = [1,2,3,4,5,6,7,8,9]
    create_rut = str(random.randint(19,22)) + '.' + str(random.choice(numeros)) + str(random.choice(numeros)) + \
          str(random.choice(numeros)) + '.' +str(random.choice(numeros)) + str(random.choice(numeros)) + \
          str(random.choice(numeros)) + '-' + random.choice(letra)
    return create_rut


file = open("ruts.txt","w")


for i in range(3):
    rut = crea_ruts()
    file.write



