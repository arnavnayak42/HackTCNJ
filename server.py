from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is a test for the main page <h1>HELLO<h1>" 

if __name__ == "__main__":
    app.run()