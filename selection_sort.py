def Selection_sort(list):
    """В результате первого прохода наибольшее значение окажется справа, 
    а в результате второго прохода к нему переместится следующее по величине значение."""
    for slot in  range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[slot], list[max_index] = list[max_index], list[slot]

list = [60, 11, 73, 25, 5, 32]
Selection_sort(list)
print(list)
