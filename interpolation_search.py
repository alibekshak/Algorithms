from bubble_sort import Bubble_sort

def IntpolSearch(list, item):
    """Бинарный поиск основан на логике, 
    согласно которой он сосредотачивается на средней части данных.
    Интерполяционный поиск более сложен. 
    Он использует целевое значение для оценки положения элемента в отсортированном массиве.
    Массив необходимо упорядочить с помощью алгоритма сортировки."""
    first = 0
    last = (len(list) - 1)
    found = False
    while first <= last and item >= list[first] and item <= list[last]:
        # Срединная тока
        mid = first + int(((float(last - first)/(list[last] - list[first])) * (item - list[first])))

        # Сравниваем значения в середине точки с о значением поиска
        if list[mid] == item:
            found = True
            return found
        if list[mid] < item:
            first = mid + 1 
    return found

list = [2, 45, 7, 23, 65, 9]
sort_list = Bubble_sort(list)
print(IntpolSearch(list, 45))
print(IntpolSearch(list, 8))