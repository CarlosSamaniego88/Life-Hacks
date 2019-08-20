import webbrowser
import urllib.request
import urllib.parse
import re
import os

smashstudios = 'UCDXfUTp1PSnA-73a0jKn4bg'
most_valuable_gaming = 'UC_dkX2_MJZeiYZImFN8AOvg'
VGBootCamp = 'UCj1J3QuIftjOq9iv_rr7Egw'
CLASH_Tournaments = 'UC5WNBHwgluAwWJE5QV-5_TA'
TwoGGaming = 'UClIuCiBN-UIsTZb0WlhRo0Q'
Beyond_the_summit_smash = 'UCKJi-4lbB3EwpLpC82OWFjA'


def main():
    query_string = urllib.parse.urlencode({"search_query" : input()})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0])

def smash_comp():
    apikey = os.environ['API_KEY']
    channel_ids = ['']

if __name__ == '__main__':
    main() 

echo "export API_KEY='AIzaSyAekUl_Jlf-JRbs-3VhvACMF_j9-z8oz8Q'" > smash.env