def find_maximum_values(list):
    maximun_values = list[0]
    value = 0
    for i in range(len(list)):
        value = list[i]
        if value > maximun_values:
            maximun_values = value
            print(f"valor maximo de lista es: {maximun_values}")


list_int = [3,5,7,2,7,9]
find_maximum_values(list_int)