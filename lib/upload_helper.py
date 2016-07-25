import shutil
import os

f = 0

pwd = os.path.dirname(os.path.realpath(__file__))

def init(passedInF):
	global f
	f = passedInF

def zipOutput():
	shutil.make_archive('attributed', 'zip', 'output')

def uploadedFilePwd():
	global f
	global pwd
	return pwd + '/../upload_zone/' + f.filename

def zipOutputPwd():
	return pwd + '/../attributed.zip'

def saveFile(name):
	global f
	f.save(name)