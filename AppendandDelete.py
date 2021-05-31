def trying(s,t,k):
    lens = len(s)
    lent = len(t)
    temp = 0

    for i in range (0, min(lens,lent)):
        if (s[i] == t[i]):
            temp += 2
        else:
            break
    temp = lens + lent - temp
    print(temp)
    if (temp <= k):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    trying("abcd","abcdert",10)
