#Start

#Initialize variable
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
philhealth_contribution = 0.05 * gross_earnings
deductions = absences + tardy + withholding_tax + sss_contribution + pagibig_contribution + philhealth_contribution
net_pay = gross_earnings - deductions

#SSS contribution based on gross earnings
if gross_earnings < 4250:
    sss_contribution = 180.00
elif 4250 <= gross_earnings <= 4749.99:
    sss_contribution = 202.50
elif 4750 <= gross_earnings <= 5249.99:
    sss_contribution = 225.00
elif 5250 <= gross_earnings <= 5749.99:
    sss_contribution = 247.50
elif 5750 <= gross_earnings <= 6249.99:
    sss_contribution = 270.00
elif 6250 <= gross_earnings <= 6749.99:
    sss_contribution = 292.50
elif 6750 <= gross_earnings <= 7249.99:
    sss_contribution = 315.00
elif 7250 <= gross_earnings <= 7749.99:
    sss_contribution = 337.50
elif 7750 <= gross_earnings <= 8249.99:
    sss_contribution = 360.00
elif 8250 <= gross_earnings <= 8749.99:
    sss_contribution = 382.50
elif 8750 <= gross_earnings <= 9249.99:
    sss_contribution = 405.00
elif 9250 <= gross_earnings <= 9749.99:
    sss_contribution = 427.50
elif 9750 <= gross_earnings <= 10249.99:
    sss_contribution = 450.00
elif 10250 <= gross_earnings <= 10749.99:
    sss_contribution = 472.50
elif 10750 <= gross_earnings <= 11249.99:
    sss_contribution = 495.00
elif 11250 <= gross_earnings <= 11749.99:
    sss_contribution = 517.50
elif 11750 <= gross_earnings <= 12249.99:
    sss_contribution = 540.00
elif 12250 <= gross_earnings <= 12749.99:
    sss_contribution = 562.50
elif 12750 <= gross_earnings <= 13249.99:
    sss_contribution = 585.00
elif 13250 <= gross_earnings <= 13749.99:
    sss_contribution = 607.50
elif 13750 <= gross_earnings <= 14249.99:
    sss_contribution = 630.00
elif 14250 <= gross_earnings <= 14749.99:
    sss_contribution = 652.50
elif 14750 <= gross_earnings <= 15249.99:
    sss_contribution = 675.00
elif 15250 <= gross_earnings <= 15749.99:
    sss_contribution = 697.00
elif 15750 <= gross_earnings <= 16249.99:
    sss_contribution = 720.00
elif 16250 <= gross_earnings <= 16749.99:
    sss_contribution = 742.50
elif 16750 <= gross_earnings <= 17249.99:
    sss_contribution = 765.00
elif 17250 <= gross_earnings <= 17749.99:
    sss_contribution = 787.00
elif 17750 <= gross_earnings <= 18249.99:
    sss_contribution = 810.00
elif 18250 <= gross_earnings <= 18749.99:
    sss_contribution = 832.00
elif 18750 <= gross_earnings <= 19249.99:
    sss_contribution = 855.00
elif 19250 <= gross_earnings <= 19749.99:
    sss_contribution = 877.00
else:
    sss_contribution = 900.00

#Compute the PhilHealth contribution
philhealth_contribution = gross_earnings * 0.05

#Withholding tax calculation
if 0 <= gross_earnings < 10417:
    tax = 0
elif 10417 <= gross_earnings <= 16666:
    tax = 0 + 0.15 * (gross_earnings - 10417)
elif 16667 <= gross_earnings <= 33332:
    tax = 937.50 + 0.20 * (gross_earnings - 16667)
elif 33333 <= gross_earnings <= 83332:
    tax = 4270.70 + 0.25 * (gross_earnings - 33333)
elif 83333 <= gross_earnings <= 333332:
    tax = 16770.70 + 0.30 * (gross_earnings - 83333)
else:
    tax = 91770.70 + 0.35 * (gross_earnings - 333333)

#Compute deductions
deduction = absences + tardy + tax + sss_contribution + philhealth_contribution + pagibig_contribution

#Compute net pay
net_pay = gross_earnings - deduction

#Output results
print("><--- EMPLOYEE SALARY DETAILS---><")
print("Company: ", company_name)
print("Employee Code: ", employee_code)
print("Employee Name: ", employee_name)
print("Department: ", department)
print("Cut Off: ", salary_cutoff)
print("Basic Pay: ", basic_pay)
print("Overtime Pay: ", overtime_pay)
print("Absent Deduction: ", absences)
print("Honorarium: ", honorarium)
print("Tardiness Deduction: ", tardy)
print("Withholding Tax: ", tax)
print("SSS Contribution: ", sss_contribution)
print("PhilHealth Contribution: ", philhealth_contribution)
print("Pag-IBIG Contribution: ", pagibig_contribution)
print("Gross Earnings: ", gross_earnings)
print("Net Pay: ", net_pay)