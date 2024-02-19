# Initialize stock quantities and other relevant variables
samosa_stock = 0  # Quantity of samosas in stock
roll_stock = 0  # Quantity of rolls in stock
samosa_price = 30  # Price per samosa
roll_price = 40  # Price per roll
employee1_hours_worked = 0  # Hours worked by employee 1
employee2_hours_worked = 0  # Hours worked by employee 2
employee1_wage_rate = 0  # Wage rate per hour for employee 1
employee2_wage_rate = 0  # Wage rate per hour for employee 2
total_samosas_sold = 0  # Total samosas sold
total_rolls_sold = 0  # Total rolls sold
boutique_sales_amount = 0  # Sales amount from the boutique

# Function to add samosa and roll in stock
def add_stock(quantity_samosa, quantity_roll):
    global samosa_stock, roll_stock
    samosa_stock += quantity_samosa
    roll_stock += quantity_roll

# Function to show quantity of samosa and roll in stock
def show_stock_quantity():
    print('Samosa Stock:', samosa_stock, 'Roll Stock:', roll_stock)

# Function to order roll and samosa, generate bill, and adjust stock
def place_order(ordered_roll, ordered_samosa):
    global samosa_stock, roll_stock, total_samosas_sold, total_rolls_sold
    if samosa_stock < ordered_samosa:
        if samosa_stock != 0:
            print('We have only samosas', samosa_stock, "\nPlease order within our stock")
        else:
            print('Samosa out of stock')
    elif samosa_stock >= ordered_samosa:
        samosa_stock -= ordered_samosa
        total_samosas_sold += ordered_samosa
        samosa_bill = ordered_samosa * samosa_price
        print('Samosa price', samosa_bill)

    if roll_stock < ordered_roll:
        if roll_stock != 0:
            print("Rolls in stock left", roll_stock, "\nPlease order within our stock")
        else:
            print('Rolls out of stock')
    elif roll_stock >= ordered_roll:
        roll_stock -= ordered_roll
        total_rolls_sold += ordered_roll
        roll_bill = ordered_roll * roll_price
        print('Roll price', roll_bill)

# Function to set employee wage rate input by the user
def set_employee_wage_rate(wage_rate_employee1, wage_rate_employee2):
    global employee1_wage_rate, employee2_wage_rate
    employee1_wage_rate = wage_rate_employee1
    employee2_wage_rate = wage_rate_employee2
    print(f'Wage rate per hour for employee 1 is set to {employee1_wage_rate} and employee 2\'s is {employee2_wage_rate}')

# Function to add hours worked by each employee
def add_hours_worked(hours_employee1, hours_employee2):
    global employee1_hours_worked, employee2_hours_worked
    employee1_hours_worked += hours_employee1
    employee2_hours_worked += hours_employee2
    print(f'Worked hours of both employees are updated, employee 1 hrs are {employee1_hours_worked} and 2 hrs are {employee2_hours_worked}')

# Function to calculate salary of employees
def calculate_salary():
    salary_employee1 = employee1_wage_rate * employee1_hours_worked
    salary_employee2 = employee2_wage_rate * employee2_hours_worked
    print('Employee 1 salary for', employee1_hours_worked, 'hours:', salary_employee1,
          "\nEmployee 2 salary for", employee2_hours_worked, "hours is", salary_employee2)

# Function to calculate bonus if sales in 1 hr reach 100 (50 samosa and 50 roll)
def issue_bonus():
    if employee1_hours_worked <= 1 and total_samosas_sold >= 50 and total_rolls_sold >= 50:
        bonus_employee1 = employee1_wage_rate * 0.1
        print('Bonus is awarded to employee 1 as sales in 1 hr of samosas and rolls are equal or more than half of stock:', bonus_employee1)
    else:
        print('Bonus is not awarded to employee 1 as sales in 1 hr of samosas and rolls are not equal or more than half of stock')

    if employee2_hours_worked <= 1 and total_samosas_sold >= 50 and total_rolls_sold >= 50:
        bonus_employee2 = employee2_wage_rate * 0.1
        print("Bonus is awarded to employee 2 as sales in 1 hr of samosas and rolls are equal or more than half of stock:", bonus_employee2)
    else:
        print('Bonus is not awarded to employee 2 as sales in 1 hr of samosas and rolls are not equal or more than half of stock')

# If boutique sales is greater than 15000, provide 1 dozen samosas and rolls for free
def provide_boutique_bonus():
    global boutique_sales_amount, samosa_stock, roll_stock
    if boutique_sales_amount >= 15000:
        samosa_stock -= 12
        roll_stock -= 12
        print('Congratulations! You got free 1 dozen samosas and rolls from my bake shop for buying clothes of more than 15000 from our boutique shop')
    else:
        print("Oops! You don't get free 1 dozen samosas and rolls for not buying clothes of more than 15000 from our boutique shop")

# Main program loop
while True:
    print('Welcome to the bake shop\n1 For add items in stock \n2 For show quantity of stock\n3 For place order and generate bill\n4 For set employee wage rate\n5 For add hours worked by employees\n6 For calculate salary of employees\n7 For issue bonus\n8 For provide boutique customers free samosas and rolls\n9 For exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        quantity_samosa = int(input('Add samosa in stock: '))
        quantity_roll = int(input('Add roll in stock: '))
        add_stock(quantity_samosa, quantity_roll)
        print('Samosas and rolls are successfully added into stock')
        show_stock_quantity()
    if choice == 2:
        show_stock_quantity()
    if choice == 3:
        ordered_roll = int(input('Order roll: '))
        ordered_samosa = int(input('Order samosa: '))
        place_order(ordered_roll, ordered_samosa)
    if choice == 4:
        wage_rate_employee1 = float(input('Wage rate per hour for employee A: '))
        wage_rate_employee2 = float(input('Wage rate per hour for employee B: '))
        set_employee_wage_rate(wage_rate_employee1, wage_rate_employee2)
    if choice == 5:
        hours_employee1 = float(input('Hours worked by employee A: '))
        hours_employee2 = float(input('Hours worked by employee B: '))
        add_hours_worked(hours_employee1, hours_employee2)
    if choice == 6:
        calculate_salary()
    if choice == 7:
        issue_bonus()
    if choice == 8:
        boutique_sales_amount = float(input("Enter customer's bought price: "))
        provide_boutique_bonus()
    if choice == 9:
        break
