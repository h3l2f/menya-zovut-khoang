from flask import *

app = Flask(__name__)

@app.route("/spike9.9.9-<num>.js")
def spike(num):
    resp = requests.get(f"https://scamff.pythonanywhere.com/spike9.9.9-{num}.js")
    return resp.text

@app.route('/add')
def add():
    name = request.args.get("n")
    resp = requests.get(f"https://scamff.pythonanywhere.com/add?n={name}")
    return f"code: {resp.text}"

if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run()
