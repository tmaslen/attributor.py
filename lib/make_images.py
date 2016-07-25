from PIL import Image
import os 

getDimensions = {
	'twitter': {
		'width': 1200,
		'height': 627
	},
	'facebook': {
		'width': 476,
		'height': 248
	}
}

pwd = os.path.dirname(os.path.realpath(__file__))

def createOutput(img, platform, service):

	dimensions = getDimensions[platform]

	attribution = Image.open(pwd + '/../assets/attributions/' + service + '.jpg', 'r')
	attributionBackground = Image.new('RGBA', (dimensions['width'], 32), (223, 17, 0, 255))

	output = Image.new('RGBA', (dimensions['width'], dimensions['height']), (255, 255, 255, 255))
	output.paste(img.resize((dimensions['width'], dimensions['height'])), (0, 0))
	offset = (0, dimensions['height'] - 32)

	output.paste(attributionBackground, offset)
	output.paste(attribution, offset)
	output.save(pwd + '/../output/' + platform + '.jpg')

def makeImages(uploadedFilePwd, service):
	img = Image.open(uploadedFilePwd, 'r')
	createOutput(img, 'twitter', service)
	createOutput(img, 'facebook', service)

if __name__ == "__main__": 
	init()