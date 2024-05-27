def division():
    res=0
    in1=float(input("Enter first number=  "))
    in2=float(input("Enter second number=  "))
    if in2!=0:
        res=round((in1/in2),4)
        print("Result of division is= ",res)
    else:
        print("----wrong input----")
        division()
    
def multiplication():
    res=0
    in1=float(input("Enter first number=  "))
    in2=float(input("Enter second number=  "))
    res=round((in1*in2),4)
    print("Result of multiplication is= ",res)

def addition():
    res=0
    in1=float(input("Enter first number=  "))
    in2=float(input("Enter second number=  "))
    res=round((in1+in2),4)
    print("Result of addition is= ",res)

def subtract():
    res=0
    in1=float(input("Enter first number=  "))
    in2=float(input("Enter second number=  "))
    res=round((in1-in2),4)
    
    print("Result of substraction is= ",res)

def sine ():
    from math import pi
    x=float(input("enter the Angle:  "))
    if x>=360:
        x=x%360
        if x>=180 and x<360:
            x=x-180
            x=x* pi /180
            res=-x+(x**3)/6-(x**5)/120+(x**7)/5040-(x**9)/362880
        else:
            x=x* pi /180
            res=x-(x**3)/6+(x**5)/120-(x**7)/5040+(x**9)/362880
    elif x>=180 and x<360:
        x=x-180
        x=x* pi /180
        res=-x+(x**3)/6-(x**5)/120+(x**7)/5040-(x**9)/362880
    else:
        x=x* pi /180
        res=x-(x**3)/6+(x**5)/120-(x**7)/5040+(x**9)/362880
    res=round(res,4)
    print("Cosine is =",res)
    
def cosine ():
    from math import pi
    x=float(input("enter the Angle:  "))
    if x>=360:
        x=x%360
        if x>=180 and x<=270:
            x=x-180
            x=x* pi /180
            res=-1+(x**2)/2-(x**4)/24+(x**6)/720-(x**8)/40320
        elif x>270 and x<360:
            x=360-x
            x=x* pi /180
            res=1-(x**2)/2+(x**4)/24-(x**6)/720+(x**8)/40320
        else:
            x=x* pi /180
            res=1-(x**2)/2+(x**4)/24-(x**6)/720+(x**8)/40320
    elif x>=180 and x<=270:
        x=x-180
        x=x* pi /180
        res=-1+(x**2)/2-(x**4)/24+(x**6)/720-(x**8)/40320
    elif x>270 and x<360:
        x=360-x
        x=x* pi /180
        res=1-(x**2)/2+(x**4)/24-(x**6)/720+(x**8)/40320
    else:
        x=x* pi /180
        res=1-(x**2)/2+(x**4)/24-(x**6)/720+(x**8)/40320 
    res=round(res,4)
    print("Sine is =",res)
    
def tangent ():
    from math import pi
    x=float(input("enter the Angle:  "))
    if x>=180:
        x=x%180
    x=x* pi /180
    r1=x-(x**3)/6+(x**5)/120-(x**7)/5040+(x**9)/362880
    r1=round(r1,4)
    r2=1-(x**2)/2+(x**4)/24-(x**6)/720+(x**8)/40320
    r2=round(r2,4)
    if r2==0:
       print("tangent is undefined")
    else:
        res=r1/r2
        res=round(res,4)
        print("Tangent is =",res)

def square():
    x=float(input("enter the number:  "))
    res=round((x**2),4)
    print("Square of",x,"is =",res)

def sq_root():
    x=float(input("enter the Value:  "))
    if x==0 or x==1:
        print("Square root of",x,"is =",x)
    elif x>1:
        r=x
        precision=10**(-10)
        while abs (x-r*r)>precision:
            r=(r+x/r)/2
        r=round(r,4)
        print("Square root of",x,"is =",r)
    else:
        print("Syntax error")

def factorial():
    x=int(input("enter the number to calculate factorial: "))
    if x==0 or x==1:
        print("Square root of",x,"is =",x)
    res=1
    for i in range(1,x+1):
        res=i*res
    print(x,"!=",res)
def power():
    x=float(input("enter the number:  "))
    y=float(input("raise to power: "))
    res=round((x**y),4)
    print(x,"^",y,"=",res)

def ln():
    x=float(input("enter the Value:  "))
    res=(x-1)-((x-1)**2)/2+((x-1)**3)/3-((x-1)**4)/4
    print("ln of ",x,"is",res)
 
while True: 
    select=input("""\nEnter the function you want to perform
        '/', '*', '+', '-', 'sine', 'cos', 'tan', 'sqrt',
        'Square' "factorial", power","ln"
        "OFF" to terminate\n""")

    if select=='*':
        multiplication()
    elif select=='/':
        division()
    elif select=='+':
        addition()
    elif select=='-':
        subtract()
    elif select=='sine':
        sine()
    elif select=="cos":
        cosine()
    elif select=="tan":
        tangent()
    elif select=="sqrt":
        sq_root()
    elif select=="OFF" or select=="off":
        print("---THANK YOU FOR USING CALCULATOR---")
        break
    elif select=='square':
        square()
    elif select=='factorial':
        factorial()
    elif select=='power':
        power()
    elif select=='ln':
        ln()
    else:
        print("----INVALID INPUT----")
    


    
