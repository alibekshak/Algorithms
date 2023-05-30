def BinarySearch(list, item):
    """Алгоритм итеративно делит список на две части
    и отслеживает самые низкие и самые высокие индексы, 
    пока не найдет искомое значение."""
    first = 0 
    last = len(list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

list = [23, 44, 5, 8, 11, 92, 79]
print(BinarySearch(list, 44))
print(BinarySearch(list, 1))
