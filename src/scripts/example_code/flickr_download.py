import flickrapi
from requests import get
import argparse

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

def flickr_walk(keyward, num):
    #Niek's account
    api_key = 'e1a693f74847710ddb5ce5b7bffa65c5'
    api_secret = '49e146c410be197d'

    flickr = flickrapi.FlickrAPI(api_key,api_secret,cache=True)
    photos = flickr.walk(text=keyward,
                         tag_mode='all',
                         tags=keyward,
                         extras='url_c',
                         sort='relevance',
                         per_page=100)

    count = 0
    for photo in photos:
        if count > int(num)-1:
            break
        try:
            url=photo.get('url_c')
        except Exception as e:
            pass
        if url:
            download(url, str(count)+'.jpg')
            count += 1
    if count < 1:
        print("no results")
    else:
        print("found {} results".format(count))

def main(num):
    flickr_walk("milky way", num)

if __name__=='__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("num", help="The number of requested images")
    args = argparser.parse_args()
    main(args.num)
