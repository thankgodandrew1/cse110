# Purpose: Calculate the speed of a falling object using the formula:

# i am using \n to create a blank space

# v(t) = sqrt(mg/c) * (1-exp ((- sqrt(mgc)/ m)t))

# import math

# print('\nwelcome to the velocity calculator. please enter the following:\n')

# m = float(input('Mass (in Kg): '))
# g = float(input('in m/s^2, 9.8 for Earth, 24 for Jupiter: '))
# t = float(input('Time (in seconds): '))
# p = float(input('Density of the (in Kg/m^3, 1.3 for air, 1000 for water): '))
# A = float(input('Cross sectional area (in m^2): '))
# C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

# First Calculate c = 1 / 2 p A C
# c = (1 / 2) * p * A * C

# Now calculate the velocity v(t) = sqrt(mg / c) * (1 - exp((-sqrt(mgc)/m)*t))
# v = math.sqrt (m * g / c) * (1 - math.exp ((- math.sqrt(m * g * c) / m) * t))

# print(f'\nThe inner value of c is: {c:.3f}' )
# print(f'The velocity after 10.0 seconds is: {v:.3f} m/s ')

# stretch challege
# Determine the velocity of a different object: find the cross sectional area of a bowling ball

#                              05 TEACH: TEAM ACTIVITY
#                                 GRADE CALCULATOR


# grade = float(input('What is your grade percent? '))
# if grade >= 90:
#     letter = 'A'
# elif grade >= 80:
#     letter = 'B'
# elif grade >= 70:
#     letter = 'C'
# elif grade >= 60:
#     letter = 'D'
# elif grade <= 60:
#     letter = 'F'

#                                 # STRETCH CHALLANGE 1
# sign = ''
# last_digit = grade % 10
# if last_digit >= 7:
#     sign = '+'
# elif last_digit < 3:
#     sign = '-'
# else:
#     sign = ''

#                                  # STRETCH CHALLENGE 2
# if grade  >= 93:
#     sign = ''


#                                  # STRETCH CHALLENGE 3

# if letter == 'F':
#     sign = ''
# print(f'Your letter grade is: {letter}{sign}')
# if grade >= 70:
#     print('Congratulation!! You succeded in this course')
# else:
#     print('Your grade is below average, try to put more effort next time!')


                          # W06 TEAM ACTIVITY - AMUSEMENT PARK RIDES

# age = int(input('What is the age of the  first rider? '))
# height = int(input('What is the height of the first rider? '))
# is_second_rider = input('Is there a second rider yes/no? ')

# can_ride = False

# # if is_second_rider.lower() == 'no':
#     # can_ride = False

# if is_second_rider.lower() == 'yes':
#     second_age = input('What is the age of the second rider? ')
#     second_height = float(input('What is the height of the second rider? '))

#     if height < 36 or second_height < 36:
#         can_ride = False
#     else:
#             if age >= 18 or second_age >= 18:
#                 can_ride = True
#             else:
#                 can_ride = False
# else:
#     if age >= 18 and height >= 62:
#             can_ride = True
#     else:
#             can_ride = False

# if can_ride:
#     print('Welcome to the ride, please be safe and have fun!')
# else:
#     print('Sorry, you may not ride')

        # STRETCH CHALLENGE III THERE IS APROBLEM IN THIS CODE I WILL RETURN TO FIX IT IF I HAVE ENOUGH TIME!

# can_ride = False

# age1 = int(input('What is the age of the first rider? '))
# height1 = int(input('What is the height of the first reader? '))

# if age1 >= 12 and age1 < 18:
#     golden1 = input('Does this rider have a golden passport (yes/no)? ')

# is_second_rider = input('Is there a second rider yes/no? ')
# if is_second_rider.lower() == 'yes':
#     age2 = input('What is the age of the second rider? ')
#     height2 = input('What is the height of the second rider? ')
#     if age2 >= 12 and age2 < 18:
#         golden2 = input('Does this rider have a golden passport (yes/no)? ')

#         # Rule 1
#         if height1 < 36 and  height2 < 36:
#             can_ride = False
#         else:
#             # Rule 3
#             if age1 >= 12 and height1 >= 52 and age2 >= 12 and height2 >= 52:
#                 can_ride = True
#             elif(age1 >= 16 and age2 >= 14) or (age1 >= 14 and age2 >= 16):
                # Rule 6
                # can_ride = True
            # else:
