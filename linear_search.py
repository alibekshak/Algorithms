def LinearSearch(list, item):
    """В каждой точке данных выполняется поиск совпадения. 
    При обнаружении искомых данных алгоритм возвращает результат и выходит из цикла.
    В противном случае он продолжает поиск до тех пор,
    пока не достигнет конца структуры данных."""
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

