from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

@app.route('/')
def home():
    heading = '<h1>Guess a number between 0 and 9</h1>'
    return heading + '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'

@app.route('/<int:number>')
def guess(number):
    text = ''
    if number > random_number:
        text = '<h1 style="color: purple">Too high, try again!</h1>'
    elif number < random_number:
        text = '<h1 style="color: red">Too low, try again!</h1>'
    else:
        text = '<h1 style="color: green">You found me!</h1><br /><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'
    return text

if __name__ == '__main__':
    app.run(debug=True)