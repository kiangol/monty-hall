from flask import Flask, render_template, request
import random
import uuid


app = Flask(__name__)
game_states = {}  # Map game ID to winner door


@app.route('/')
def root():
    return """<h1>Welcome to the <b>magic door</b> game!</h1>
    <a href='/select'>Launch game</a>
    """
 

@app.route('/select')
def new():
    game_id = str(uuid.uuid4())
    winning = random.randint(1, 3)
    game_states[game_id] = winning

    return render_template('select.html', game_id=game_id)


@app.route('/reselect', methods=['POST'])
def reselect():

    # request selected door parameter
    selected = int(request.form['door'])

    # request game id
    game_id = request.args.get("game_id")
    winning = game_states[game_id]

    # open a random door that is not the winning or selected door
    opened = set([1, 2, 3])
    opened.discard(winning)
    opened.discard(selected)
    opened = random.choice(list(opened))

    return render_template('reselect.html', game_id=game_id, selected=selected)


if __name__ == '__main__':
    app.run(debug=True)
