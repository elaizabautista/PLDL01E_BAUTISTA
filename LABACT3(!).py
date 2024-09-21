# Employee Salary Calculation Program

# Start

# Initialize variables
company_name = input("Enter Company Name: ")
department = input("Enter Department: ")  # Corrected to reflect the actual department
employee_code = input("Enter Employee Code: ")
employee_name = input("Enter Employee Name: ")
salary_cutoff = input("Enter Salary Date Cut-off: ")

# Salary Information
print("\n--- Salary Information ---")
rate_per_hour = float(input("Enter Rate Per Hour: "))
hours_per_payday = float(input("Enter Hours Per Payday: "))
overtime_hours = float(input("Enter Overtime Hours: "))
absence_hours = float(input("Enter Absence Hours: "))
honorarium = float(input("Enter Honorarium: "))
tardy_hours = float(input("Enter Tardy Hours: "))
pagibig_contribution = 100.00

# Calculate
basic_pay = rate_per_hour * hours_per_payday
overtime_pay = rate_per_hour * overtime_hours
absences = rate_per_hour * absence_hours
tardy = rate_per_hour * tardy_hours
gross_earnings = basic_pay + overtime_pay + honorarium
withholding_tax = 0.10 * gross_earnings
sss_contribution = 0.05 * gross_earnings
philhealth_contribution = 0.03 * gross_earnings
deductions = (absences + tardy + withholding_tax + sss_contribution + pagibig_contribution + philhealth_contribution)
net_pay = gross_earnings - deductions

# Output
print("\n--- Salary Summary ---")
print(f"Company Name: {company_name}")
print(f"Department: {department}")
print(f"Employee Code: {employee_code}")
print(f"Employee Name: {employee_name}")
print(f"Salary Date Cut-off: {salary_cutoff}")
print(f"Basic Pay: {basic_pay:.2f}")
print(f"Overtime Pay: {overtime_pay:.2f}")
print(f"Absences: {absences:.2f}")
print(f"Honorarium: {honorarium:.2f}")
print(f"Tardy: {tardy:.2f}")
print(f"Withholding Tax: {withholding_tax:.2f}")
print(f"SSS Contribution: {sss_contribution:.2f}")
print(f"Pag-IBIG Contribution: {pagibig_contribution:.2f}")
print(f"PhilHealth Contribution: {philhealth_contribution:.2f}")
print(f"Deductions: {deductions:.2f}")
print(f"Gross Earnings: {gross_earnings:.2f}")
print(f"Net Pay: {net_pay:.2f}")
