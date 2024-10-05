import oop2

employee_payroll = oop2.Employee_Salary()
emp_rate_per_hour = float(input("Enter the value rate per hour: "))
emp_num_of_absences = int(input("Enter value for number of absences: "))
tardiness_hours = int(input("Enter number of tardiness: "))

absences_deduction = employee_payroll.get_absences_deduction(emp_rate_per_hour, emp_num_of_absences)
tardiness_deduction = employee_payroll.get_tardiness_deduction(emp_rate_per_hour,tardiness_hours)

partial_deduction =absences_deduction + tardiness_deduction
print("Employeed partial deduction is: %.2f" % partial_deduction)


