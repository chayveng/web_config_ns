from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the root endpoint


@app.route('/', methods=['GET'])
def home():
    return render_template('template/index.html')

# Define a route for another endpoint


@app.route('/greeting', methods=['GET'])
def greetig():
    return 'Hello, World! This is your Flask API.'


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='10.8.8.16', port=6006)
