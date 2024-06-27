user_input = input("Введите элементы списка, разделенные пробелом: ")


items_list = user_input.split()


if len(items_list) == len(set(items_list)):
    print("Повторяющихся значений нет.")
else:
    print("Есть повторяющиеся значения.")
