db = {}

def addEmployee():
    while True:
        try:
            Employee = input("Enter Employee Name: ")
            pay = float(input("Enter Employee Pay: "))
            rank = input("Enter Employee Rank: ")
            db[Employee] = {'salary': pay, 'position': rank}
            print(f"Successfully Employed {Employee}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid pay value.")

def removeEmployee():
    while True:
        try:
            print("Ok, Remove Him")
            Employee = input("Enter Employee Name: ")
            if Employee in db:
                del db[Employee]
                print(f"Successfully Fired {Employee}")
            else:
                print(f"Employee Not Found ({Employee})")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def displayEmployees():
    print("Employee Database:")
    for name, info in db.items():
        print(f"Name: {name}, Salary: {info['salary']}, Position: {info['position']}")
    if not db:
        print("No employees in the database.")

def main():
    while True:
        try:
            print("\n1. Add Employee\n2. Remove Employee\n3. Display Database\n4. Exit")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                addEmployee()
            elif choice == 2:
                removeEmployee()
            elif choice == 3:
                displayEmployees()
            elif choice == 4:
                print("Exiting program.")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
