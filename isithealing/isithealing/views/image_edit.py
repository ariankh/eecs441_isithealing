from isithealing import *
from PIL import Image
from resizeimage import resizeimage


@app.route("/image_edit", methods=['POST', 'GET'])
def image_edit():
	if request.method == 'POST':
		newfile = request.files['newfile']


		filename = 'most_recent.png'

		newfile.save((app.config['UPLOAD_FOLDER']+filename))

	return render_template("image_edit.html")