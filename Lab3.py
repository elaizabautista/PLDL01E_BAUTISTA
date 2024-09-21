#start

#initialize variable
pagibig_contribution = 100.00

#Input
#Company Information
print("><--- Company Information ---><")
company_name = input("Company Name: ")
department = input("Department: ")
employee_code = input("Employee Code: ")
employee_name = input("Employee Name: ")
salary_cutoff = input("Salary Date Cut-off: ")

#Salary Information
print("><--- Salary Information ---><")
rate_per_hour = float(input("Rate per Hour: "))
hours_per_payday = float(input("Number of Hours per Payday: "))
overtime_hours = float(input("Number of Overtime Hours: "))
absence_hours = float(input("Number of Absence Hours: "))
honorarium = float(input("Honorarium: "))
tardy_hours = float(input("Number of Tardy Hours: "))

#Calculate
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

#SSScontribution
