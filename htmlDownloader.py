import requests
import sys

print(sys.argv)

if len(sys.argv) != 2:
	print("error ip address is unclear\nusage: python3 htmlDownloader.py 192.168.xx.xx")
	sys.exit()

ipaddress = sys.argv[-1]
url = 'http://' + ipaddress + ':8080/storage/emulated/0/Android/data/com.polarstarspace.veggiecamera/files'
r = requests.get(url, allow_redirects=True)

open('state.html', 'wb').write(r.content)
