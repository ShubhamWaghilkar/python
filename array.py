import array
arr = array.array('i',[1,2,3])

print ("Newly created array : ", end=" ")
for i in range(0,3):
    print(arr[i] , end = " ")
print("\r")

arr.append(10)
print("appended array :", end=" ")
for i in range(0,4):
    print(arr[i], end=" ")
print("\r")

arr.insert(2,5)
print("After insertion :" , end=" ")
for i in range(0,5):
    print(arr[i], end= " ")
print("\r")

arr.pop(3)
print("After popping :", end=" ")
for i in range(0,4):
    print(arr[i], end=" ")
print("\r")

print("Index of current element :")
print(arr.index(2))
for i in range(0,4):
    print(arr[i], end=" ")
print("\r")