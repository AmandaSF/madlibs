from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

colors = ['red', 'green', 'blue', 'pink', 'yellow', 'purple', 'brown', 'magenta', 'chartreuse', 'lime']



@app.route('/game')
def show_game_form():
    wanna_play = request.args.get("wannaPlay")
    if wanna_play == "yes":
        return render_template("game.html", colors=colors)
    elif wanna_play == "no":
        return render_template("goodbye.html", wannaPlay=wanna_play)
    else:
        return render_template("cat.html")

@app.route('/madlib')
def show_madlib():
    madlib_args = request.args.items()
    madlib_args = dict(madlib_args)
    return render_template("madlib.html", color=madlib_args["color"], name=madlib_args["name"], adjective=madlib_args["adjective"], noun=madlib_args["noun"])











if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)


