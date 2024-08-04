def convert_temperature():
    print("Temperature Conversion Program")

    while True:
        print("select the required condition:")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")

        elif choice == "2":
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius + 273.15
            print(f"{celsius}°C is equal to {kelvin}K")

        elif choice == "3":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius}°C")

        elif choice == "4":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            kelvin = (fahrenheit - 32) * 5/9 + 273.15
            print(f"{fahrenheit}°F is equal to {kelvin}K")

        elif choice == "5":
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin - 273.15
            print(f"{kelvin}K is equal to {celsius}°C")

        elif choice == "6":
            kelvin = float(input("Enter temperature in Kelvin: "))
            fahrenheit = (kelvin - 273.15) * 9/5 + 32
            print(f"{kelvin}K is equal to {fahrenheit}°F")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    convert_temperature()