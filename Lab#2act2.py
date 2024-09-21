# Initialization
employee_name = ""
department = ""
total_deduction = 0
gross_income = 0
net_income = 0
pagibig_contribution = 100.00

#Input employee details and income data
employee_name = input("Enter employee's name: ")
department = input("Enter department: ")
rate_per_hour = float(input("Rate per hour: "))
hours_per_day = int(input("Hours per day: "))
days_per_week = int(input("Days per week: "))
weeks_per_month = int(input("Weeks per month: "))

#Calculate gross income
gross_income = rate_per_hour * hours_per_day * days_per_week * weeks_per_month

#Calculate SSS Contribution
if gross_income <= 20000:
    sss_contribution = 125.75
elif gross_income <= 50000:
    sss_contribution = 2200.50
elif gross_income <= 75000:
    sss_contribution = 4800.00
else:
    sss_contribution = 5800.00

#Calculate PhilHealth Contribution
if gross_income <= 20000:
    philhealth_contribution = 100.00
elif gross_income <= 50000:
    philhealth_contribution = 1200.00
elif gross_income <= 75000:
    philhealth_contribution = 6800.00

else:
    philhealth_contribution = 8800.00

# Calculate total deduction and net income
total_deduction = sss_contribution + philhealth_contribution + pagibig_contribution
net_income = gross_income - total_deduction

#Display results
print("employee name:", employee_name)
print("department:", department)
print("net income:", net_income)
print("gross income:", gross_income)
print("total deduction:", total_deduction)