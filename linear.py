import array

def search(arr,n,x,y):
    for i in range(0,n):
        if(arr[i] == x and arr[i] == y):
            return i;
    return -1;



arr = [2,3,4,5,6];
x = 4;
y= 5;
n = len(arr);
result = search(arr,n,y,x)
if(result == -1):
    print("Element is not present in the array")
else:
    print("Searched Elements are : ",result)