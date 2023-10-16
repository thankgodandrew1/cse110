# pi = 0.14159
# print(pi)

# first_num = input('please enter number')
# second_num = input('please enter another number')
# print (int(first_num) + int(second_num))

# days_in_feb = 28
# print(f'the total number of days in febuary is {days_in_feb } ')
# print ( str (days_in_feb) + ' days in febuary')
# first_num = '5'
# second_num = '6'

# print(first_num+ second_num)

# colour = 'blue'
# animal = 'pig'
# print (colour+ ' ' + animal + '!')
# combined_word = (colour + ' ' + animal + '!' )
# print (combined_word)

# boys_count = 10
# print ('there are ' + str (boys_count) + ' boys' )
# girls_count = 12
# print (boys_count + girls_count)

# length_num = '12'
# width_num = '15 '
# print(length_num + width_num)


# age = int(input('How old are you? '))
# next_year_age = age + 1
# print(f'On your next birthday, you will be {next_year_age}.  ' )
# print()
# eggs = int (input('How many egg cartons do you have? '))
# total = eggs * 12
# print(f'You have {total} eggs')
# print()
# people = float (input ('\nHow many cookies do you have? '))
# people_num = float (input('How many people are there? '))
# divide = people/people_num
# print(f'Each person may have {divide} cookies')


# Area of a square
# side = float(input('what is the  length of a side of the square? '))
# area = side ** 2
# print(f'The area of the square is: {area}')

# Area of a reactangle
# length= float(input('\nwhat is the length of rectangle? '))
# width = float(input('what is the width of the traiangle? '))
# area = length*width
# print(f'The area of the rectangle is {area}')

# Area of a circle
# radius = float(input('\nwhat is the radius of the circle? '))
# area =3.14 * (radius ** 2)
# print (f'The area of the circle is: {area}')

# Stretch challenge using the math.py
# import math
# radius = float (input('\nwhat is the radius of a circle? '))
# area = math.pi * (radius ** 2)
# print(f'The area of a circle is: {area} ')

# Stretch challenge 2
# length = float(input('what is the value to be used? '))

# calculate areas

# area_square = value ** 2
# area_circle = math.pi * (value ** 2 )
# volume_cube = value ** 3
# volume_sphere =(4 / 3) * math.pi * ( value ** 3)
# display result
# print (f'Area of a square: {area_square}')
# print (f'Area of a circle {area_circle}')
# print (f'Volume of a cube: {volume_cube}')
# print (f'Volume of a sphere: {volume_sphere}')
# Stretch 3
# Area of a circle in m^2 and cm^2
# side = float(input('what is the length of a  side of the square (in cm)? '))
# print (f'The area of the square is: {side**2} cm^2 ')
# print(f'The area of the square is: {side**2 / 10000} m^2 ')

# Area of a Rectangle
# length = float(input('\nwhat is the length of rectangle (in cm)? '))
# width = float(input('what is the width of the rectangle (in cm)? '))

# print (f'The area of a rectangle is: {length} * {width} cm^2 ')
# print (f'The area of a rectangle is: {length} * {width} / 10000 m^2 ')


#                              W05 PREPARATION ACTIVITY

# price = float(input('How much did you pay? '))
# if price >= 1:
    # tax = .07
# else:
    # tax = 0
# print('Your tax rate is: ' + str (tax) )

# country = input('Nationality: ')

# if country.lower() == 'canada':
    # print('Oh look a canadian')
# else:
    # print('You are not a canadian')

# province = input('Which province do you reside?: ')
# if province.lower() in('alberta','nunavut', 'yukon'):
    # tax = 0.05
# elif province.lower() == 'madoga':
    #  tax = 0.08

# else:
    # tax = 0.15
# tax = str(tax)
# print(f'Tax rate is: ${tax}' )


# color = input('What is your favorite color? ')
# if color == 'blue':
    # print('I like blue too!')

# THIS IF STATEMENT WILL MATCH THE WORD BLUE, REGARDLESS OF THE CAPITALIZATION

# if color.lower() == 'blue':
    # print('I like blue too!')

                                # 05 PREPARE: CHECKPOINT
                                # I. COMPARING NUMBERS
# num_table = int(input('How many tables are in the truck?: '))
# num_chair = int(input('How many chairs are in the truck?: '))

# if num_table > num_chair:
#     print('The number of tables is greater ')
# else:
#     print('The number of tables is not greather')

