import fileinfo
import os
import sys
import json
import requests

rootdir = '/Users/satan/Music/iTunes/iTunes Media/Music/'
API = 'https://itunesartwork.dodoapps.io/?query={}&entity=album&country=us'
output_folder = 'output/'

def download_file(album):
    url_download = album['url']
    local_filename = album['title']+'.jpg'
    local_filename = output_folder+local_filename.replace('/','_')
    print local_filename

    r = requests.get(url_download, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return local_filename

def get_album_details(album_name):
    url = API.format(album_name)
    r = requests.get(url)
    album_details = r.json()
    for album in album_details:
        download_file(album)

for root, subdirs, files in os.walk(rootdir):
    for sub in subdirs:
        for info in fileinfo.listDirectory(root + '/' + sub, [".mp3"]):
            print "\n".join(["%s=%s" % (k, v) for k, v in info.items()])
            for k,v in info.items():
                if k == 'album':
                    get_album_details(v)
