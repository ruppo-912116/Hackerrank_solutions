x = -1
z = -100000

while (z> -100000):
    fun = (z**2)-z + 1
    print("the value of the function:", fun)
    z-= 1
    if (fun== 0):
        break

print("The final value is:", z)
