from flask import Flask, current_app

# initialize application
app = Flask(__name__)


# Routes

# GET /
@app.route('/')
def get_index():
    return current_app.send_static_file('./index.html')


# run server
if __name__ == '__main__':
    app.run(debug=True)
