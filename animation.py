import time

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

greetings_message_1 = "Hello there! ; )"
greetings_message_2 = "I am a calculator which converts | Fahrenheit --> Celsius |"
to_continue = " PRESS 'RETURN' TO CONTINUE"
message = "*** Heat Index Calculator ***" \
          ""

#instruction q's
question_1 = "Please Enter A Number ***ANYWHERE BETWEEN 1-200***"

ai_responses = ['Hello there! ;)', 'PRESS *RETURN* TO CONTINUE', 'I am a calculator which converts | Fahrenheit --> Celsius |', '           *** Heat Index Calculator ***']

ai_questions = ['How many locations?: ', 'Decimal precision for calculations [1--4]: ',
                'Enter name of Location(s): ']

def saysomething():
    print(ai_responses[0])
    time.sleep(1)
    input(ai_responses[1])
    time.sleep(1.5)
    print(ai_responses[2], end="\n")
    time.sleep(1)
    print("\n", "\n", ai_responses[3], end=" ")
    time.sleep(2.5)
    return

saysomething()


    f_c = ['Enter air temperature [in deg F]', 'Enter relative humidity [in percentage]']


def asksquestions():
    print(""
          "", "\n")
    int(input(ai_questions[0]))
    int(input(ai_questions[1]))
    int(input(ai_questions[2]))

asksquestions()