#                 can_ride = False
# else: # There is only one rider
#     # Rule 2
#     if (age1 >= 18 or golden1.lower() == 'yes') and height1 >= 62:
#         can_ride = True
#     else:
#         can_ride = False

# if can_ride:
#     print('Welcome to the ride, please be safe and have fun!')
# else:
#     print('Sorry, you may not ride')

                                             # W07 TEAM ACTIVITY I


# num = int(input('What is the magic nunber? '))
# guess  = int(input('Guess the magic number: '))


# if guess > num:
#     print('Lower')
#     guess = int(input('Guess the magic number: '))

# elif guess < num:
#     print('Higher')
#     guess = int(input('Guess the magic number: '))

# print('You guessed right')

                                       # W07 TEAM ACTIVITY II

# import random

# magic_num = random.randint(1, 100)

# i need to start the variable 'guess' at something, but i dont want to start it as a valid number
# that the computer have chosen, so i will start with a -1
# guess = -1

# keep going as long as the guess doesn't match the magic number

# while guess != magic_num:
#     guess = int(input('What is your guess? '))

#     if guess < magic_num:
#         print('Higher')
#     elif guess > magic_num:
#         print('Lower')
#     else:
#         print('You guessed right!')


                              #   W07 TEAM ACTIVITY STRETCH CHALLENGE!!!

# import random

# keep_playing = 'yes'

# # AS LONG AS YES IS INPUTTED THE GAME WILL CONTINUE TO PLAY
# while keep_playing.lower() == 'yes':
#     magic_num = random.randint(1, 100)

# THIS VARIABLE WILL KEEP TRACK OF HOW MANY GUESSES MADE
#     guess_count = 0

#     guess = -1

#     while guess != magic_num:
#         guess = int(input('What is your guess? '))
#         guess_count = guess_count + 1

#         if guess < magic_num:
#             print('Higher')
#         elif guess > magic_num:
#              print('Lower')
#         else:
#              print('You guessed right!')

# AT THIS POINT THEY HAVE GUESSED IT CORRECTLY
#     print(f'it took you {guess_count} guesses')

#     keep_playing = input('Would you like to play again (yes/no)? ')

# print('Thank you for playing!')


                                #   WEEK 08 TEAM ACTIVITY CORE + STRETCH CHALLENGE

# I import math to use it later in the program
# import math

# choice = int(input('How many numbers and rows do you need in your multiplication table? '))

# user_choice = choice + 1

# just to make things clear log(100) = 2.00 + 1 = 3.00 when converted to a whole num or integer it will be = 3
# anything less than log(100) = 1.-- + 1 which will result to 2.-- we need to multiply users 'choice'  * 'choice'
# so that if it's result is >= 100 the multiplication format will be 3 spacing but if it is less than 100
# it's formatting will be 2 spaces, so i first created a variable that stores the users choice when it multiplies itself (choice * choice)
# and also a variable (format) to convert log to integer and add a + 1 value to justify the above description
# which is to achieve either the 2 spacing format or the 3 spacing format.
# if users choice is <= 9 the format will be 2 spaces else, it would be 3 spaces. why? 9*9 is less than 100

# decision_num = choice * choice

# format = int(math.log10(decision_num)) + 1

# # REPEAT THIS LINE 5 TIMES:
# for row_number in range (1, user_choice):
#     for col_num in range (1, user_choice):
#         number = row_number * col_num
#         print(f'{number:{format}}', end= ' ')
#     print()

                               #  09 TEAM ACTIVITY CORE + STRETCH


# import math

# lst = []

# number = 0

# numbers_sum = 0

# print('Type in a list of numbers, input 0 when done\n')

# while number != 0:
#     number = int(input('Type in the number: '))

#     if number != 0:
#         lst.append(number)

# # SUMMATION OF THE LIST

# print()
# summation = sum(lst)

# print(f'The sum is: {summation}')

# # FINDING THE AVERAGE USING THE SUM() FUNCTION TO GET THE sum () OF THE LIST AND len()
# # FUNCTION TO GET THE LENGTH OR THE NUMBERS OF ELEMENTS IN THE LIST

# def Average(lst):
#     return sum(lst) / len(lst)

# average = Average(lst)

# print(f'The Average of the list is: {average}')

# # TO SIMPLY FIND THE  LARGEST NUMBER USING THE max() FUNCTION

# max_lst = max(lst)
# print(f'The largest number is:', (max_lst))

# # TO FIND THE SMALLEST POSITIVE NUMBER USING THE min() FUNCTION

# smallest = min([i for i in lst if i > 0])

# print('The smallest positive number is: ', (smallest))

