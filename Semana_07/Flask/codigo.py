from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        number = random.randint(1, 20)
        guess = int(request.form['guess'])
        if number == guess:
            result = "Você ganhou!"
        else:
            result = "Você perdeu!"
        return render_template('index.html', game_result=result)
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', page_name=request.path), 404

if __name__ == '__main__':
    app.run(debug=True)
