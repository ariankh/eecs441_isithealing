from imports import *
app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.config['UPLOAD_FOLDER'] = 'isithealing/static/pictures/'
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'bmp', 'gif', 'png'])