# if num_table == num_chair:
#     print('The numbers of table and chairs are equal')
# else:
#     print('The numbers of tables and chairs are not equal ')

# if num_chair > num_table:
#     print('The number of chairs is greather')
# else:
#     print('The number of chairs is not greather')

#                                  # II. COMPARING STRINGS

# # animal = input('What is your favorite animal?: ')

# if animal.lower() == 'dog':
    # print('That is my favorite animal too!')
# else:
    # print('That one is not my favorite!')

                                 # W06 PREPARATION ACTIVITY

# gpa = float(input('What is your grade point average? '))
# lowest_grade = float(input('What was your lowest grade? '))

# if gpa >= .85 and lowest_grade >= .75:
#     honour_roll = True
# else:
#     honour_roll = False
# if honour_roll:
#     print('You made Honour Roll!!')

                         # W06 PREPARE: CHECKPOINT- QUALIFYING FOR A LOAN

# print('Qualifying for A Loan\n')

# print('On the next questions give a rating from 1-10:\n')

# loan = int(input('How large is the loan? '))
# credit_history = int(input('How good is your credit history? '))
# income = int(input('How high is your income? '))
# down_payment = int(input('How large is your down payment? '))

# is_loan = False
# # i was having an error on my code felt so fustrated i had to input is_loan = False this would set
# # the variable to a default value of 'False' that way, if some reason it doesn't get set in our
# # ru--les below it will not be left 'undefined' and cause an error, and i don't like to set it
# # to default to be True, because i don't want to accidentally give someone a loan!
# if loan >= 5:
#     if credit_history >= 7 and income >= 7:
#         is_loan = True


# if credit_history >= 7 or income >=7:
#     if down_payment >= 5:
#         is_loan = True
# else:
#     is_loan = False

# if not credit_history >= 7 or income >= 7:
#         is_loan = False
# if not is_loan >= 5:
#     if credit_history < 4:
#         is_loan = False
# else:
#     if income >= 7 or down_payment >= 7:
#         is_loan = True
# if income >= 4 and down_payment >= 4:
#      is_loan = True

# else:
#     is_loan = False

# if is_loan:
#     print('The decision is yes, this is a good loan.')
# else:
    # print('The decision is no, you should not loan this money.')




#     print('Qualifying for A Loan\n')

# print('On the next questions give a rating from 1-10:\n')

# loan = int(input('How large is the loan? '))
# credit_history = int(input('How good is your credit history? '))
# income = int(input('How high is your income? '))
# down_payment = int(input('How large is your down payment? '))

# is_loan = False
# # i was having an error on my code felt so fustrated i had to input is_loan = False this would set
# # the variable to a default value of 'False' that way, if some reason it doesn't get set in our
# # rules below it will not be left 'undefined' and cause an error, and i don't like to set it
# to default to be True, because i don't want to accidentally give someone a loan!
# # if loan >= 5:
# #     if credit_history >= 7 and income >= 7:
# #         is_loan = True

# #     elif credit_history >= 7 or income >=7:
# #         if down_payment >= 5:
# #             is_loan = True
# #         else:
# #             is_loan = False



# #     else:
# #          is_loan = False
# # else: # this means is a small loan

# #    if credit_history < 4:
# #         is_loan = False
# #    else:
# #        if income >= 7 or down_payment >= 7:
# #            is_loan == True
# #        elif income >= 4 and down_payment >= 4:
# #            is_loan = True

# #        else:
# #            is_loan = False

# # if is_loan:
# #     print('The decision is yes, this is a good loan.')
# # else:
# #     print('The decision is no, you should not loan this money.')


                                         # W07 PREPARATION MATERIAL

# tip = float(input('What is the tip amount? '))

# while tip < 0:
#     print('Sorry, the tip cannot be negative.')
#     tip = float(input('What is the tip amount? '))

# print(f'You have tipped an amount of ${tip:.2f}')



# number = 1

# while number <= 5:
#     print(f'The number is {number}')

#     number = number + 1

# print('Finished with the loop')

# number = 0
# name = ''

# while number < 10:
#     number = int(input('what is the number? '))
#     name = input('What is your name? ')

# print(f'Your name is {name}')


                                           # 07 PREPARE: CHECKPOINT

# number = int(input('Type in a positive number: '))

# while number < 0:
#     print('The number is a negative number, please try again')
#     number = int(input('Type in a positive number: '))