# # FINDING THE NEW SORTED LIST LED ME TO CREATE A NEW LIST NAME new_lst

# sorted_list = sorted(lst)

# print('The sorted list is: ')
# for number in sorted_list:
#     print(number)

                                        #   WEEK 10 TEAM ACTIVITY CORE + STRETCH
# accounts = []
# balances = []

# account = ''

# while account != 'quit':
#     account = input('What is the name of the bank accounts (type quit when done) ')
    
#     if account != 'quit':
#         balance = float(input('What is your current balance? '))
    
#         accounts.append(account)
#         balances.append(balance)

# total = 0

# print()
# print('Account information:')

# for i in range (len(accounts)):
    
#     print(f'{i}. {accounts[i]} - ${balances[i]:.2f}')

# # Total calculation

# total = sum(balances)

# # Average calculation

# average = total / len(balances)

# print()
# print(f'Total: ${total}')
# print(f'Average: ${average:.2f}')

# account_name = ''
# highest_balance = 0

# for i in range (len(accounts)):
#     account = accounts[i]
#     balance = balances[i]
    
#     if balance > highest_balance:
#         highest_balance = balance
#         account_name = account
# print(f'The highest balance is: {account_name} - ${highest_balance}')

# account_update = 'yes'

# while account_update == 'yes':
#     account_update = input('Do you want to update an account? ')

#     if account_update == 'yes':
#         index = int(input('What is the index of the account you want to update? '))
#         new_amount = float(input('What is the new amount? '))
        
#         balances[index] = new_amount

#         print()
#     print('Account information:')
    

#     for i in range(len(accounts)):
#         account = accounts[i]
#         balance = balances[i]
#         print(f'{i}. {account} - ${balance:.2f}')
    
        
""" 
# Author Name: ThankGod Andrew

# Purpose: practice finding items in a file core requirements
# """

# largest_chap = -1
# largest_book = None
# max_chap = -1
# max_name = None

# with open('books_and_chapters.txt') as books:
#     for book in books:
#         parts = book.strip().split(':')

#         book_name = parts[0]
#         book_chap = int(parts[1]) 
#         scripture = parts[2]
    
#         print(f'Scripture: {scripture}, Book: {book_name}, Chapter: {book_chap}')
    
#         if book_chap > largest_chap:
          
#             largest_chap = book_chap
#             largest_book = book_name

#     print(f'\nThe highest number of chapters in the list is: {largest_chap} with the scripture name {largest_book}')
              
                 
#                   # STRETCHY STRETCH CHALLENGE

#     books.seek(0)

#     user_scripture = input('Which scripture do you want to learn about? ')

#     with open('books_and_chapjters.txt') as books:
#         for book in books:
#             parts = book.strip().split(':')

#             book_name = parts[0]
#             book_chap = int(parts[1]) 
#             scripture = parts[2]
        
#             if scripture.lower() == user_scripture:
#                 print(f'Scripture: {scripture}, Book: {book_name}, Chapters: {book_chap}')

#                 if book_chap  > max_chap:
#                     max_chap = book_chap
#                     max_name = book_name
    
#         print()
#         print(f'The book in the {user_scripture.title()} with the largest number of chapters is: {max_name} chapter {max_chap}')

                                    #    WEEK 13 TEAM ACTIVITY CORE + STRETCH

import math

def compute_area_square(side):
        area = compute_area_rectangle(side, side)
        return area

def compute_area_rectangle(length, width):
        return length * width

def compute_area_circle(radius):
        area = math.pi * (radius ** 2)
        return area

def compute_area (shape, value1, value2 = 0):
        area = -1
        if shape == 'square':
                area = compute_area_square(value1)
        elif shape == 'rectangle':
                area = compute_area_rectangle(value1,value2)
        elif shape == 'circle':
                area = compute_area_circle(value1)

        return area


shape = None

while shape != 'quit':
        shape = input('What shape do you have? ').lower()

        if shape == 'square':
                side = float(input('What is the length of the sides of the square? '))
                area_square = compute_area(shape, side)
                print(f'The area of the square is {area_square}')

        elif shape == 'rectangle':
                length = float(input('What is the length? '))
                width = float(input('What is the width '))
                area_rectangle = compute_area(shape, length, width)
                print(f'The area of the rectangle is {area_rectangle}')

        elif shape == 'circle':
                radius = float(input('What is the side of the radius? '))
                area_circle = compute_area(shape, radius)
                print(f'The area of the circle is {area_circle:.2f}')

