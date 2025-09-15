Monthly_income = input("Enter your monthly income: ")
Total_monthly_expenses = input("Enter your total monthly expenses: ")
Monthly_Savings = Monthly_income - Total_monthly_expenses
print(f"Your monthly savings is: {Monthly_Savings}")
projected_Savings = Monthly_Savings * 12 + Monthly_Savings * 12 * 0.05
print(f"Your projected savings after one year, with interest is: ${projected_Savings}")
