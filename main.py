from flask import *
import json
from datetime import date

app = Flask(__name__,template_folder="templates")

@app.route("/spike9.9.9-<num>.js")
def spike(num):
    with open("num.json","r") as f:
        data = json.load(f)
    if num not in list(data.keys()): return "Not found!", 404
    time = int(date.today().strftime(r"%y%m%d"))
    if int(data[num]["date"]) > time: return render_template("nopass.html")
    else: return render_template("withpass.html")

@app.route('/add')
def add():
    with open("num.json","r") as f:
        data = json.load(f)
    with open("num","r") as f:
        num = int(f.read())
    timenow = date.today().strftime(r"%y%m%d")
    name = request.args.get("n")
    if (name == None) or (name == ""): name == "Anonymous"
    data[num] = {}
    data[num]["date"] = int(timenow)+1
    data[num]["name"] = name

    with open("num.json","w") as f:
        json.dump(data,f,indent=4)
    with open("num","w+") as f:
        f.write(str(num+1))
    
    return "ok"

if __name__ == "__main__":
    app.run()