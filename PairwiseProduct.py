def max_pair(elements):
    n = len(elements)
    max_product = 0
    index1 = 0
    index2 = 0

    for i in range(n):
        if (elements[i] > elements[index1]):
            index1 = i

    for i in range(n):
        if ((elements[i] != elements[index1]) and (elements[i]>elements[index2])):
            index2 = i

    max_product = elements[index1] * elements[index2]
    
    return max_product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pair(input_numbers))
