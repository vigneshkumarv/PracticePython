# Python program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def enter_list():
    num_list = []
    list_size = int(input("Enter the size of the list: "))
    if list_size > 0:
        for count in range(0,list_size):
            inp = int(input("Enter integer {}: ".format(count+1)))
            num_list.append(inp)
        return num_list
    else:
        print("Invalid size!")
        return 0

def remove_duplicates(int_list):
    new_list = []
    for element in int_list:
        if not(element in new_list):
            new_list.append(element)
    print(new_list)

out_list = enter_list()
if out_list != 0:
    remove_duplicates(out_list)
else:
    exit()
