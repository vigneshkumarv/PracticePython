# Python program to generate fibonacci series

def sequence():
    length = int(input("Enter the length of fibonacci sequence: "))
    if length > 0:
        return length
    else:
        print("Invalid Length!")
        return 0

def fibonacci(sequence_length):
    if(sequence_length < 1):
        exit()
    else:
        i = 0
        j = 1
        k = 1
        print("Fibonacci series is given by: ")
        for count in range(0,sequence_length):
            print(k, end = " ")
            k = i + j
            i=j
            j=k

len = sequence()
fibonacci(len)
