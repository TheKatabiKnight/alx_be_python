def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_list.append(input('Enter the item to add: '))
            pass
        elif choice == '2':
            remove = input('Please enter the name of the item you wish to remove: ')
            if remove in shopping_list:
                shopping_list.remove(remove)
            else:
                print('Item not in your Shopping List!!')
            pass
        elif choice == '3':
            x = 0
            while x <= len(shopping_list) - 1:
                print(shopping_list[x])
                x += 1
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()