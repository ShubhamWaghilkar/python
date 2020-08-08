def fact(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
        print(fac)
    return fac

def fac_rec(n):
    if n == 1:
        return 1
    else:
        return n * fac_rec(n-1)


num = int(input("Enter number \n"))
print(fac_rec(num))