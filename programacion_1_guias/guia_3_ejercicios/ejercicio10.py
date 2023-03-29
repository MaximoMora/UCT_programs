
def list_multiply(list_int):
    for i in range(len(list_int)):
        value = list_int[i] * 1/2
        list_int[i] = value
    print(list_int)

list_user = [2,4,6,8]
list_multiply(list_user)