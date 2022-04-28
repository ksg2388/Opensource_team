def Arr():
   arr1 = list(map(int, input().split()))
   print("input the 1st list :", arr1)
   arr2 = list(map(int, input().split()))
   print("input the 2st list :", arr2)

def union(arr1, arr2):
   for value in arr2:
      if value not in arr1:
         arr1.append(value)
   arr1.sort()
   print("union : ", arr1)

def intersection(arr1, arr2, result):
   for value in arr1:
      if value in arr2:
         result.append(value)
   result.sort()
   print("intersection : ", result)