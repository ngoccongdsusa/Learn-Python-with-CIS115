 #This program calculates the payroll for employees based on their hours worked and pay rate.

# Declare the variables
employee_name = ""
employee_id = 0
department = ""
pay_type = ""
hours_worked = 0.0
overtime_hours = 0.0
pay_rate = 0.0
ovetime_rate = 0.0
overtime_pay = 0.0
job_code = 0
regular_pay = 0.0
gross_pay = 0.0
federal_tax = 0.0
state_tax = 0.0
social_security = 0.0
medicare = 0.0
number_of_dependents = 0
total_withholding = 0.0
take_home_pay = 0.0

# Declare the constants variables
FEDERAL_TAX = 6.5
STATE_TAX = 3.99
SOCIAL_SECURITY_RATE = 6.2 #Corrected
DEPENDENT_RATE = 2.5
FEDERAL_MEDICARE_RATE = 1.45 #Corrected
UNION_DUES = 14.75
U401K_PRE = 21.6

# Get the user input for hours worked, pay rate, job code, and number of dependents
employee_name = input("Enter the employee's name: ")
employee_id = int(input("Enter the employee's ID: "))
department = ["Sales", "Marketing", "IT", "HR", "Accounting"]
pay_type = input("Enter the employee's pay type (Hourly/Salaried): ")
hours_worked = float(input("Enter the number of hours worked: "))
number_of_dependents = int(input ("Enter the number of dependents: "))
job_code = int(input("Enter the job code (1, 2, or 3): ")) 


# Perform pay rate based on job code
if job_code == 1:
    pay_rate = 17.00
elif job_code == 2:
    pay_rate = 18.00
elif job_code == 3:
    pay_rate = 19.00
else:
    print("Invalid job code. Please enter a valid job code (1, 2, or 3).")
    exit()

#Perform gross pay calcualtions base on hours worked and pay rate, including overtime pay if applicable
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_rate = pay_rate * 1.5
    regular_pay = 40 * pay_rate
    overtime_pay = overtime_hours * overtime_rate
    gross_pay = regular_pay + overtime_pay
else:
    overtime_hours = 0
    overtime_rate = 0
    regular_pay = hours_worked * pay_rate
    gross_pay = regular_pay


# Perform the caculations for gross pay,
federal_tax = gross_pay * (FEDERAL_TAX / 100)
state_tax = gross_pay * (STATE_TAX / 100)
social_security = gross_pay * (SOCIAL_SECURITY_RATE / 100)
medicare = gross_pay * (FEDERAL_MEDICARE_RATE / 100)
dependent_withholding = (number_of_dependents * DEPENDENT_RATE) * gross_pay
total_withholding = federal_tax + state_tax + social_security + medicare + dependent_withholding + UNION_DUES + U401K_PRE
take_home_pay = gross_pay - total_withholding



#Print the gross pay, total withoutholding, and take home pay
print(f" Name of employee: {employee_name}")
print(f"Employee ID: {employee_id} ")
print(f"Department: {department}")
print(f"Total Hours Worked: {hours_worked}")
print(f"Regular Hours: {hours_worked - overtime_hours}")
print(f"Overtime Housrs: {overtime_hours}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Overtime Rate: ${overtime_rate:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
print(f"TX Withholding Tax Federal: ${federal_tax:.2f}")
print(f"TX Withholding Tax State: ${state_tax:.2f}")
print(f"TX EE Social Security Tax Federal: ${social_security:.2f}")
print(f"TX EE Medicare Tax Federal: ${medicare:.2f}")
print(f"TX Withholding Tax Dependent: ${dependent_withholding:.2f}")
print(f"TX Withholding Tax Union Dues: ${UNION_DUES:.2f}")
print(f"TX Withholding Tax 401K Pre-Tax: ${U401K_PRE:.2f}")
print(f"Total Withholding: ${total_withholding:.2f}")
print(f"Total Net Pay: ${take_home_pay:.2f}")