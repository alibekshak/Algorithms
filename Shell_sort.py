def ShellSort(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            # сортировка подсписка 
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j - distance
            list[j] = temp
        # уменьшение растояния до сдедующего элемента 
        distance = distance // 2
    return list

list = [1, 44, 64, 3, 77, 29, 10, 5, 23, 17, 63, 97]
print(ShellSort(list))
