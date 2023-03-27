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
    y1 = (-user_b+root(user_b**2)-(4*user_a*user_c))/(2*user_a)
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
