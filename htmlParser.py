import os
from html.parser import HTMLParser

import platform
print(platform.system())
if platform.system() == 'Linux':
    try:
        os.system("rm file.txt")
    except:
        pass
    try:
        os.system("rm fileList.txt")
        print("file deleted")
    except:
        pass
elif platform.system() == "Windows":
	print("not developed for windows yet")
	sys.exit()
else:
	print("could not recognize your OS")
	sys.exit()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass
        #print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        pass
        #print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print(data)
        if ('.json' in data) or ('jpg' in data) or ('bmp' in data):
            if '20201109' in data:
                print("Encountered some data  :", data)
                os.system("echo \"" + data + "\" >> fileList.txt")

parser = MyHTMLParser()

import sys
if len(sys.argv) != 2:
	print("usage: python3 htmlParser.py state.html")
	sys.exit()


fname = sys.argv[-1]
print(fname)
html = open(fname, 'r').read()
parser.feed(html)
