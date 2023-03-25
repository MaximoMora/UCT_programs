#11

list_numbers = []

for i in range(5):
    user_number = int(input("dame un numero: "))
    list_numbers.append(user_number)
    if list_numbers[i] % 2 == 0:
        print("es par")
    else:
        print("es impar")

#12

for i in range(1):
    price = int(input("precio del producto: "))
    descount = int(input("cual es el porcentaje de descuento: "))
    descount_float = descount / 100
    final_price = price - (price * descount_float)

print(f"El precio de producto es {price} su descuento es {descount} el precio final es {final_price}")

#13
count_a = 0
for i in range(1):
    word = input("palabra: ")
    for k in word:
        if str(k) == "a":
            count_a += 1

print(f"la cantidad de veces de la letra a en la palabra {word} es {count_a}")

#14
for i in range(1):
    number_1 = int(input("numero 1: "))
    number_2 = int(input("numero 2: "))
    cociente = number_1 / number_2
    rest = int(number_1 % number_2)
    print(rest)
    print(f"el cociente de {number_1} / {number_2}  es {cociente}")
    print(f"el resto de la division {number_1} / {number_2}  es {rest}")


#15
list_number = []
for i in range(5):
    number_user = int(input("numero: "))
    list_number.append(number_user)
    max_number = 0
    minimun_number = max_number
    if number_user > max_number:
        max_number = number_user
    
    if number_user < minimun_number:
        minimun_number = number_user
    
print(f"la lista {list_number} su numero mayor es {max_number} y su numero menor es {minimun_number}")

#reto 1

word_user = input("palabra: ")
if word_user == word_user[::-1]:
    print("palindromo")
else:
    print("no es un palindromo")

#reto 2
user_number = int(input("numero: "))
for i in range(user_number):
    print(user_number)
    x = user_number



