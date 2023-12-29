import os
def clear():
    os.system("clear")

def main():
        clear()
    #capitalize
        user = str(input("\nEnter a string::- "))
        CAP = user.upper()
        CAP1 = user.capitalize()
        print(f"Capitalized string:- {CAP}")
        print(f"Capitalized string:- {CAP1}")

    #center    
        user_2 = int(input("\nEnter the width for centering::- "))
        CENTER = user.center(user_2)
        print(f"Centered string:- {CENTER} ")
        
    #substring count
        user_3 = str(input("\nEnter a substring to count::- "))
        substring = user.count(user_3)
        print(f"Count of {user_3}:- {substring}")
        
    #suffix or endswith    
        user_4 = str(input("\nEnter a suffix to check at the end::- "))
        suffix = user.endswith(user_4)
        print(f"Ends with {user_4}:- {suffix}")
        
    #finding the index    
        user_5 = str(input("\nEnter a substring to find::- "))
        index1 = user.find(user_5)
        print(f"Index of  {user_5}:- {index1}")
    
    #format 
        user_6 = str(input("\nEnter Your name::- "))
        user_7 = int(input("Enter your age::- "))
        text = "HEllo, My Name is {} and I am {} year old"
        f_t = text.format(user_6,user_7)
        print(f"Formatted string:- {f_t}")
    
if __name__ == "__main__":
    main()