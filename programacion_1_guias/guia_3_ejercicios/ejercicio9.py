
def maximun_values(list):
    maximun_value = 5
    value = 0
    list_maximun = []
    for i in range(len(list)):
        value = list[i]
#        print(value)
        if value >= maximun_value:
            maximun_value = value
            list_maximun.append(maximun_value)
    print(f"los valores maximo de la lista son: {list_maximun}")

list_int = [4,7,1,7,8,1]
maximun_values(list_int)