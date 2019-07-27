from instapy_cli import client
from os import listdir
from os.path import isfile, join

username = "USERNAME"
password = "PASSWORD"
image = "FILE PATH"
text = "Uploaded via python"
mypath = "/Users/Carlos/Projects/Life-Hacks/Insta_scheduler/future_posts"

future_posts = [photo for photo in listdir(mypath) if isfile(join(mypath, photo))]
print(future_posts)

for post in range(len(future_posts)):
    with client(username, password) as cli:
        cli.upload(post, text)
        print("success")