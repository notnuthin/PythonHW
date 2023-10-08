def sort_dictionary(d):
    if isinstance(d, dict)!=True:
        raise TypeError("Variable provided is not a dictionary")
    
    dictKeys = list(d.keys())
    
    for i in range(1,len(dictKeys)):
        j=i-1
        current = dictKeys[i]
        while j>=0 and current>dictKeys[j]:
            dictKeys[j+1] = dictKeys[j]
            j=j-1
        dictKeys[j+1] = current

    returnList = []
    for i in range(0,len(dictKeys)):
        name = dictKeys[i]
        phone = d.get(name)[0]
        returnList.append((name,phone))

    return returnList
#print(sort_dictionary({ 'Tom' : (5464512, 24) , 'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)} ))


    