testList = [0, 5, 4, 8, 1, 9, 7, 3, 6, 2]

def quicksort(listToSort, lowIndex, highIndex):
    if ((highIndex - lowIndex) > 0):
        p = partition(listToSort,lowIndex,highIndex)
        quicksort(listToSort,lowIndex,p-1)
        print(testList)
        quicksort(listToSort,p+1,highIndex)
        print("second one", testList)


def partition(listToSort, lowIndex, highIndex):
    divider = lowIndex
    pivot = highIndex


    for i in range(lowIndex, highIndex):
        if (listToSort[i] < listToSort[pivot]):
            listToSort[i], listToSort[divider] = listToSort[divider], listToSort[i]
            divider += 1

    listToSort[pivot], listToSort[divider] = listToSort[divider], listToSort[pivot]

    return divider

quicksort(testList,0,9)
#print(testList)


       
    

        
