import  array

def leftRotate(arr,d,n):
    for i in range(d):
        leftRotatebyOne(arr,n)


def leftRotatebyOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i]= arr[i+1]
    arr[n-1] = temp

def printArray(arr,size):
    for i in range(size):
        print("%d" % arr[i], end=" ")

arr = [5,7,6,5,4,4,5,4]
leftRotate(arr,1,8)
printArray(arr,8)
