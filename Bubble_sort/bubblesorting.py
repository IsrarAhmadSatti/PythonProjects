my_list = []

def ascendingSort(num):
    swapped = True
    for i in range(num):
        val = int(input("Enter a list element: "))
        my_list.append(val)
    print('\noriginal Array is: ', my_list)
    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] < my_list[i + 1]:
                swapped = True
                my_list[i+1], my_list[i] = my_list[i], my_list[i+1]
    print("\nSorted Array")
    print(my_list)

num = int(input("How many elements do you want to sort: "))
ascendingSort(num)
