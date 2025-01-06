db = {}
def addEmployee():
    Employee = input("Enter Employee Name: ")
    pay = input("Enter Employee Pay: ")
    rank = input("Enter Employee Rank: ")
    db[Employee] = {'salary': pay, 'position': rank}
    print(f"Successfully Employed {Employee}")
    return main()
def removeEmployee():
    print("Ok Remove Him")
    Employee = input("Enter Employee Name: ")
    if Employee in db:
        del db[Employee]
        print(f"Successfully Fired {Employee}")
        return main()
    else:
        print(f"Employee Not Found ({Employee}")
        return main()

def displayEmployees():
    for name, info in db.items():
        print(f"Name: {name}, Salary: {info['salary']}, Position: {info['position']}")
def main():
    print("\n1. Add Employee\n2. Remove Employee\n3. Display Database\n4. Exit")
    choice = int(input("Enter You're Choice: "))
    if choice == 1:
        addEmployee()
    elif choice == 2:
        removeEmployee()
    elif choice==3:
        displayEmployees()

if __name__ == "__main__":
    main()
