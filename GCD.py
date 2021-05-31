def divisor(a,b):
    c = min(a,b)

    for i in range(1,c+1):
        if(a%i==0 and b%i==0):
            temp = i

    print (temp)

if __name__ == "__main__":
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    divisor(a,b)