import keyword

# Get the list of Python keywords
python_keywords = keyword.kwlist

def print_keywords_per_character():
    for keyword in python_keywords:
        for char in keyword:
            print(char)
        print()

def print_all_keywords():
    print(', '.join(python_keywords))

while True:
    print("MENU:")
    print("1: Print keywords per character")
    print("2: Print all keywords")
    print("3: Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        print("\nPrinting keywords per character:")
        print_keywords_per_character()
    elif choice == '2':
        print("\nPrinting all keywords:")
        print_all_keywords()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")