from app import app
from random import randint
def generateQuestion():
    num1 = randint(1,10)
    num2 = randint(1,10)
    operations = ["+", "-", "*", "/"]
    operation = operations[randint(1,3)]
    if operation == "/":
        num1 = num1 * num2
    if num2 > num1:
        num1copy = num1
        num1 = num2
        num2 = num1copy
    text = "{0}{1}{2} = ".format(num1, operation, num2)
    answer = 4
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 / num2
    return text,int(answer)

@app.route('/')
@app.route('/index')
def index():
   # text, answer = generateQuestion()
    text, answer = generateQuestion()
    return text  + str(answer)
