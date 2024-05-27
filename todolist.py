#Implementing Todolist ap using Functions
todolist = ["get","set","wet"]
completed=[]

def Additem(todolist):
    
    while True:
        item = input("\nEnter item you want to add to the list: ")
        if item == "" or item == " ": #Nothingness check
            print("Enter a valid input")
        else:
            todolist.append(item) #updating the list
            add = input("Do you want to continue adding item: Y or N: ")#Continue????
            if add == "y" or add == "Y":
                continue
            elif add == 'N' or add == "n":
                break
            else:
                print("Wrong Choice going to main")
                break
    return todolist #returning updated list

def movetoComplete(todolist):
    
    if len(todolist) == 0: #length check
        print("List is empty add items first")
    else:
        try:
            #Getting index of the element to be removed
            #after displaying it to user
            print("\nHere is the original list \t",todolist)
            print("Enter index of item you want to move 0 to", len(todolist)-1)
            index = int(input("Enter the index: "))
            if index > (len(todolist)-1): #wrong index check
                print("Wrong choice: Enter valid index")
                movetoComplete(todolist)
            else:
                completed.append(todolist[index]) #moving item to completed list
                del todolist[index] #removing completed item from the todolist
                print("item moved to completed list")
        except ValueError:
            print("Wrong choice Try Again")
            movetoComplete(todolist) #Validation Check
    return completed
            
def Removeitem(todolist):
    
    if len(todolist) == 0: #length check
        print("List is empty add items first")
    else:
        try:
            #Getting index of the element to be removed
            #after displaying it to user
            print("\n",todolist)
            print("Enter item you want to remove 0 to", len(todolist)-1)
            item = int(input("enter the number here: "))
            if item > (len(todolist)-1): #wrong index check
                print("\tEnter valid Index again")
                Removeitem(todolist)
            else:
                print("TO DO Removed")
                del todolist[item] #deleting the item from todolist
        except ValueError:
            print("Wrong choice Try Again")
            Removeitem(todolist)
    return todolist

def viewTodo(todolist):
    #displaying todolist 
    if len(todolist)== 0:
        print("List is empty add something first")
    else:
        print("\t TODO list",todolist)

def viewComplete(completed):
    #displaying completed Tasks list
    if len(completed)== 0:
        print("List is empty move tasks first")
    else:
        print("\t Completed task list",completed)

def to_do_operations():
    
    while True:
        print("\n\t\tChoose operation: ")
        oper = input("1:Additem, 2:Removeitem, 3:moveComplete 4:Viewtodo 5:viewcomplete 6:exit: ")
        if oper == "1" or oper == "Additem":
            Additem(todolist)
        elif oper == "2" or oper == "Removeitem":
            Removeitem(todolist)
        elif oper == '3' or oper == "move complete":
            movetoComplete(todolist)
        elif oper == '4' or oper == "Viewtodo":
            viewTodo(todolist)
        elif oper == '5' or oper == "viewcomplete":
            viewComplete(completed)
        elif oper == '6' or oper == "exit":
            print("\n\tTHANK YOU for using our app")
            break
        else:
            print("Wrong Choice select again")
        
to_do_operations()
