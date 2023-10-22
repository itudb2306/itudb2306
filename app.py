from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_page():
    return "<h1>Database Project's Homepage</h1>"

@app.route("/test")
def test_page():
    return "<h1>Test Page</h1>"

if __name__ == "__main__":
    app.run() # Run the app server on localhost:5000
