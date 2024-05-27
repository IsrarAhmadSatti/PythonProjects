#ATM Module Sample

def BalanceInquiry(myData):
    #Printing Current balance
    print("Your Current balance is: ",myData["balance"])

def Withdraw(myData):
    #Withdrawing Function whole object is input for this function
    #function changes in the balnce and updates the object and returns updated object
    try:
        bal = int(input("Enter the amount you want to withdraw: "))
        if bal > myData["balance"]: #Checking whther balance is sufficient or not
            print("Insufficient balance try again")
            check = input("Do you want to add balance: yes (y) or no (n) ")
            #^Check for user if he wants to withdraw more
            if check == "yes" or check == "y":
                AddBalance(myData)
            elif check == "no" or check == "n":
                return myData["balance"]    
        else:
            newbal = myData["balance"] - bal
            print("Your remaining balance is: ", newbal)
            myData["balance"] = newbal
            return myData["balance"]
    except ValueError: #Exception if user enter a wrong input
        print("Enter correct amount: Try Again")
        Withdraw(myData)

def AddBalance(myData):
    # Adding amount to the Account
    try:
        bal = int(input("Enter the amount you want to add: "))
        if bal > 0:
            addbal = myData["balance"] + bal #adding the balance
            print("Your new balance is: ",addbal)
            myData["balance"] = addbal #updating the object
            return myData["balance"]
        else:
            print("Invalid amount try agian")
            AddBalance(myData) #Recalling the function if invalid input
    except ValueError:#Exception if user enter a wrong input
        print("Enter some amount please")
        AddBalance(myData)

def userlogg(myData):
    usid = input("Enter your name please: ")
    if usid == myData["username"]: # Varifying username
        while True:
            pin = int(input("Enter your pin please: "))
            if pin == myData["pincode"]:# varifying pincode
                print("\tLogin Succesfull")
                return True
                break
            else:
                print("!!!WRONG PIN!!! Try Again")
    else:
        print("Wrong user name Try Again: ")
        userlogg(myData) #recall function if inputs are wrong   

def ATM_Function(myData):
    userlogg(myData)
    while True:
        print("\t\tChoose")
        choose = input("0:BalnaceInquiry, 1:Withdraw, 2:AddBalance, 3:Exit: ")
        if choose == "BalanceInquiry" or choose == "0":
            BalanceInquiry(myData)
        elif choose == "Withdraw" or choose == "1":
            Withdraw(myData)
        elif choose == "AddBalance" or choose == "2":
            AddBalance(myData)
        elif choose == "Exit" or choose == "3":
            print("Thank you for using our Services: ")
            break
        else:
            print("Wrong option Retry!!!!!")
            
print("\tWelcome to ATM Services\n")
myData = {
    "username" : "Israr",
    "pincode" : 1045,
    "balance" : 100,
    }
user2 = {
    "username" : "talal",
    "pincode" : 5665,
    "balance" : 1000
    }
      
ATM_Function(myData)
 
