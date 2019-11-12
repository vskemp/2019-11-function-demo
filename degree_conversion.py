# Celsius to Fahrenheit
# Prompt the user for a number in degrees Celsius,
# and convert the value to degrees in Fahrenheit
# display it to the user. Example session:

# $ python degree_conversion.py
# Temperature in C? 28
# 82.4 F
# $ python degree_conversion.py
# Temperature in C? -5
# 23 F
# Hint: the formula to convert degrees C to 
# degrees F is: F = C x 1.8 + 32.

Celsius = int(input("Temperature in C?: "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print ("Temperature:", Fahrenheit, "F")