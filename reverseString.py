# program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

def input_string():
    string = input("Enter a string: ")
    return string

def reverse_string(inputString):
    list_string = []
    split_string =  inputString.split()
    count = len(split_string) - 1
    while (count >= 0):
        list_string.append(split_string[count])
        count = count - 1
    print(" ".join(list_string))


temp = input_string()
reverse_string(temp)
