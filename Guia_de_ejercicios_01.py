#1. Solicite la distancia que viaja un bus en kilómetros y el tiempo
#que le lleva recorrer esa distancia. Calcular y mostrar la velocidad media del bus.

user_distance = int(input("Cuanto es tu velocidad en kilometros: "))
user_time = int(input("Cuanto es tu tiempo en horas: "))
speed = user_distance / user_time
print(f"Entonces mas a {speed} kilometros por hora")

#2. Solicite un numero con decimales y evalué el siguiente polinomio 3*x**4-10*x**3+21.

user_number = float(input("Dame un numero con decimales: "))
polynomial = 3*user_number**4-10*user_number**3+21
print(f"El resultado de tu polinomio es: {polynomial}")

#3. Pedir la edad en años y muestre la edad en días.
user_age = int(input("Dame tu edad: "))
user_age_days = user_age * 365
print(f"Tu edad en dias es {user_age_days}")

# 4. Pedir el lado del cuadrado y mostrar el perímetro y el área

user_side_square = int(input("Dame el lado de un cuadrado: "))
square_perimeter = user_side_square * 4
square_area = user_side_square * user_side_square
print(f"EL lado del cuadrado es {user_side_square}, su perimetro es {square_perimeter} y su area es {square_area}")

#5. Pedir los lados del rectángulo y calcular perímetro y área.

user_long_rectangle = int(input("Dame el largo del rectangulo: "))
user_broad_rectangle = int(input("Dame el ancho del rectangulo: "))
rectangle_perimeter = 2*(user_long_rectangle+user_broad_rectangle)
rectangle_area = user_long_rectangle * user_broad_rectangle
print(f"El lado del rectangulo es {user_long_rectangle} y ancho {user_broad_rectangle} '/n', su perimetro es {user_side_square} y su area es {rectangle_area}")

#6. Pedir el radio del círculo y mostrar el perímetro y el área.

user_radio = int(input("Dame el radio de un circulo: "))
circle_perimeter = user_radio * 2
circle_area = user_radio **2
print(f"EL radio del circulo es {user_radio}, y su perimetro {circle_perimeter} es y su radio {circle_area}")

#7. Pedir base y altura para calcular área de triangulo rectángulo

triangule_base = int(input("Dame la base del triangulo: ")) 
triangule_height = int(input("Dame la altura: "))
trinagule_area = (triangule_base * triangule_height) / 2
print(f"La area de un tringulo de base {triangule_base}  y altura {triangule_height} ")

#8. Dada la ecuación lineal y=ax+b, pida por teclado a y b y calcule "y" para x=1,2,3,4 muestrelos resultados por pantalla.

x = [1,2,3,4]
print("y = a*x+b")
for i in range(len(x)):
    a = int(input("El valor de a = "))
    b = int(input("EL valor de b = "))
    y = a*x[i]+b
    print(f"El resultado de la ecuacion lineal y=ax+b es: {y}")

#9. Agregue al ejercicio anterior que sume los valores de "y", muestre ese total y saque elpromedio.

x = [1,2,3,4]
sum_y = 0
list_y = []
for i in range(len(x)):
    a = int(input("El valor de a = "))
    b = int(input("EL valor de b = "))
    y = a*x[i]+b
    list_y.append(y)
    sum_y += list_y[i]
    print(f"El resultado de la ecuacion lineal y=ax+b es: {y}")

print("Los numeros producto de la ecuacion lineal son: ")
for i in range(len(list_y)):
    print(list_y[i])

print(f"el promedio de la suma de la ecuacion lineal es: {sum_y/4}")

#10. Dada la ecuación cuadrática ax2+bx+c=0 y sabiendo 
#que y1=(-b+ raíz(b2-4ac))/(2a) y y2=(-b-raíz(b2-4ac))/(2a), pida a, b, c y calcule para x=1,2,3,4

x_list = [1,2,3,4]

def root(number):
    for i in range(int(number)):
        root_number = i * i
        if root_number == number:  
            root_number = i
            return root_number
            break
    print("no hay raiz exacta")


for i in range(len(x_list)):
    user_a = int(input("a para la ecuacion cuadratica: "))
    user_b = int(input("b para la ecuacion cuadratica: "))
    user_c = int(input("c para la ecuacion cuadratica: "))
    y1 = (-user_b+root(user_b**2-4*user_a*user_c))/(2*user_a)
    y2 = (-user_b-root(user_b**2-4*user_a*user_c))/(2*user_a)
    x = user_a*x_list[i]**2+user_b*x_list[i]+user_c
    y = root(25)
    a = []
    if y >= 0:
        a = ["tiene 2 vertices",2]
    elif y == 0:
        a = ["tiene solo un vertice",1]
    else:
        a = ["no tiene un punto fijo en el plano",0]

    print(f"Los valores son a={user_a} b={user_b} c={user_c}")
    print("La funcion cuadratica a*x**2+b*x+c")
    print(f"El tipo de funcion {a[0]} ")
    if a[0] == "tiene 2 vertices":
        print(f"Los valores de y1: {y1} y de y2={y2}")
    elif a[1] == "tiene solo un vertice":
        print(f"EL unico valor y1 y y2 = {y1}")
    else:
        print("no tiene un punto prederterminao")


#11. Dado el año de nacimiento de una persona calcule la edad al año actual.

year = 2023
user_born = int(input("Que año naciste: "))
print(f"La edad que tienes es = {year-user_born}")

#12. Lea 5 números y calcule el promedio.

sum_numbers= 0
for i in range(5):
    number = int(input("Dame un numero: "))
    sum_numbers += number

average = sum_numbers / 4
print(f"promedio = {average}")


