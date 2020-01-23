"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    game_answer = request.args.get("game")
    
    if game_answer == "no":
        return render_template("goodbye.html")
    elif game_answer == "yes":
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():

    color = request.args.get("color")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    building = request.args.get("building")
    place = request.args.get("place")
    animals = request.args.getlist("animals")

    print("\n\n\n\n")
    print(animals) 

    return render_template("madlib.html", color=color, noun=noun, person=person, 
        adjective=adjective, building=building, place=place, animals=animals)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
