m = int(input("inserte valor de m: "))
n = int(input("inserte valor de n: "))
q = input ("desea ver proceso de suma? [y/n] ")



sumatoria = 0

if m <= n :                 # "m" debe ser menor a "n"
    for i in range(m,n+1):  # para "i" en el rango minimo (m) y el maximo (n)
        cal = i*2           # calculo
        sumatoria = sumatoria + cal
        if q = "y"
         print (cal,i,sumatoria)
    print ("su resultado es:")
    print (sumatoria)
else:
    print (" 'm' debe ser menor que 'n' ")

