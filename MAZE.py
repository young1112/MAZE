P = '\x1b[1;97'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nNO INTERNET CONNECTION\n'%(M))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "Nigeria" == fc:
		__import__("MAZE").login()
		__import__("MAZE64").login()
	print("UNKNOWN SYSTEM ")
		
