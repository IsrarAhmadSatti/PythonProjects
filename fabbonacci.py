
def fabonacci(num):
    a = 0
    b = 1
    print(a , end=' ')
    while b < num:
        a , b = b, a + b
        print(a , end = ' ')

num = int(input("Enter the number to create fabbonaci series: "))
fabonacci(num)