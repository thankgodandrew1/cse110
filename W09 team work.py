import math

lst = []

number = ''

numbers_sum = 0

print('Type in a list of numbers, input 0 when done\n')

while number != 0:
    number = int(input('Type in the number: '))

    if number != 0:
        lst.append(number)

# SUMMATION OF THE LIST

print()
summation = sum(lst)

print(f'The sum is: {summation}')

# FINDING THE AVERAGE USING THE SUM() FUNCTION TO GET THE sum () OF THE LIST AND len()
# FUNCTION TO GET THE LENGTH OR THE NUMBERS OF ELEMENTS IN THE LIST

def Average(lst):
    return sum(lst) / len(lst)

average = Average(lst)

print(f'The Average of the list is: {average}')

# TO SIMPLY FIND THE  LARGEST NUMBER USING THE max() FUNCTION

max_lst = max(lst)
print(f'The largest number is:', (max_lst))

# TO FIND THE SMALLEST POSITIVE NUMBER USING THE min() FUNCTION

smallest = min([i for i in lst if i > 0])

print('The smallest positive number is: ', (smallest))

# FINDING THE NEW SORTED LIST LED ME TO CREATE A NEW LIST NAME new_lst

sorted_list = sorted(lst)

print('The sorted list is: ')
for number in sorted_list:
    print(number)