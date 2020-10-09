import os, sys
import numpy as np
from PIL import Image, ImageDraw


ddir = ''
if len(sys.argv) == 2:
	ddir = sys.argv[-1]
else:
	print("err: python3 imgPOVcreator.py")


def cropper(orig_1920_1080):
	t = np.flip(np.asarray(orig_1920_1080),axis=0)
	return t[400:1400, :,:]
#        img = cropper(mpimg.imread(_ph_img_jpgs_[index]))
#        img1920 = np.flip(np.asarray(Image.open("20201006_000133.jpg"), dtype=np.int16),axis=0)

povDir = os.path.join(ddir, "jpgPov_ybox")
jpgDir = os.path.join(ddir, "jpg")
idsfna = os.path.join(ddir, "id.txt")
ids = open(idsfna, "r").readlines()
ids = [z.split(".")[0].split("e_")[1] for z in ids]
imgDir = [os.path.join(jpgDir, "VeggieCamera_crops_picture_" + z + ".jpg") for z in ids]
imgOut = [os.path.join(povDir, "VeggieCamera_crops_picture_" + z + ".jpg") for z in ids]
print(ids, imgDir)
if not os.path.isdir(povDir):
	try:
		os.mkdir(povDir)
	except:
		print("error while making folder:", povDir)
		sys.exit()


for i in range(len(ids)):
	a = cropper(Image.open(imgDir[i]))
	image = Image.fromarray(a)
	draw = ImageDraw.Draw(image)
	draw.rectangle((490, 500, 490+50, 500+170), outline=(255, 255, 0), width=3)
	draw.rectangle((390, 500, 390+50, 500+170), outline=(255, 255, 0), width=3)
	draw.rectangle((180, 500, 180+50, 500+170), outline=(255, 255, 0), width=3)
	draw.rectangle((0, 585, 1000, 585), outline=(0, 255, 0), width=3)
	image.save(imgOut[i])
	print(i, imgOut[i])
