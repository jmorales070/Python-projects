#
# Pennies to Pay
# Calculates the amount of money a person would earn over a period of time
# Input(s)
#  days, amount
#
# Output
#  total_pay, each_day_pay

import pyinputplus as pyip

# Constants
# how much the salary increases each day
each_day_increase = 2

def main():
    # User knows what the program does
    print('This program calculates the amount of money a person would earn over a period of time.')

    try:
        # Ask user for the number of days, and check for input errors
        days = pyip.inputInt('\nEnter the number of days: ', min=1)

        # Ask user for the amount of money they desire each day, and check for input errors
        amount = pyip.inputFloat('Enter the amount of money you desire each day: ', min=0.01)

        # Initialize variables
        total_pay = 0
        each_day_pay = amount

        # Display header
        print('\n' + '~' * 23)
        print('Day \tSalary')
        print('-' * 23)

        # Loop through each day
        for day in range(1, days + 1):
            # Print the salary for each day
            print(f'{day:<5} \t${each_day_pay:>10.2f}')
            # Calculates the total pay
            total_pay += each_day_pay
            # Calculates the salary for the next day
            each_day_pay *= each_day_increase
        
        # Display the total pay
        print('-' * 23)
        print(f'Total pay: ${total_pay:>7.2f}')
        print('~' * 23)

    except Exception as e:
        print(f'<<< Something went wrong: {e} >>>')

    # User knows program ended
    print("\nProgram ends.")
    
# Call the main function
main()
