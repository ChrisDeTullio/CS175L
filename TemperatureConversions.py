def main():
    controlLoop()

def convertToKelvin(temp_fahrenheit):
    kelvin = (temp_fahrenheit - 32) * 5/9 + 273.15
    return kelvin 

def convertToCentigrade(fahrenheit):
    centigrade = (fahrenheit - 32) * 5/9
    return centigrade

def doConversion(fahrenheit):
    kelvin = convertToKelvin(fahrenheit)
    centigrade = convertToCentigrade(fahrenheit)
    print(f'Fahrenheit: {fahrenheit:.2f} Kelvin: {kelvin:.2f} Centigrade: {centigrade:.2f}')

def repeat():
    num_inputs=int(input("How many conversions would you like to do this time? "))
    for x in range(num_inputs):
        fahrenheit = getFahrenheit()
        doConversion(fahrenheit)

def controlLoop():
    conversions = input("Do you want to do some conversions(Yes or No)? ")
    if conversions == "Yes":
        repeat()
    else:
        return None

def getFahrenheit():
    while True:
        fahrenheit=float(input("Enter Fahrenheit temperature (must be -50 to 130): "))
        if -50 <= fahrenheit <= 130:
            return fahrenheit
        else:
            print("Please re-enter")
            getFahrenheit()
        
if __name__ == '__main__':
    main()
