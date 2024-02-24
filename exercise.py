#1. If the gross is less than 1000, then the income tax is 10%
#2. If the gross is less than 2000, then the income tax is 12%
#3. If the gross is less than 4000, then the income tax is 14%
#4. If the gross is more than 4000, then the income tax is 18%
#5. If the gross is less than 2000, every child gets you a tax cut of 1%
#6. If the gross is more than 2000, every child gets you a tax cut of 0.5%
#Read the "gross" and the number of children
#Print the "net"
#Use try/except when reading the inputs

try:
    # Read the gross salary and number of children
    gross = float(input("Enter gross salary: "))
    children = int(input("Enter the number of children: "))

    # Calculate income tax based on gross salary
    if gross < 1000:
        tax_rate = 0.10
    elif gross < 2000:
        tax_rate = 0.12
    elif gross < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    # Calculate tax cut based on the number of children
    if gross < 2000:
        child_tax_cut = 0.01 * children
    else:
        child_tax_cut = 0.005 * children

    # Calculate net salary
    income_tax = gross * (tax_rate-child_tax_cut)
    net = gross - income_tax

    # Print the net salary
    print(f"Net salary: {net:.2f}")

except ValueError:
    print("Error: Please enter valid numeric values for gross salary and number of children.")
