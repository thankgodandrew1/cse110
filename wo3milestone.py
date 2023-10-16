# This is about a program to calculate the price of a meal
# I import math to use its library
# I prefer using single quote on my code due to the apostrophe on the child i had to use double quote on the first code 
 
import math
print('Please input the value for the following:\n ')

child_meal = float(input("What is the price of a child's meal? "))
drinks = float(input("What is the price of a child's drink? "))
adult_meal = float(input("What is the price of an adult's meal? "))
appetizers = float(input("What is the price of an adult's appetizer? "))

# On this 3rd line of code i returned to my single quote
# I asked for the number of the adults and children including tax rate
child_num = int(input('How many childeren are there? '))
adult_num = int(input('How many adult are there? '))
tax = float(input('what is the sales tax rate? '))

# On the next lines i created a program to determine: subtotal, sales_tax, and total. 
meal = child_meal + drinks
Adult_meal = adult_meal + appetizers
meal_subtotal =(meal * child_num) + (Adult_meal * adult_num)
print(f'\nSubtotal: ${meal_subtotal:.2f}')

sales_tax = (meal_subtotal) * (tax) / 100                  
print (f'Sales tax: ${sales_tax:.2f}')

Total_price= meal_subtotal + sales_tax
print (f'Total: ${Total_price:.2f}' )

# I requested for the payment amount to determine if there be change for the buyer.

payment = float(input('\nWhat is the payment amount? '))
change_amount = payment - Total_price
print(f'Change: ${change_amount:.2f}')


# Based on the program i worked on i think i fit into the first grading category, i was able to work on
# the requiremts and also clearly inputted an additional order for both the adult and the child
# which is the drink and the appetizer  

