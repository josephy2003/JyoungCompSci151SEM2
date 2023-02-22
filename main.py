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


def pause():
    time.sleep(1)

pause()


greetings_message_1 = "Hello there! ; )"
greetings_message_2 = """I am a calculator, I can convert ' \
                         
                                
                                | Fahrenheit --> Celsius |"""
to_continue = " PRESS 'RETURN' TO CONTINUE"
message = "*** Heat Index Calculator ***" \
          ""

# instruction q's
question_1 = "Please Enter A Number ***ANYWHERE BETWEEN 1-200***"
#                     0                     1
ai_responses = ['Hello there! ;)','PRESS *RETURN* TO CONTINUE'
    ,
#                                2                             3
                '\n'
                'I am a calculator which converts | Fahrenheit --> Celsius |',
#                                         4
                '           *** Heat Index Calculator ***']

#                                0
ai_questions = ["""Insert 3 different location names.



Name Of Location(1) """, 'Name Of Location(2) ', 'Name Of Location(3) ', 'Decimal precision for calculations [1--4]: ']
#                                 2                        3                                   4

#          1


def saysomething():
    print(ai_responses[0])
    time.sleep(1)
    input(ai_responses[1])
    time.sleep(1.5)
    print(ai_responses[2], end="\n")
    time.sleep(1)
    print("\n", "\n", ai_responses[3], end=" ")
    time.sleep(2.5)



saysomething()

f_c = ['Enter air temperature [in deg F]', 'Enter relative humidity [in percentage]']

user_input = input()

def asksquestions():
    print(""
          "")
    input("""Insert 3 different location names. \n
    Name Of Location(1) """)
    input("""Name Of Location(2) """)
    input(ai_questions[2])
    input(ai_questions[3])





def prompt():
    print("""
    
        """),
    LN = input("How Many Loctions Do You want?")
    if LN > 0
        print("Location", {LN})
    L = input(ai_questions[0])
    pause()
    LM = (input(ai_questions[1])),
    pause()
    dec_precison = int(input(ai_questions[2])),
    pause()
    x = round(5.76543, 4),
    T = float(input("Please Enter designated °F.")),
    R = float(input("")),
    HI = -42.379 + 2.04901523*T + 10.14333127*R - 0.22475541*T*R- 0.00683783*T*T - 0.05481717*R*R\
     + 0.00122874*T*T*R + 0.00085282*T*R*R - 0.00000199*T*T*R*R
    print(LN)
    print(L)
    print(LM)
    print(T)
    print(HI)

prompt()









