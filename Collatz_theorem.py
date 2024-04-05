#generating Collatz Conjecture

def Collatz(num):
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            steps += 1
        elif num % 2 != 0:
            num = num * 3 + 1
            steps += 1
        print(num,end=",")
    print('\nNumber of steps: ', steps)

num = int(input('enter any number to generate collatz conjecture: '))
Collatz(num)


    
