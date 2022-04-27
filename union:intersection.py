#union/intersection
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = [] # 중복 제거된 값들이 들어갈 리스트

print("input the 1st list :", arr1)
print("input the 2nd list :", arr2)

for value in arr2:
   if value not in arr1:
      arr1.append(value)
arr1.sort()

print("union : ",arr1)

for value in arr1:
   if value in arr2:
      result.append(value)

print("intersection : ", result)