import time
import sys


def animate():
    time.sleep(.5)
    print(".", end=' ')
    time.sleep(.5)
    print(".", end=" ")
    time.sleep(.5)
    print("."
          "", "\n")
    print(""


          "")


animate()

# message
greetings_message_1 = "Hello there! ; )"
greetings_message_2 = """I am a calculator, I can convert... \


                                | Fahrenheit --> Celsius |"""
to_continue = " PRESS 'RETURN' TO CONTINUE"
message = "*** Heat Index Calculator ***" \
          ""


################################################################
def main():
    Location = []
    temperature = []
    humidity = []
    heat_index = []
    print(greetings_message_1, "\n")
    time.sleep(1)
    print(greetings_message_2, end=" ")
    print(""
          ""

          "")
    time.sleep(1)
    print("""

            """)
    num_location = int(input("How Many locations would you like?: "))
    if num_location <= 0:
        print("Error!")
        exit(-1)
        # if num_Location >= 1:
        #     L = input(""
        #
        #                "Location Name: ", {[x-x]- num_location})
        #     if L > 1:
        #         print(f"Location: ", {num_location + 1 == x}, ": ")

    precision = int(input("Enter the precise decimal [0--4] *3 is reccomended* "))
    if precision < 1 or precision > 4:
        print("Uh-oh, numbers ONLY 0-4!")
        exit(-1)
    for x in range(num_location):

        L = input("Location Name: ")
        if num_location > 1:  # Location
            print("Location ", end=f"{x + 1} ")
        T = float(input("Enter the air temperature: "))
        R = float(input("What is the Humidity level [in a percentage]: "))
        HI = -42.379 + 2.04901523 * T + 10.14333127 * R - 0.22475541 * T * R - 0.00683783 * T * T - 0.05481717 * R * R \
             + 0.00122874 * T * T * R + 0.00085282 * T * R * R - 0.00000199 * T * T * R * R
        animate()
        time.sleep(.50)
        print("The Heat index is:", round(HI, precision))
        temperature.append(T)
        humidity.append(HI)
        Location.append(L)
        heat_index.append(HI)
        animate()
        time.sleep(.50)
        print("The lowest heat index is: ", end="")
        print(min(heat_index))
    averaged_temperature = T + T // num_location
    average_HI = HI + HI // num_location  # need to move this out of for loop
    print("The Average HI is:", average_HI, "Deg F")


main()