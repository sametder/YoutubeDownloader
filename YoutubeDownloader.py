import pytube 
url = input("Enter video URL: ")

path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)