def hello_world_example(self):
        print("Hello, World!")
    
def variable_example(self):
        # Variable example
        name = "Jyothish"
        age = 21
        print(f"My name is {name} and I am {age} years old.")
    
def arithmetic_operations(self):
        num1=int(input("enter the first number:"))
        num2=int(input("enter the second number:"))

        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        
        operation=int(input("enter required operation(1-4):"))
        if operation==1:
            addition = num1 + num2
            print(addition)
        elif operation==2:
            subtraction = num1 - num2
            print(subtraction)
        elif operation==3:
            multiplication = num1 * num2
            print(multiplication)
        elif operation==4:
            division = num1 / num2
            print(division)
        else:
            print("invalid operation")
            
def conditional_statements_example(self):
        # Conditional statements example
        num=int(input("enter the number:"))
        if num > 0:
            print(f"{num} is positive.")
        elif num < 0:
            print(f"{num} is negative.")
        else:
            print(f"{num} is zero.")
    
def string_manipulation_example(self):
        # String manipulation example
        message = "Welcome to jyothish world!"
        print("Original message:", message)
        print("Uppercase:", message.upper())
        print("Lowercase:", message.lower())
        print("Split into words:", message.split())


def main():
    print("Examples of different syntax elements:")
    print("1.Hello World Example")
    print("2.Variable Example")
    print("3.Arithmetic Operations Example")
    print("4.Conditional Statements Example")
    print("5.String Manipulation Example")
    print("6.Exit")
    while(True):  
        example_choice = int(input(" Enter your choice (1-5): "))
        if example_choice == 1:
           hello_world_example() 
        elif example_choice == 2:
           variable_example()
        elif example_choice == 3:
           arithmetic_operations()
        elif example_choice == 4:
           conditional_statements_example()
        elif example_choice == 5:
           string_manipulation_example()
        else:
          print("Invalid choice.Exiting")
          exit()
if __name__ == "__main__":
    main()



