def Bubble_sort(list):
    last_element = len(list) - 1
    for i in range(last_element, 0, -1):   # внешний цикл, проход по элиментам списка
        for indx in range(i):  # внутренний цикл, на каждом последующем проходе колличество сравненний будет уменьшаться на 1
            if list[indx] > list[indx+1]:
                list[indx], list[indx+1] = list[indx+1], list[indx]
    
    return list

print(Bubble_sort([1, 2, 44, 22, 12, 48, 5, 34]))