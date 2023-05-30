def LinearSearch(list, item):
    index = 0 
    found = False
    # Сравниваем значения с каждым элементом данных
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else: 
            index += 1
    return found

list = [23, 3, 4, 11, 6, 80, 19]
print(LinearSearch(list, 3))
print(LinearSearch(list, 10))

