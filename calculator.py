def sum1(num1,num2):
    return num1+num2
def sub1(num1,num2):
    return num1-num2
def div1(num1,num2):
    return num1/num2
def mul(num1,num2):
    return num1*num2
def result():
    ops=str(input("Enter the opaation you want to do + or - or / or * : ") )
    if ops not in '+-*/':
        print("Invalid Choice Please chose Between + / - * ")
        return result()
    a=int(input("Enter the first number : "))
    b=int(input("Enter the Sceond number : "))
    do_again=None
    if ops== '+':
        print("{}+{} = ".format(a,b) + str(sum1(a,b)))
    elif ops== '-':
        print("{}-{} = ".format(a,b) + str(sub1(a,b)))
    elif ops== '*':
        print("{}*{} = ".format(a,b) + str(mul(a,b)))
    elif ops== '/':
        print("{}/{} = ".format(a,b) + str(div1(a,b)))
    do_again= str(input("Do you want to continue Y/N : "))
    if do_again == 'Y' or do_again =='y':
        return result()
    else:
        pass
    
result()
