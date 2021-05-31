def max_pair(elements):
    n = len(elements)
    max_product = 0

    elements.sort()
    max_product = elements[n-1] * elements [n-2]
    
    return max_product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pair(input_numbers))
