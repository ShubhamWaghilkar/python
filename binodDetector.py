import os
def isBinod(filename):
    with open(filename,"r") as f:
        contents = f.read()

        if "binod" in contents.lower():

            return True
        else:
            return False




if __name__ == '__main__':
    nBinod = 0
    li = os.listdir()
    for item in li:
        if item.endswith('txt'):
            print(item)
            flag = isBinod(item)

            if(flag):
                print(f"Binod in {item}")
                nBinod +=1
            else:
                print(f"Binod not found in {item}")
    print(f"Binod dected Summary")
    print(f"{nBinod} files found with Binod")