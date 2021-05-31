a = int(float(input("enter the length of the array: ")))
arr = [] #array to store the numbers entered by the user
result = [] #array to store the pairs of the number giving the entered sum

while(a> 0):
    i = int(input("enter the elements: "))
    arr.append(i)
    a = a - 1
  
         
lowIndex = 0
highIndex = len(arr) - 1


sum = int(input("enter the sum you want "))


while (lowIndex < highIndex):

    tempSum = arr[lowIndex] + arr[highIndex]

    if (tempSum == sum):
        result.append((arr[lowIndex],arr[highIndex]))
        lowIndex = lowIndex + 1
    elif (tempSum < sum):
        lowIndex = lowIndex + 1
    elif (tempSum > sum):
        highIndex = highIndex - 1
    else:
        break

if(result):
    print("the numbers are: ",result)
else:
    print("No such pair exists")


