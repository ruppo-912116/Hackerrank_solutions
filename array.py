arrayList = [ [2,4,5,6,7], [1,2,4,5,8] ]

#main algorithm for filtering the common elements
def commonElement(arrayList):
    tmp = []

    for a in arrayList[0]:
        for b in arrayList[1]:
            if (a == b):
                tmp.append(a)
    return tmp

print(commonElement(arrayList))

