def enter_list():
    size = int(input("Enter the size of list (integers): "))
    num_list = []
    for count in range(1,size+1):
        num_list.append(int(input("Enter number {}: ".format(count))))
    print("Entered list is: ",num_list)
    return num_list

def extract_first_and_last_elements(numlist):
    new = []
    numlist_len = len(numlist)
    for count in range(0,numlist_len):
        if count == 0 or count == numlist_len-1:
            new.append(numlist[count])
    print(new)



temp = enter_list()
extract_first_and_last_elements(temp)
