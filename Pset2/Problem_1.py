"""
calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
"""
for i in range(12):
    balance = balance - (monthlyPaymentRate * balance) + ((balance - (monthlyPaymentRate * balance)) * (annualInterestRate / 12.0))
print("Remaining balance: ", round(balance, 2))    