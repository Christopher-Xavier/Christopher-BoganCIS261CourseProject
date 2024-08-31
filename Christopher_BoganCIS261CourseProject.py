import datetime

# Part 1: Initial Application

def open_file():
    with open('user_data.txt', 'a+') as file:
        file.seek(0)
        users = [line.split('|')[0] for line in file.readlines()]
    return users

def add_user(users):
    while True:
        user_id = input("Enter User ID (or type 'End' to finish): ")
        if user_id.lower() == 'end':
            break
        if user_id in users:
            print("User ID already exists.")
            continue
        password = input("Enter Password: ")
        auth_code = input("Enter Authorization Code (Admin/User): ")
        if auth_code not in ['Admin', 'User']:
            print("Invalid Authorization Code.")
            continue
        with open('user_data.txt', 'a') as file:
            file.write(f"{user_id}|{password}|{auth_code}\n")
        users.append(user_id)

def display_users():
    with open('user_data.txt', 'r') as file:
        for line in file:
            print(line.strip())

# Part 2: Updating the Application

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

def login_process():
    users = []
    with open('user_data.txt', 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 3:
                user_id, password, auth_code = parts
                users.append(Login(user_id, password, auth_code))
            else:
                print(f"Skipping invalid line: {line.strip()}")
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")
    for user in users:
        if user.user_id == user_id and user.password == password:
            print(f"Welcome {user_id}!")
            return
    print("Invalid User ID or Password.")

# Example usage
users = open_file()
add_user(users)
display_users()
login_process()

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
        'total_gross_pay': sum(employee['gross_pay'] for employee in employee_data),
        'total_income_tax': sum(employee['income_tax'] for employee in employee_data),
        'total_net_pay': sum(employee['net_pay'] for employee in employee_data)
    }
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours: {totals['total_hours']}")
    print(f"Total Overtime Hours: {totals['total_overtime_hours']}")
    print(f"Total Gross Pay: {totals['total_gross_pay']}")
    print(f"Total Income Tax: {totals['total_income_tax']}")
    print(f"Total Net Pay: {totals['total_net_pay']}")

# Function to save employee data to a file
def save_to_file(employee_data, filename="employee_data.txt"):
    with open(filename, 'w') as file:
        for employee in employee_data:
            line = f"{employee['from_date']}|{employee['to_date']}|{employee['name']}|{employee['hours']}|{employee['hourly_rate']}|{employee['tax_rate']}\n"
            file.write(line)

# Example usage for employee data
employee_data = [
    {'from_date': '08/01/2024', 'to_date': '08/15/2024', 'name': 'John Doe', 'hours': 45, 'hourly_rate': 20, 'tax_rate': 0.2},
    {'from_date': '08/01/2024', 'to_date': '08/15/2024', 'name': 'Jane Smith', 'hours': 38, 'hourly_rate': 22, 'tax_rate': 0.18}
]

calculate_pay(employee_data)
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
                employee = parse_employee_record(line) # type: ignore
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
