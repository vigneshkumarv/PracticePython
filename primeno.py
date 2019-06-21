#Python program to determine if a positive integer is prime or not.

def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

input_int = int(input("Enter a positive integer: "))
if input_int > 1:
    output = prime(input_int)
    if(output):
        print("{} is prime".format(input_int))
    else:
        print("{} is not prime".format(input_int))
else:
    print("Invalid Input!, Please enter integer greater than 1.")
