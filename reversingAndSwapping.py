def swapping(a):
    tempArr = []
    temp = a.swapcase()
    tempArr = temp.split()
    tempArr.reverse()
    return ' '.join(tempArr)

if __name__ == "__main__":
    STRING = "Coding is aWEsome"
    print(swapping(STRING))