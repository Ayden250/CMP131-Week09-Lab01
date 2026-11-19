#Ayden
#131
#9
#1
#Future Value
#November 18, 2026

def futureValue(present_value, interest_rate, months):
    future_value = present_value * (1 + interest_rate) ** months
    return future_value


def main():
    print("FUTURE VALUE PROGRAM")
    
    present_value = float(input("Enter the present value of the account: $"))

    while present_value < 0:
        print("Error: Present value cannot be negative.")
        present_value = float(input("Enter the present value of the account: $"))

    interest_percentage = float(input("Enter the monthly interest rate (%): "))

    while interest_percentage < 0:
        print("Error: Interest rate cannot be negative.")
        interest_percentage = float(input("Enter the monthly interest rate (%): "))

    interest_rate = interest_percentage / 100

    months = int(input("Enter the number of months: "))

    while months <= 0:
        print("Error: Number of months must be greater than zero.")
        months = int(input("Enter the number of months: "))

    result = futureValue(present_value, interest_rate, months)

    print("\n)
    print("ACCOUNT SUMMARY")
    print(f"Present Value:          ${present_value:,.2f}")
    print(f"Monthly Interest Rate:   {interest_percentage:.2f}%")
    print(f"Number of Months:        {months}")
    print(f"Future Value:            ${result:,.2f}")
main()
