import os
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from lib import make_images
from lib import upload_helper

app = Flask(__name__)

def getPwd():
	return os.path.dirname(os.path.realpath(__file__))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/make_images", methods=['POST', 'GET'])
def makeImages():
	if request.method == 'POST':
		upload_helper.init(request.files['file'])
		upload_helper.saveFile(upload_helper.uploadedFilePwd())
		make_images.makeImages(upload_helper.uploadedFilePwd(), request.form['service'])
		upload_helper.zipOutput()
		return send_file(upload_helper.zipOutputPwd())
	else:
		return 'error'

if __name__ == "__main__":
    app.run()