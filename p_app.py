from flask import Flask, render_template

app = Flask(__name__)

@add.route('/')
def index():
	return render_template("layout.html")

app.run(debug=True, port=8088, host='0.0.0.0')
