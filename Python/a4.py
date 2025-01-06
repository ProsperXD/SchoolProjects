# Show the UI
print("#" * 80)
print("#" * 9, " " * 60, "#"*9)
print("#" * 9, "Advanced Calculator".center(60), "#" * 9)
print("#" * 9, " " * 60, "#"*9)
print("#" * 80)

def main():
    print("Welcome to the Advanced Calculator!")

    # Display menu options
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    # Get user choice
    choice = input("Please select the calculation (1 or 2): ")

    # Check user choice and perform the corresponding calculation
    if choice == "1":
        c_to_f()
    elif choice == "2":
        f_to_c()
    else:
        print("Invalid choice. Please select 1 or 2.")

def c_to_f():
    # Get input from the user
    celsius = float(input("Enter temperature in Celsius: "))

    # Perform the conversion
    fahrenheit = (celsius * 9/5) + 32

    # Display the result
    print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")

def f_to_c():
    # Get input from the user
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Perform the conversion
    celsius = (fahrenheit - 32) * 5/9

    # Display the result
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")

# Run the program
if __name__ == "__main__":
    main()
