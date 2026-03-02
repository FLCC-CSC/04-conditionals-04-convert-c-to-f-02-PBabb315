# FILE NAME - convert_C_to_F_02.py

# NAME: Patrick Babb
# DATE: 3/1/2026
# BRIEF DESCRIPTION: a more complex conversion program for F-C/C-F temp conversions



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    temp_conversion()

def temp_conversion():
    
    print('===== Temperature Converter =====')
    print('  1. Convert from Celsius to Fahrenheit')
    print('  2. Convert from Fahrenheit to Celsius')
    choice = int(input('Please choose from the above menu: '))
    if (choice == 1):
        c = float(input('Enter a temperature to convert: '))
        converted = c * 9/5 + 32
        print(f'{c} degrees Celsius is {converted} degrees Fahrenheit.')
    else:
        f = float(input('Enter a temperature to convert: '))
        converted = (f - 32 ) * 5/9
        print(f'{f} degrees Fahrenheit is {converted} degrees Celsius.')
main()
        
    
    









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
that generally speaking if elif else is more tidy for coding as the user can't just type whatever in and get a result tied
to the else code






'''