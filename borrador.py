

#x = [1,2,3,4]
#print("y = a*x+b")
#for i in range(len(x)):
#    a = int(input("El valor de a = "))
#    b = int(input("EL valor de b = "))
#    y = a*x[i]+b
#    print(f"El resultado de la ecuacion lineal y=ax+b es: {y}")


#for i in range(len(list_y)):
#    print(list_y[i])

#print(f"el promedio de la suma de la ecuacion lineal es: {sum_y/4}")
#sum_numbers= 0
#for i in range(5):
#    number = int(input("Dame un numero: "))
#    sum_numbers += number

#average = sum_numbers / 4
#print(f"promedio = {average}")

#e = 25
#for i in range(e):
#    if i * i == e:
#        print(f"la raiz de {e} es {i}")

#x_list = 1,2,3,4

#def root(number):
#    for i in range(number):
##        if root_number == number:
#            print(f"numero raiz de {number} es {i}")

#for i in range(len(x_list)):
x_list = [1,2,3,4]

def root(number):
    for i in range(int(number)):
        root_number = i * i
        if root_number == number:
            print(f"numero raiz de {number} es {i}")
            root_number = i
            return root_number
            break
    print("no hay raiz exacta")


for i in range(len(x_list)):
    user_a = int(input("a para la ecuacion cuadratica: "))
    user_b = int(input("b para la ecuacion cuadratica: "))
    user_c = int(input("c para la ecuacion cuadratica: "))
    y1 = (-user_b+root(25))/(2*user_a)
    y2 = (-user_b-root(25))/(2*user_a)
    x = user_a*x_list[i]**2+user_b*x_list[i]+user_c


print(f"EL resultado de la funcion cuadratica de a: {user_a} b: {user_b} c: {user_c}")
