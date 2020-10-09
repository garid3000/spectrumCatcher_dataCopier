import sys
import os
import time

start = time.ctime()

if not(len(sys.argv) == 2 or len(sys.argv) == 3):
	print('usage: python3 downloader.py fileList.txt\nor   : python3 downloader.py fileList.txt your/downloading/dir')
	sys.exit()
ddir = '' #downloading directory
if len(sys.argv) == 3:
	fname = sys.argv[-2]
	ddir = sys.argv[-1]
	if not os.path.isdir(ddir):
		print("err: there is no directory named:", ddir)
		sys.exit()

	jsonDir = os.path.join(ddir, "json")
	jpgDir = os.path.join(ddir, "jpg")
	bmpDir = os.path.join(ddir, "bmp")
	if not os.path.isdir(jsonDir):
		try:
			 os.mkdir(jsonDir)
		except:
			print("error while making following folder:", jsonDir)
	if not os.path.isdir(jpgDir):
		try:
			os.mkdir(jpgDir)
		except:
			print("error while making following folder:", jpgDir)
	if not os.path.isdir(bmpDir):
		try:
			os.mkdir(bmpDir)
		except:
			print("error while making following foler:", bmpDir)

elif len(sys.argv) == 2:
	fname = sys.argv[-1]
file  = open(fname, 'r')
lines = file.readlines()




#this is os dependent
os.system("rm " + os.path.join(ddir, "id.txt"))

for line in lines:
	if   "json" in line:
		os.system('wget http://192.168.11.16:8080/storage/emulated/0/Android/data/com.polarstarspace.veggiecamera/files/' + line[:-1] + " -O " + os.path.join(jsonDir, line[:-1]) )
		# print('wget http://192.168.11.16:8080/storage/emulated/0/Android/data/com.polarstarspace.veggiecamera/files/' + line[:-1] + " -O jsons/" + line[:-1] )
		os.system("echo \"" +  line[:-1] + "\" >> " + os.path.join(ddir, "id.txt"))
	elif "jpg" in line:
		os.system('wget http://192.168.11.16:8080/storage/emulated/0/Android/data/com.polarstarspace.veggiecamera/files/' + line[:-1]  + " -O " + os.path.join(jpgDir, line[:-1]) )
	elif "bmp" in line:
		os.system('wget http://192.168.11.16:8080/storage/emulated/0/Android/data/com.polarstarspace.veggiecamera/files/' + line[:-1]  + " -O " + os.path.join(bmpDir, line[:-1]) )


end = time.ctime()

print(start+ '\n'+ end)