# print(f'The number is: {number}')

# candy = input('Mum, Dad may i have a piece of candy? ').lower().strip()

# while candy != 'yes':
#     candy = input('Mum, Dad may i have a piece of candy? ').lower().strip()

# print('Thanks mom, thanks dad!')

                                            #  W08 PREPARATION MATERIAL
# for i in range(20):
#     print(i)
#     for j in range(20, 23):
#         print(f'-- {j}')

                                            # W08 CHECKPOINT ACTIVITY
                                            # 1

# colors = ["red", "blue", "green", "yellow"]

# for color in colors:
#     print(f'The color is: {color}')

# print()
#                                             # 2

# # for i in range(1, 9):
# #     print(i)
#                                             # 3
# print()
# # for i in range(0, 22, 2):
#     # print(i)



                                          # W09 PREPARATION MATERIAL
# books = []

# books.append('1 Nephi')
# books.append('2 Nephi')
# books.append('Jacob')
# books.append('Enos')

# # WE ITERATE

# print('Your books are: ')

# for book in books:
#     print(book)

# receipts = [23, 45, 3, 21, 22, 33]
# running_total = 0

# for receipt in receipts:
#     running_total += receipt

# print(f'Your total is: {running_total:.2f}')

                                        # 09 PREPARE CHECKPOINT

# friends = []

# name = None

# while name != 'end':
#     name = input('Type the name of a friend: ')

#     if name != 'end':
#         friends.append(name)

# print()
# print('Your friends are:')

# for friend in friends:
#     print(friend)

# def menu():
#     print('Welcome to the Shopping Cart Program!\n')

#     print('Please select from the following 1-5:')
#     print(' 1. Add item\n 2. view cart\n 3. Remove item\n 4. Compute total\n 5. Quit')

# shopping_list = []
# cart = input()
# menu()
# option = int(input('Pick a menu option 1-5: '))

# while option != 5:
#     if option == 1:
#         cart = input('What item would you like to add? ')
#         shopping_list.append(cart)
#         print(f'{cart} has been added to cart\n')


#     elif option == 2:

#         print('The contents in your shopping cart are: ')

#         for i in shopping_list:
#             print(i)

#     menu()
#     option = int(input('Pick a menu option 1-5: '))

# print('Thank you, Goodbye.')



                                 #    WEEK 10 CHECKPOINT ACTIVITY

# items = []
# item = None

# while item != 'quit':
#     item = input('Please enter the items in the shopping list (type quit to finish) ')

#     if item != 'quit':
#         items.append(item)

# print()
# print('The shopping list with indexes is:')
# for i in range(len(items)):
#     item = items[i]
#     print (f' {i}. {item}')

# print()
# index = int(input('Which item would you like to change? '))
# new_item = input('What item would you love to add? ')

# items[index] = new_item

# print()
# print('The shopping list with indexes is:')

# for i in range(len(items)):
#     item = items[i]
#     print (f' {i}. {item}')

# people = [
#     'Stephanie 36',
#     'John 29',
#     'Emily 24',
#     'Gretchen 54',
#     'Noah 12',
#     'Penelope 32',
#     'Micheal 2',
#     'Jacob 10']

# youngest_age = 9999
# youngest_name = ''

# for person in people:
#     parts = person.split()

#     name = parts[0]
#     age = int(parts[1])

#     if age < youngest_age:
#         youngest_age = age

#         youngest_name = name

# print(f'The youngest in the list is: Name: {youngest_name}, Age: {youngest_age}')

                         # Week 13 Checkpoint Activity
                        #  purpose is to write function

def display_regular(sentence):
    regular = sentence
    return regular

def display_uppercase(sentence):
    uppercase = sentence.upper()
    return uppercase

def display_lowercase(sentence):
    lowercase = sentence.lower()
    return lowercase

first_sentence = input('What is your message? ')

first_sentence_regular = display_regular(first_sentence)
first_sentence_upper = display_uppercase(first_sentence)
first_sentence_lower = display_lowercase(first_sentence)

print(first_sentence_regular)
print(first_sentence_upper)
print(first_sentence_lower)

                    #    OH OR

def display_regular(message):
    print(message)

def display_uppercase(message):
    new_message = message.upper()
    print(new_message)

def display_lowercase(message):
    new_message = message.lower()
    print(new_message)

user_message = input('What is the message? ')

display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)