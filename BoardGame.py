#Example Flask App for a hexaganal tile game
#Logic is in this python file

from flask import Flask, render_template_string, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# HTML Template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guess the Number</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .game-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        h1 {
            color: #333;
        }

        input[type="number"] {
            padding: 10px;
            width: 50%;
            margin-top: 10px;
            font-size: 16px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-top: 10px;
            cursor: pointer;
        }

        button:hover {
            background-color: #28a745;
            color: white;
        }

        p {
            font-size: 18px;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>Guess the Number Game</h1>
        <p>{{ message }}</p>
        <form action="/" method="POST">
            <input type="number" name="guess" placeholder="Enter your guess" required>
            <button type="submit">Submit Guess</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)  # Generate a random number between 1 and 100
        session['attempts'] = 0  # Initialize attempts counter
    
    if request.method == "POST":
        guess = int(request.form['guess'])
        session['attempts'] += 1

        if guess < session['number']:
            message = "Too low! Try again."
        elif guess > session['number']:
            message = "Too high! Try again."
        else:
            message = f"Correct! You guessed the number in {session['attempts']} attempts."
            session.pop('number')  # Reset the game after the correct guess
            session.pop('attempts')

        return render_template_string(html_template, message=message)

    return render_template_string(html_template, message="Guess the number between 1 and 100!")

if __name__ == "__main__":
    app.run(debug=True)


