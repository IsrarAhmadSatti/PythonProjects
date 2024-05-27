
###ANAGRAMS
##str1 = input("Enter 1st string: ")
##str2 = input("Enter 2nd string: ")
##str1 = str1.upper()
##str2 = str2.upper()
##counter = 0
##for i in range(len(str2)):
##    if str2[i] in str1:
##        counter += 1
##if counter == len(str1):
##    
##    print("\tEntered strings are Anagrams")
##    
##else:
##    
##    print("\nEntered strings are not anagrams")

###Changing Cases
##lst=input("Enter the string please: ")
##lst2=''
##for i in range (0,len(lst)):
##    if i%2==0:
##        lst2=lst2+(lst[i].upper())
##    else:
##        lst2=lst2+lst[i]
##print("Original String\n",lst,"\nHerer is the modified string \n",lst2)
##print("Reverse of that string",lst2.swapcase())

###Matrix Addition
##def Matrix_Addition():
##    matrix=[
##        [2,3,6],
##        [4,1,5],
##        [2,7,6]
##        ]
##    matrice=[
##        [1,0,0],
##        [0,1,0],
##        [0,0,1]
##        ]
##    print("First Matrix\n",matrix)
##    print("Second Matrix\n",matrice)
##    print("\nAfter addition")
##    for i in range(0,3):
##        print("[",end=' ')
##        for j in range(0,3):
##            print(matrix[i][j]+matrice[i][j],end=' ')
##        print("]\n")
##Matrix_Addition()

###Floyd's Triangle
##def Floyd_Triangle(N):
##    for i in range(1,N+1):
##        for j in range(1,i+1):
##            p=i*(i-1)/2+j
##            print(int(p),end='  ')
##        print("\n")
##
##try: 
##    N=int(input("Enter the number to create pascal's triangle: "))
##    if N >= 1:
##        Floyd_Triangle(N)
##    else:
##        print("Enter a number greater then or equal to 1")
##except ValueError:
##    print("!!!INVALID INPUT TRY AGAIN!!!")
    
###Pascal's Triangle
##def pascals(N):
##    for i in range(1,N+1):
##        if i==1:
##            p=1
##            print(f'{p:1d}','\n')
##        p=1
##        print(f'{p:1d}',end=' ')
##        for j in range(0,i):
##            p=(i-j)/(j+1)*p
##            p=int(p)
##            print(f'{p:2d}',end=' ')
##        print("\n")
##try:
##    N = int(input("Enter the number to create pascal's triangle: "))
##    if N == 0:
##        print(1)
##    else:
##        pascals(N)
##    
##except ValueError:
##    print("!!!INVALID INPUT TRY AGAIN!!!!")

###selection sort algorithm
##arr=[]
##while True:
##    num=int(input("Enter the number: -1 to terminate: "))
##    if num == -1:
##        break
##    arr.append(num)
##print("Array entered by user is:\n",arr)
##for i in range(len(arr)):
##    min_ind=i
##    for j in range (i+1,len(arr)):
##        if arr[min_ind]>arr[j]:
##            min_ind=j
##    arr[i],arr[min_ind]=arr[min_ind],arr[i]
##print("Here is your sorted array\n",arr)

###Insertion sort algorithm
   
##print("Array entered by user is:\n",arr)
##for i in range(1,len(arr)):
##    key=arr[i]
##    j=i-1
##    while j>=0 and key<arr[j]:
##        arr[j+1]=arr[j]
##        j-=1
##    arr[j+1]=key
##
##print("Here is your sorted array\n",arr)

###recursion factorial
##def factorial(num):
##    if num<=1:
##        return 1
##    else:
##        return num * factorial(num-1)
##num=int(input("Enter the number tocalculate factorial: "))
##print(factorial(num))

###linearsearch algorithm
##mylst=["k","l","m","n","o","p","q","a","b"]
##srch=input("Enter the character you want to search: ")
##count=0
##for i in range(0,len(mylst)):
##    if srch==mylst[i]:
##        print(srch," is present at index ",i)
##        count+=1
##if count==0:
##    print(srch," is not in the list")

