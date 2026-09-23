dictionary = {}

# 1. 'True' must have a capital 'T'
while True:
    print("\n dictionary management system")
    print("1. add a word")
    print("2. search for meaning")
    print("3. display all words")
    print("4. update meaning")
    print("5. delete word")
    print("6. exit")
    
    # Everything below here is now indented by 4 spaces 
    # to place it INSIDE the while loop
    choice = input("enter the choice: ")
    
    if choice == "1":
        keyword = input("enter the word: ").lower() 
        meaningvalue = input("enter the meaning: ")
        dictionary[keyword] = meaningvalue
        print("word added successfully!")

    elif choice == '2':
        keyword = input("enter the word to search: ").lower()
        if keyword in dictionary:
            print("meaning:", dictionary[keyword])
        else:
            print("word not found in the dictionary.")
            
    elif choice == "3":
        if dictionary:
            print("words in dictionary and meanings:")
            for keyword, meaningvalue in dictionary.items():
                print(f"{keyword}: {meaningvalue}")
        else:
            print("dictionary is empty.")
            
    elif choice == "4":
        keyword = input("enter the word to update meaning: ").lower()
        if keyword in dictionary:
            newmeaningvalue = input("enter the new meaning: ")
            # 2. Fixed typo here: 'dictionar' -> 'dictionary'
            dictionary[keyword] = newmeaningvalue
            print("meaning updated successfully!")
            print("updated meaning:", dictionary[keyword])
        else:
            print("word is not found in the dictionary")
            
    elif choice == "5":  
        keyword = input("enter the word to delete: ").lower()
        if keyword in dictionary:
            del dictionary[keyword]
            print("deleted the word successfully")
        else:
            print("word is not found in the dictionary")
            
    elif choice == '6':
        print("exiting the program......")
        break  
        
    else:
        print("invalid choice! please enter a valid option.")