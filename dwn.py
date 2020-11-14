from pytube import YouTube
link= input("enter the link")
print("downloading")
YouTube(link).streams.first().download
print("video download succesfull"
      "y")