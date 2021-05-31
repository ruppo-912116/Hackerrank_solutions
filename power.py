r = 1
def powerSum(d,n):
    if n>0:
       global r
       n -= 1
       r = d * r
       powerSum(d,n)
    return r

print(powerSum(2,6))
