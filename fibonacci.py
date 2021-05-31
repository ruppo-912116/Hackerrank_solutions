
def fibonacci(n):
    arr = [0,1]
    
    for i in range(2,n):
        arr.append(arr[i-2] + arr[i-1])

    print (arr)




if __name__ == "__main__":
    n = int(input("enter the fibonacci number: "))
    fibonacci(n)

