import time

def animate():
    time.sleep(.5)
    print(".", end=' ')
    time.sleep(.5)
    print(".", end=" ")
    time.sleep(.5)
    print(".", end=" ")

animate()



#intro message
greetings_message_1 = "\nHello there! ;)"
greetings_message_2 = "I am a calculator which converts | Fahrenheit --> Celsius |"
to_continue = "PRESS 'RETURN' TO CONTINUE"
message = "*** Heat Index Calculator ***"

#instruction q's
question_1 = "Please Enter A Number ***ANYWHERE BETWEEN 1-200***"

ai_response = ['\nHello there! ;)',
               'I am a calculator which converts | Fahrenheit --> Celsius |',
               'PRESS *RETURN* TO CONTINUE', 'message = "*** Heat Index Calculator ***"']


print(*ai_response, sep=" ")

