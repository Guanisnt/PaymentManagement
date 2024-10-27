from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 假設用列表來記錄電費
records = []

@app.route("/")
def index():
    return render_template("index.html", records=records)

@app.route("/add", methods=["POST"])
def add_record():
    name = request.form["name"]
    amount = request.form["amount"]
    paid = request.form.get("paid", "no") == "yes"
    records.append({"name": name, "amount": amount, "paid": paid})
    return redirect(url_for("index"))

@app.route("/toggle_paid/<int:index>")
def toggle_paid(index):
    records[index]["paid"] = not records[index]["paid"]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5051, debug=True)  # 更改這裡的 port