###bubble sort an array
##ar1=[8,2,6,4]
##ar2=[1,7,3,5]
##arr=ar1+ar2
##swapped=True
##while swapped:
##    swapped=False
##    for i in range (len(arr)-1):
##        if arr[i]<arr[i+1]:
##            swapped=True
##            arr[i],arr[i+1]=arr[i+1],arr[i]       
##print("The swapped array in increasing order is \n",arr)

##dig=int(input("Enter the number: "))
##if dig<8:
##    print("octal equilent of",dig,"is",dig)
##elif dig>=8 and dig<64:
##    k=dig//8
##    d=dig%8
##    print("octal equilent of",dig,"is",k,d)
##if dig<16:
##    print("octal equilent of",dig,"is",dig)
##elif dig>=16 and dig<256:
##    k=dig//16
##    d=dig%16
##    print("hex equilent of",dig,"is",k,d)

###leap year
##year=int(input("enter the year: "))
##if year%4==0:
##    print(year," is a leap year")
##else:
##    print(year,"is not a leap year")
##
##return ascii of the characters enetered
##sen=input("Enter a string: ")
##for i in sen:
##    print("ASCII of ",i,"is=",ord(i))
##
##prime numbers between 1 and N, N as inputfrom user
##def prime(n):
##    lst=[]
##    for i in range (2,n+1):
##        if i<10 and i%4!=0 and i%6!=0 and i%9!=0:
##            lst.append(i)            
##        elif i>10 and i%2!=0 and i%3!=0 and i%4!=0 and i%5!=0 and i%7!=0:
##            lst.append(i)
##    return lst
##num=int(input("Enter a number: "))
##print("prime number between",1,"and", num,"are \n",prime(num))

###Implementing positive and negative powers
##def power(x,n):
##    if n==0:
##        return 1
##    elif n>1:
##        powe=x
##        for i in range(1,int(n)):
##            powe=powe*x
##    elif n<0:
##        powe=x
##        n=-(int(n))
##        for i in range(1,n):
##            powe=powe*x
##        powe=1/powe
##    return powe
##num=float(input("Enter the number: "))
##p=float(input("Enter the power: "))
##print(num,"raise to power",p,"is =",power(num,p))

###input numbers from user and arrrange them in list and calculate their average
##def average(n):
##    avg=0
##    for i in range (len(n)):
##        avg+=n[i]
##    avg=avg/len(n)
##    avg=round(avg,2)
##    return avg
##lst=[]
##while True:
##    num=int(input("Input numbers, -1 to terminate: "))
##    if num==-1:
##        break
##    lst.append(num)
##print("entered numbers in list are: ",lst)
##print("average of the entered numbers is",average(lst))
##
##arr=list(input("enter a string:  "))
##for i in range (len(arr)//2):
##    arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
##print(arr)

###reversing elements of an array
##arr=[1,2,3,4,5,6,7,8,9]
##for i in range (len(arr)//2):
##   arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
##print(arr)
##
##x=int(input("enter the number to calculate factorial: "))
##if x==0 or x==1:
##    print("Square root of",x,"is =",x)
##res=1
##for i in range(1,x+1):
##    res=i*res
##print(res)
##
##array=[1,2,3,4,5]
##array.reverse()
##print(array)

###number from 1 to 100 except multiple of 3 or 5
##count=[]
##for i in range(1,101):
##    if i%3==0:
##        count.append('fizz')
##        continue
##    if i%5==0:
##        count.append('buzz')
##        continue
##    else:
##        count.append(i)
##print(count)

###Compares three numbers and returns largest
##def comp_num(num1,num2,num3):
##    if num1>num2 and num1>num3:
##        print(num1,"is the largest number")
##    if num2>num1 and num2>num3:
##        print(num2,"is the largest number")
##    if num3>num2 and num3>num1:
##        print(num3,"is the largest number")
##num1=int(input("Enter the first number= "))
##num2=int(input("Enter the second number= "))
##num3=int(input("Enter the third number= "))
##comp_num(num1,num2,num3)

###counts vowels in a string
##str1=input("enter a string: ")
##count=0
##str1 = str1.lower()
##for i in str1:
##    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
##        count+=1
##    
##print("Vowels in the string are",count)

