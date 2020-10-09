from PIL import Image
import os, sys
import numpy as np

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

povDir = os.path.join(ddir, "jpgPov")
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
	image.save(imgOut[i])
	print(i, imgOut[i])
