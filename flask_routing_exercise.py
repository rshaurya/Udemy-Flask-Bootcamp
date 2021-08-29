# Set up your imports here!
# import ...
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return "<h1> Welcome! Got to /pupyy_latin/name to see your name in puppy latin!"
    # Welcome Page
    # Create a generic welcome page.

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    
    return "<h1> Your Puppy latin name is {}".format(pupname)


if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
    pass
