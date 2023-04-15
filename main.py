from flask import Flask , request
app = Flask(__name__)
@app.route("/")
def hel():
    data = request.args.get('x')
    return "you entered = {}".format(data)
@app.route("/bold")
def bold():
    return "clear"
if __name__ == "__main__":
    app.run(debug=True)