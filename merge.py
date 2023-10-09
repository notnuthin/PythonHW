def merge_list(list1, list2):
    
    
    if isinstance(list1, list[int])==False:
        raise TypeError("First list is not a list of ints")
    if isinstance(list2,list[int])==False:
        raise TypeError("Second list is not a list of ints")
    list1.extend(list2)
    
    for i in range (0,len(list1)-1):
        min=list1[i]
        minIndex = i
        for j in range(i+1,len(list1)):
            if list1[j]<min:
                minIndex = j
                min = list1[j]
        temp = list1[i]
        list1[i] = min
        list1[minIndex]=temp

    return list1
            




# print(merge_list([1,2,3,],[1,2,4]))
# print(merge_list([1,5,9],[]))
# print(merge_list([1,5,3,7],[6,2,4]))
# print(merge_list([1,5,3,2],[2,1,4,5,6]))
# print(merge_list([],[]))

