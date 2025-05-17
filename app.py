from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>FitStream Life</title>
        </head>
        <body>
            <h1>Welcome to FitStream Life</h1>
            <p>Your journey to fitness begins here!</p>
        </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
