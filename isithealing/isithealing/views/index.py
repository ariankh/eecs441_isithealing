from isithealing import *

@app.route("/", methods=['POST', 'GET'])
def index():
	return render_template("index.html")
