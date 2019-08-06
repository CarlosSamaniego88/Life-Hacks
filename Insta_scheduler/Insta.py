from instapy_cli import client
import glob
import schedule
import time

def main():
    post()

def post():
    username = "user"
    password = "pass"
    mypath = "/Users/Carlos/Projects/Life-Hacks/Insta_scheduler/future_posts/*.JPG"

    image_paths = glob.glob("/Users/Carlos/Projects/Life-Hacks/Insta_scheduler/future_posts/*.JPG")
    insta_post_descriptions = ["TBT to Chihuahua when all I just worried about was tortas piolines #TortasPiolines #python",
                                "TBT to spring break with the day one fam #wynwood #python"
                            ]
    future_posts = zip(image_paths, insta_post_descriptions)
    print(future_posts)
   
    with client(username, password) as cli:
        cli.upload(future_posts)
        print("success")

    # schedule.every().thursday.at("15:00").do(post)

while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    main() 