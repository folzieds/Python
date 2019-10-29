#
# @author Osu Adefolarin
#

# A basic calculator
import re


print("Basic Calculator!!")
print("Type 'quit' to exit\n")

previous = 0
run = True

def calculate():
    global previous
    global run
    equation = ''

    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z().,{};:" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(f"{previous} {equation}")


while run:
    calculate()

# TODO: add try except block as to handle errors
# TODO: add test to show TDD
