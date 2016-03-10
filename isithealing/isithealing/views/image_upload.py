from isithealing import *

@app.route("/image_upload", methods=['POST', 'GET'])
def image_upload():
	return render_template("image_upload.html")