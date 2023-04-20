# This program will calculate whether the user input is a prime
# Pedro Ayala

def main():  # main function
    num = int(input('Enter your number: '))

    if IsPrime(num):  # call function to find if a number is prime
        print(num, 'is prime')  # print is prime
    else:
        print(num, 'is not a prime')  # print is not a prime


# Definition of function to find if a number is prime
def IsPrime(num):
    if num <= 1:
        return False  # return false to main

    for i in range(2, num):  # loop to find a factor
        if num % i == 0:  # if factor found, not prime
            return False

    return True  # return true to main


main()  # return to main