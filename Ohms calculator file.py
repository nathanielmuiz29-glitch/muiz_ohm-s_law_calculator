
# OHM'S LAW AND POWER CALCULATOR
# ND1 Python Mini Project

# Function to calculate voltage
def calculate_voltage():
    print("\n--- VOLTAGE CALCULATION ---")
    current = float(input("Enter current (A): "))
    resistance = float(input("Enter resistance (Ohms): "))

    voltage = current * resistance

    print("Voltage =", voltage, "Volts")


# Function to calculate current
def calculate_current():
    print("\n--- CURRENT CALCULATION ---")
    voltage = float(input("Enter voltage (V): "))
    resistance = float(input("Enter resistance (Ohms): "))

    if resistance == 0:
        print("Error! Resistance cannot be zero.")
    else:
        current = voltage / resistance
        print("Current =", current, "Amperes")


# Function to calculate resistance
def calculate_resistance():
    print("\n--- RESISTANCE CALCULATION ---")
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    if current == 0:
        print("Error! Current cannot be zero.")
    else:
        resistance = voltage / current
        print("Resistance =", resistance, "Ohms")


# Function to calculate electrical power
def calculate_power():
    print("\n--- POWER CALCULATION ---")
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    power = voltage * current

    print("Power =", power, "Watts")

    # Additional feature: Power safety warning
    if power > 100:
        print("WARNING! High power detected.")
    else:
        print("Power level is within the project safety limit.")


# Main program
while True:

    print("\n==============================")
    print("   OHM'S LAW CALCULATOR")
    print("==============================")

    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    try:
        if choice == "1":
            calculate_voltage()

        elif choice == "2":
            calculate_current()

        elif choice == "3":
            calculate_resistance()

        elif choice == "4":
            calculate_power()

        elif choice == "5":
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice! Please select 1-5.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

