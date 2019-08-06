from instapy_cli import client
import glob
import schedule
import time

def main():
    post()

def post():
    username = "USERNAME"           #insert your username  
    password = "PASSWORD"           #insert your password
    mypath = "/path/directory/imagefolder"     #insert path to folder with photos you want to post

    image_paths = glob.glob(mypath)     #will iterate and store all image paths in folder
    # print(image_paths)
    insta_post_descriptions = ["TBT to Chihuahua when all I just worried about was tortas piolines #TortasPiolines #python",
                                "TBT to spring break with the day one fam #wynwood #python"
                            ]       #associate a description with your photo, check order with print statement in 15 
    
    future_posts = zip(image_paths, insta_post_descriptions)    #creates a dictionary with photo and description
    # print(future_posts)
   
    with client(username, password) as cli:
        for photo, description in future_posts: 
            cli.upload(photo, description)
            break                               #break allows the posting of one photo at a time instea of all in folder
        print("success")

schedule.every().thursday.at("15:00").do(post)  #insert when you want to schedule posts

while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    main() 