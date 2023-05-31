import pytube

url = input("give me video's url: ")
path = ""

pytube.YouTube(url).streams.get_lowest_resolution().download(path)