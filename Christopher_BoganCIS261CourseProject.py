import datetime

# Function to get dates in the format mm/dd/yyyy
def get_dates():
    while True:
        from_date_str = input("Enter the from date (mm/dd/yyyy): ")
        to_date_str = input("Enter the to date (mm/dd/yyyy): ")
        try:
            from_date = datetime.datetime.strptime(from_date_str, '%m/%d/%Y')
            to_date = datetime.datetime.strptime(to_date_str, '%m/%d/%Y')
            if from_date <= to_date:
                return from_date_str, to_date_str
            else:
                print("The from date must be before the to date.")
        except ValueError:
            print("Invalid date format. Please try again.")

# Function to calculate income tax and net pay
def calculate_pay(employee_data):
    for employee in employee_data:
        gross_pay = employee['hours'] * employee['hourly_rate']
        income_tax = gross_pay * employee['tax_rate']
        net_pay = gross_pay - income_tax
        employee['gross_pay'] = gross_pay
        employee['income_tax'] = income_tax
        employee['net_pay'] = net_pay

# Function to display employee payment information
def display_employee_info(employee_data):
    for employee in employee_data:
        print(f"From date: {employee['from_date']}, To date: {employee['to_date']}, "
              f"Employee Name: {employee['name']}, Hours Worked: {employee['hours']}, "
              f"Hourly Rate: {employee['hourly_rate']}, Gross Pay: {employee['gross_pay']}, "
              f"Income Tax Rate: {employee['tax_rate']}, Income Taxes: {employee['income_tax']}, "
              f"Net Pay: {employee['net_pay']}")

# Function to update and display totals
def display_totals(employee_data):
    totals = {'total_employees': 0, 'total_hours': 0, 'total_tax': 0, 'total_net_pay': 0}
    for employee in employee_data:
        totals['total_employees'] += 1
        totals['total_hours'] += employee['hours']
        totals['total_tax'] += employee['income_tax']
        totals['total_net_pay'] += employee['net_pay']
    print(f"Total Employees: {totals['total_employees']}, Total Hours: {totals['total_hours']}, "
          f"Total Tax: {totals['total_tax']}, Total Net Pay: {totals['total_net_pay']}")

# Main loop to get employee data
employee_data = []
try:
    while True:
        from_date, to_date = get_dates()
        name = input("Enter the employee's name: ")
        hours = float(input("Enter the total hours worked: "))
        hourly_rate = float(input("Enter the hourly rate: "))
        tax_rate = float(input("Enter the income tax rate (as a decimal): "))
        employee_data.append({
            'from_date': from_date,
            'to_date': to_date,
            'name': name,
            'hours': hours,
            'hourly_rate': hourly_rate,
            'tax_rate': tax_rate
        })
        if input("Enter 'done' to finish, or press any other key to continue: ") == 'done':
            break
except Exception as e:
    print(f"An error occurred: {e}")

# Calculate pay and display information
calculate_pay(employee_data)
display_employee_info(employee_data)
display_totals(employee_data)