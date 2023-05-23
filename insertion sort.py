def Insertion_sort(list):
    """
    На первой итерации мы сортируем два элемента данных.
    Затем мы расширяем выборку: берем третий элемент и находим для него позицию согласно его значению. 
    Алгоритм выполняется до тех пор, пока все элементы не будут перемещены в правильное положение.
    """
    for i in range(1, len(list)):
        j = i - 1
        next_element = list[i]
        while list[j] > next_element and j >= 0: # сравниваем текущии элемент со следующим 
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = next_element
    
    return list

list = [2, 3, 45, 9, 6, 11, 34, 65, 23, 7]
print(Insertion_sort(list))