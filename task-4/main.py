def add(a,b):
    
    c=a+b
    print_fun(a,b,c,'+')

def sub(a,b):   
    c=a-b
    print_fun(a, b, c, '-')

def mul(a,b):
    c=a*b
    print_fun(a, b, c, '*')
def div(a,b):
    c=a/b
    print_fun(a, b, c, '/')
def dec():
    print("**********************************CALCULATOR**********************************")

def print_fun(a,b,c,o):
    print(f"*****************************{a} {o} {b} = {c}*******************************")

def thank():
    print("*****************************THANK YOU*******************************")


def main():
    dec()
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter the operation:"))
    while True:
        if ch==1:
            add(a,b)
            break
        elif ch==2:
            sub(a,b)
            break
        elif ch==3:
            mul(a,b)
            break
        elif ch==4:
            div(a,b)
            break
        elif ch==5:
            thank()
            break
        else:
            print("Invalid Input")
            break


if __name__ == "__main__":
    main()
    
