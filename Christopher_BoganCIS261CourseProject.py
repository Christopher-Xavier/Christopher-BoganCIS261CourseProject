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

# Function to calculate income tax, net pay, and overtime
def calculate_pay(employee_data):
    for employee in employee_data:
        regular_hours = min(employee['hours'], 40)
        overtime_hours = max(employee['hours'] - 40, 0)
        regular_pay = regular_hours * employee['hourly_rate']
        overtime_pay = overtime_hours * employee['hourly_rate'] * 1.5
        gross_pay = regular_pay + overtime_pay
        income_tax = gross_pay * employee['tax_rate']
        net_pay = gross_pay - income_tax
        employee['regular_hours'] = regular_hours
        employee['overtime_hours'] = overtime_hours
        employee['gross_pay'] = gross_pay
        employee['income_tax'] = income_tax
        employee['net_pay'] = net_pay

# Function to display employee payment information
def display_employee_info(employee_data):
    for employee in employee_data:
        print(f"From date: {employee['from_date']}, To date: {employee['to_date']}, "
              f"Employee name: {employee['name']}, Regular hours: {employee['regular_hours']}, "
              f"Overtime hours: {employee['overtime_hours']}, Hourly rate: {employee['hourly_rate']}, "
              f"Gross pay: {employee['gross_pay']}, Income tax rate: {employee['tax_rate']}, "
              f"Income taxes: {employee['income_tax']}, Net pay: {employee['net_pay']}")

# Function to update and display totals
def display_totals(employee_data):
    totals = {
        'total_employees': len(employee_data),
        'total_hours': sum(employee['regular_hours'] for employee in employee_data),
        'total_overtime_hours': sum(employee['overtime_hours'] for employee in employee_data),
        'total_tax': sum(employee['income_tax'] for employee in employee_data),
        'total_net_pay': sum(employee['net_pay'] for employee in employee_data)
    }
    print(f"Total employees: {totals['total_employees']}, Total regular hours: {totals['total_hours']}, "
          f"Total overtime hours: {totals['total_overtime_hours']}, Total tax: {totals['total_tax']}, "
          f"Total net pay: {totals['total_net_pay']}")

# Function to save employee data to a file
def save_to_file(employee_data, filename="employee_data.txt"):
    with open(filename, "a") as file:
        file.writelines(
            f"{employee['from_date']}|{employee['to_date']}|{employee['name']}|{employee['hours']}|{employee['hourly_rate']}|{employee['tax_rate']}\n"
            for employee in employee_data
        )

# Function to parse employee record from file
def parse_employee_record(record):
    from_date_record, to_date_record, name, hours, hourly_rate, tax_rate = record.strip().split('|')
    return {
        'from_date': from_date_record,
        'to_date': to_date_record,
        'name': name,
        'hours': float(hours),
        'hourly_rate': float(hourly_rate),
        'tax_rate': float(tax_rate)
    }

# Function to read employee data from a file and generate a report
def generate_report(filename="employee_data.txt"):
    from_date_str = input("Enter the from date for the report (mm/dd/yyyy) or 'All' to display all records: ")
    if from_date_str.lower() != 'all':
        try:
            from_date = datetime.datetime.strptime(from_date_str, '%m/%d/%Y')
        except ValueError:
            print("Invalid date format. Please try again.")
            return

    totals = {'total_employees': 0, 'total_hours': 0, 'total_overtime_hours': 0, 'total_tax': 0, 'total_net_pay': 0}
    with open(filename, "r") as file:
        for line in file:
            try:
                employee = parse_employee_record(line)
                if from_date_str.lower() == 'all' or employee['from_date'] == from_date_str:
                    calculate_pay([employee])
                    display_employee_info([employee])
                    totals['total_employees'] += 1
                    totals['total_hours'] += employee['regular_hours']
                    totals['total_overtime_hours'] += employee['overtime_hours']
                    totals['total_tax'] += employee['income_tax']
                    totals['total_net_pay'] += employee['net_pay']
            except ValueError as e:
                print(f"Error processing record: {line.strip()} - {e}")

    print(f"Total employees: {totals['total_employees']}, Total regular hours: {totals['total_hours']}, "
          f"Total overtime hours: {totals['total_overtime_hours']}, Total tax: {totals['total_tax']}, "
          f"Total net pay: {totals['total_net_pay']}")

# Main loop to get employee data
employee_data = []
try:
    while True:
        from_date, to_date = get_dates()
        name = input("Enter the employee's name: ")
        try:
            hours = float(input("Enter the total hours worked: "))
            hourly_rate = float(input("Enter the hourly rate: "))
            tax_rate = float(input("Enter the income tax rate (as a decimal): "))
        except ValueError:
            print("Invalid input. Please enter numeric values for hours, hourly rate, and tax rate.")
            continue
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

# Save data to file
save_to_file(employee_data)

# Calculate pay and display information
calculate_pay(employee_data)
display_employee_info(employee_data)
display_totals(employee_data)

# Generate report
generate_report()
