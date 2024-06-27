def list_operations():
    numbers = []
    while True:
        print("\n1. Add number")
        print("2. Remove number")
        print("3. Print list")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            num = int(input("Enter number to add: "))
            numbers.append(num)
            print(f"{num} added to the list.")
        elif choice == '2':
            if numbers:
                num = int(input("Enter number to remove: "))
                if num in numbers:
                    numbers.remove(num)
                    print(f"{num} removed from the list.")
                else:
                    print(f"{num} not found in the list.")
            else:
                print("List is empty.")
        elif choice == '3':
            print("Current list:", numbers)
        elif choice == '4':
            print("Exiting list operations.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def dictionary_operations():
    person = {}
    
    while True:
        print("\n1. Add key-value pair")
        print("2. Remove key-value pair")
        print("3. Print dictionary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            person[key] = value
            print(f"Added {key}: {value} to the dictionary.")
        elif choice == '2':
            if person:
                key = input("Enter key to remove: ")
                if key in person:
                    del person[key]
                    print(f"Removed {key} from the dictionary.")
                else:
                    print(f"Key {key} not found in the dictionary.")
            else:
                print("Dictionary is empty.")
        elif choice == '3':
            print("Current dictionary:", person)
        elif choice == '4':
            print("Exiting dictionary operations.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def tuple_operations():
    rollno = ()
    
    while True:
        print("\n1. Add elements")
        print("2. remove element")
        print("3. Print elements")
        print("4. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            num=int(input("Enter a roll no to add: "))
            rollno=rollno+(num,)
            print(f"{num} added to the tuple")
        elif choice == '2':
            if rollno:
                index=int(input("Enter the index of the element to remove: "))
                if index>=0 and index<len(rollno):
                    rollno=rollno[:index]+rollno[index+1:]
                    print(f"Element at index {index} removed from the tuple.")
                else:
                    print("Invalid index.")
            else:
                print("tuple is empty")
        elif choice == '3':
            if rollno:
                for i in rollno:
                    print(i)
            else:
                print("tuple is empty.")
        
        elif choice == '4':
            print("Exiting tuple operations.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")



def main():
    while True:
        print("\nSelect data structure to operate on:")
        print("1. List")
        print("2. Dictionary")
        print("3. Tuple")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            list_operations()
        elif choice == '2':
            dictionary_operations()
        elif choice == '3':
            tuple_operations()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
