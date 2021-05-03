import urllib.request
import urllib.error

try:
    url = urllib.request.urlopen("https://docs.python.org/3/tutorial/datastructures.html")
    content = url.read()
except urllib.error.HTTPError:
    print("HTTP Error")
    exit()

f = open("python.html", "wb")
f.write(content)
f.close()