import os
def clear():
    os.system('clear')

names = []

def display_list():
    clear()
    if not names:
        print("\n!!! No DATA !!!")
    else:
        print(f"\n{names}")
    
def add_name():
    clear()
    name = str(input("Enter you'r name:- "))
    names.append(name)
    print(f"\n{names}")
    
def remove_name():
    clear()
    name_2 = str(input("Enter the name to remove:- "))
    names.remove(name_2)
    print(f"\n{names}")
    
def append_name():
    clear()
    name_3 = str(input("Enter the name to Append:- "))
    names.append(name_3)
    print(f"\n{names}")

def insert_name():
    clear()
    name_4 = str(input("Enter the name to Insert:- ")) 
    index = int(input("Enter the index position::- "))  
    names.insert(index,name_4)
    print(f"\n{names}")
    
def pop_name():
    clear()
    try:
        name_5 = int(input("Enter the index position to do POP::- "))
        names.pop(name_5)
    except IndexError:
        print(f"Index {name_5} is out of bounds for the list.")
    print(f"\n{names}")
    
def reverse_order():
    clear()
    names.reverse()
    print(f"\n{names}")
    
def extend_list():
    clear()
    name_7 = str(input("Enter the name to Extend::- "))
    names.extend(name_7)
    print(f"\n{names}")

def sort_list():
    clear()
    names.sort()
    print(f"\n{names}")

def main():
    while True:
        try:
            print("""
                ======string manipulation====== 
                \n1.Add Name \n2.Remove Name \n3.Append Name \n4.Insert Name \n5.Pop Name
                \n6.Reverse Order \n7.Extend List \n8.Get Numbers and Sort \n9.Display List
                \n0.Exit""")
            
            choice = int(input("\nEnter You'r choice (0-9)::- "))
            
            if choice == 1:
                add_name()
                
            elif choice == 2:
                remove_name()
                
            elif choice == 3:
                append_name()
                
            elif choice == 4:
                insert_name()
                
            elif choice == 5:
                pop_name()
                
            elif choice == 6:
                reverse_order()
                
            elif choice == 7:
                extend_list()
                
            elif choice == 8:
                sort_list()
                
            elif choice == 9:
                display_list()
                
            elif choice == 0:
                clear()
                user_input = str(input("\nWould you like to exit the program (Y/N)::- "))
                if user_input.lower() == 'y':
                    print("\n\tYou'r Exiting The Program.!!! HAND !!!")
                    break
                elif user_input.lower() == 'n':
                    print("\n!!! Hi user. You'r back !!!")
                    continue
                else:
                    print(f"{user_input} is Invalid. choices are:- (y/n)")
                
        except ValueError:
            print("Invalid input. Try again")
            
    
if __name__ == "__main__":
    main()