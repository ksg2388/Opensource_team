def Arr():
    arr1 = list(map(int, input("input the 1st list :").split()))
    arr2 = list(map(int, input("input the 2st list :").split()))
    result = []
    
    arr3 = arr1[:]
    for value in arr2:
        if value not in arr1:
            arr3.append(value)
    arr3.sort()
    print("union :", arr3)
    
    for value in arr1:
        if (value in arr2):
            result.append(value)
    result.sort()
    print("intersection :", result)
