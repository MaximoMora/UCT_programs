m_number = int(input("m inicio: "))
n_number = int(input("n final: "))
total = 0
for i in range(m_number,n_number+1):
    print(i)
    total += i * 2
    print(i,total)
    
print(total)


#problema 1

def funcion(x):
    return 2*(x+5) + 2

problema1 = funcion(3)
print(problema1)

#problema 2

price = int(input("precio: ")) 
iva = 19

final_price = price * 0.81
print(int(final_price))


    