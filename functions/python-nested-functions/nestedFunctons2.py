def pop(lista):
    def get_last_item(my_list):
        return my_list[len(list)-1] 

    lista.remove(get_last_item(lista))
    return lista

a = [1 ,2 ,3, 4, 5]
print(pop(a))
print(pop(a))
print(pop(a))