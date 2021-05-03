import  urllib.request

url = "https://avatars.githubusercontent.com/u/42641554?v=4"

urllib.request.urlretrieve(url, "image.png")