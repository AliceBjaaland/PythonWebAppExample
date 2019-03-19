from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hell) World"


@app.route("/signup", methods=["POST"])
def sign_up():
    if request.method == 'POST':
        form_data = request.form
        print (form_data["email"])
        return ("All Ok")
    else:
      return render_template('hello.html')

app.run(port=5000)
app.run(debug=True)
# https://stackoverflow.com/questions/51700053/flask-werkzeug-exceptions-badrequestkeyerror
