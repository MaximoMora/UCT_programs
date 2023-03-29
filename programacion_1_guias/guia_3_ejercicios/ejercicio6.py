def list_values(list):
    minimum_value = list[0]
    value = 0
    for i in range(len(list)):
        value = list[i]
#        print(value)
        if value < minimum_value:
            minimum_value = value
            print(f"es valor minimo es: {minimum_value}")

list_int = [2,4,7,2,9,1]
minimum_value = list_values(list_int)