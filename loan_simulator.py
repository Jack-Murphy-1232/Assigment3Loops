def loan_simulator():
    loan_amount = float(input("Enter loan amount: "))
    interest_rate = float(input("Enter annual interest rate (%): "))
    monthly_payment = float(input("Enter monthly payment: "))
    
    balance = loan_amount
    months = 0
    
    while balance > 0:
        interest = balance * interest_rate / 100 / 12
        balance = balance + interest
        balance = balance - monthly_payment
        months = months + 1
    
    print("Loan paid off in", months, "months.")

loan_simulator()
