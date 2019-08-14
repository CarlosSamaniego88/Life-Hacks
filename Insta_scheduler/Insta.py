from instapy_cli import client
import glob
import schedule
import time
import os

#Remember to have a folder of images that all have endings of either JPG, jpeg, or png
#When running this script, run, "nohup python insta.py &", this will allows the script to run in the background

def main():
    post()

def post():
    #in .bash_profile, write, "export username="yourusername", and, "export password="yourpassword""
    username = os.environ['INSTA_USERNAME']          
    password = os.environ['INSTA_PASSWORD']           
    mypath = "directory/*.JPG"     #insert path to folder with photos you want to post
                                   #make sure all images in fill have same ending like JPG, jpeg, png, etc

    image_paths = glob.glob(mypath)     #will iterate and store all image paths in folder
    # print(image_paths)
    insta_post_descriptions = ["TBT to",
                                "TBT to "
                            ]       #associate a description with your photo, check order with print statement in 15 
    
    future_posts = zip(image_paths, insta_post_descriptions)    #creates a dictionary with photo and description
    # print(future_posts)
   
    with client(username, password) as cli:
        for photo, description in future_posts: 
            cli.upload(photo, description)
            break                               #break allows the posting of one photo at a time instead of all in folder
        print("success")

schedule.every().thursday.at("15:00").do(post)  #insert when you want to schedule in military time

while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    main() 

echo "export INSTA_USERNAME='carlossamaniego14'" > instagram.env
echo "export INSTA_PASSWORD='Omoplata#88'" >> instagram.env