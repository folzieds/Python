#
# @author Osu Adefolarin
#

# A basic calculator
import re
import logging

logging.basicConfig(filename='cal.log', level=logging.DEBUG)


print("Basic Calculator!!")
print("Type 'quit' to exit\n")

previous = 0
run = True

def calculate():
    global previous
    global run

    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    if equation == "quit":
        run = False
    else:
        try:
            equation = re.sub('[a-zA-Z().,{};:" "]','',equation)
            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(f"{previous} {equation}")
        except Exception as error:
            print("You have entered an invalid value")
            logging.ERROR(error)



while run:
    calculate()

# TODO: add try except block as to handle errors
# TODO: add test to show TDD
