'''
Inches / Centimeters/ Meters

1 inch = 2.54 centimeters

To convert to centimeters from inches
we multiply the number of inches by 2.54.

To convert from centimeters to meters we
divide the number of centimeters by 100.

12 * 2.54 / 100 = 0.3048 meters

To convert from meters back to centimeters we
multiply the number of meters by 100.

0.3048 * 100 = 30.48

To convert from centimeters back to inches we
divide by 2.54.

30.48 / 2.54 = 12.0

'''


'''
Miles / Kilometers

1 mile is roughly equivalent to 1.609 kilometers.

To convert 26 miles to kilometers we multiply
26 by 1.609.

26 * 1.609 = 41.834
'''

'''
Farenheit / Celsius

F = 98.6
C = (F * 32) * (5 / 9)
'''

'''
Celsius / Farenheit

C = 37
F = C * (9/5) + 32
'''


'''
Unit Converter: Miles and Kilometers
'''
def print_menu():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")

def km_miles():
    km = float(input("Enter number (Kilometers): "))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input("Enter number (Miles): "))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

if __name__ == '__main__':
    print_menu()
    choice = input("Which conversion would you like to make? ")
    if choice == 1:
        km_miles()

    if choice == 2:
        miles_km()
