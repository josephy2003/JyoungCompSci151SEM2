



def main():
    print("Heat Index calculator")
    num_Location = int(input("How many locations?"))
    if num_Location <= 0:
        print("Error!")
        exit(-1)
def precision():
    int(input("Enter the precise decimal"))




if precision <1 or precision >4:
    print("Error!")
    exit(-1)
    temperatures = []
    humidities = []
    HIs = []
    Locations = []

    for x in range(num_Location):
        location = input(f"Enter a location: {x + 1}")
        temperature = float(input("Enter the air temperature"))
        # we need to get the temp from here
        humidity = float(input("What is the Humidity level [in a percentage]"))
        HI = -42.379 + 2.04901523 * temperature + 10.14333127 * humidity - 0.22475541 * temperature * humidity - 0.00683783 * temperature * \
             temperature - 0.05481717 * humidity * humidity + 0.00122874 * temperature * temperature * humidity + 0.00085282 * temperature * humidity * humidity - 0.00000199 * temperature * temperature * humidity * humidity
        print("The Heat index is:", round(HI, precision))
        print(temperatures.append(temperature))
        print(humidity.append(humidity))
        (HIs.append(HI))
        Locations.append(location)
        print(HIs)
        print(Locations)
        print(location)
        print(temperature)
    print("The lowest heat index is:", end="")
    print(min(HIs))
    average_HI = HI + HI // num_Location
    print("The Average HI is:", average_HI, "Deg F")
    average_temperature = temperature + temperature // num_Location

