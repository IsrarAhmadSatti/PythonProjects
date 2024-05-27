#Structural Sorting approach
swapped=True
sort=[]
while True:
    try:
        num=int(input("Enter the number -1 to stop: "))
        if num == -1:
            break
        sort.append(num)
    except ValueError:
        print("Wrong input Enter the number agian: ")
print("The array entered by user\n",sort)
if sort!=[]:
    while swapped:
        swapped=False
        for i in range(0,len(sort)-1):
            if sort[i]<sort[i+1]:
                sort[i],sort[i+1]=sort[i+1],sort[i]
                swapped=True
    print("here is your sorted array\n",sort)
else:
    print("Array is empty =",sort)
