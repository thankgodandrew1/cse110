""" 
Author Name: ThankGod Andrew 

purpose: Using functions to calculate Wind Chill

"""

# this wind_chill_calculator function has in it the formula for calculating wind chill
def wind_chill_calculator():
    return 35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + (0.4275 * temp * (speed ** 0.16))
    
# This function holds the convertion of celsius temperrature to fahreint
def conversion():
    return temp * (9/5) + 32

temp = float(input('What is the temperature? '))
degrees = input('Fahrenheit or Celcius (F/C)? ').lower()


for speed in range(5, 65, 5):

    if degrees == 'f':
        wind_chill = wind_chill_calculator()

        print(f'At temperature {temp}F, and wind speed {speed} mph, the windchill is {wind_chill:.2f}F')

    elif degrees == 'c':
        convert = conversion()
        the_wind_chill = 35.74 + (0.6215 * convert) - (35.75 * (speed ** 0.16)) + (0.4275 * convert * (speed ** 0.16))
        
        print(f'At temperature {convert}F, and wind speed {speed} mph, the windchill is {the_wind_chill:.2f}F')


# I think i am able to meet requirements i have been able to solve every problem present in this prove assingnment