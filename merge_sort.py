def MergeSort(list):
    """
    Алгоритм рекурсивно разбивает данные на две части до тех пор, 
    пока размер данных не станет меньше определенного порогового значения. 
    На этапе слияния алгоритм объединяет данные, 
    пока мы не получим окончательный результат.
    """
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        MergeSort(left) # повторяется пока длина каждого list не достигнет 1
        MergeSort(right)

        # объединеие, отсортированных частей в список 
        a = 0
        b = 0 
        c = 0 
        while a < len(left) and b < len(right): 
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
    return list

list = [22, 1, 43, 16, 7, 90, 74, 39, 6, 11]
print(MergeSort(list))


