"""
 - Interest rate calculator
    -Compound, simple, continuous interest; allow user to input principle amount, interest rate, time period.
    -Future value of savings
- Loan calculator
    Calculates monthly payment, total payment.
    User inputs loan amount, interest rate, loan duration
    Amortisation - split payment into principle and interest
- Allow user to convert interest rates for comparison
    - Nominal vs Real (inflation taken into account)
    - Different times
- File handling
    - Create reports and summaries
    - Create databases
    - Create graphs and visualisations
- Error handling
- GUI? Tkinter
"""


# Savings calculator
def calculate_balance(interest_type, principle, interest, time):
    if interest_type == "1":
        balance = principle * (1 + interest * time)
    elif interest_type == "2":
        pass
    else:
        return


while True:
    print("Welcome!")
    print(
        """
        1. Savings
        2. Loans
        3. Interest Rate Converter
        4. Exit\n"""
    )

    choice = input("Please choose an option: ")

    if choice == "1":
        print("Savings")
        interest_type = input(
            """
            1. Simple
            2. Compound\n"""
        )
        principle = float(input("Enter principle value: "))
        interest = float(input("Enter interest rate: "))
        time = float(input("Enter term (years): "))
        balance = calculate_balance(interest_type, principle, interest, time)
    elif choice == "2":
        break
    elif choice == "3":
        break
    elif choice == "4":
        print("Exiting application...")
        exit()
    else:
        print("Invalid choice...\n")
