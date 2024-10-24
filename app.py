from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the app on the local development server
    app.run(debug=True)
