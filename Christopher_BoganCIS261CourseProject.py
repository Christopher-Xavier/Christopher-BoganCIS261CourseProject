def get_employee_name():
	return input("Enter employee's name: ")

def get_total_hours():
	return float(input("Enter total hours worked: "))

def get_hourly_rate():
	return float(input("Enter hourly rate: "))

def get_income_tax_rate():
	return float(input("Enter income tax rate (as a decimal): "))

def calculate_pay(total_hours, hourly_rate, tax_rate):
	gross_pay = total_hours * hourly_rate
	income_tax = gross_pay * tax_rate
	net_pay = gross_pay - income_tax
	return gross_pay, income_tax, net_pay

def display_employee_info(name, total_hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay):
	print(f"\nEmployee Name: ${name}")
	print(f"Total Hours Worked: ${total_hours}")
    print(f"Hourly Rate: ${hourly_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate:{tax_rate * 100:.2f}%")
	print(f"Income Tax: ${income_tax:.2f}")
	print(f"Net Pay: ${net_pay:.2f}\n")
	 
def display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
	print("\n--- Totals ---")
	print(f"Total Number of Employees: {total_employees}")
	print(f"Total Hours Worked: ${total_hours}")
	print(f"Total Gross Pay: ${total_gross_pay:.2f}") 
	print(f"Total Income Tax: ${total_tax:.2f}")
	print(f"Total Net Pay: ${total_net_pay:.2f}")

def main():
	total_employees = 0
	total_hours = 0
	total_gross_pay = 0
	total_net_pay = 0
	while True:
		name = get_employee_name()
   if name.lower() == "end":
	  break
	total_hours_worked = get_total_hours()
	hourly_rate = get_hourly_rate()
	tax_rate = get_income_tax_rate()
gross_pay, income_tax, net_pay = calculate_pay(total_hours_worked, hourly_rate, tax_rate)
display_employee_info(name, total_hours_worked, hourly_rate, gross_pay, tax_rate, income_tax, net_pay)
   total_employees += 1
		total_hours += total_hours_worked
		total_gross_pay += gross_pay
		total_tax += income_tax
		total_net_pay += net_pay, total_net_pay

	display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
	if __name__ == "__main__":
		main()