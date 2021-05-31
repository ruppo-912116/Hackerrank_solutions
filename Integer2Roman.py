# Roman equivalents including the exceptions
# exceptions are 4,9,40,90,400,900
intToroman = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}

def IntegertoRoman(integer):
    finalResult=""
    # List of all the equivalents
    # The descending order is for the division of the input integer starting from the largest place value 
    descendingEquivalents = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    for i in descendingEquivalents:
        if integer != 0:
            quotient = integer // i
            # if quotient is not zero, print the roman numbers
            # for loop will repeat and append the roman till it meets the value
            if quotient != 0:
                for _ in range(quotient):
                    finalResult = finalResult + intToroman[i]
            # update integer with remainder
            integer = integer % i
    return finalResult


if __name__ == "__main__":
    integerNumber = int(input("Enter an integer: "))
    # handling invalid numbers
    if integerNumber > 0:
        print(IntegertoRoman(integerNumber))
    else:
        print("invalid input")
