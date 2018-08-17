# coding: utf-8

import requests, uuid, time
from requests.compat import urljoin
from bs4 import BeautifulSoup


url = '' # Target URL
images = [] # Array of image list | 画像リストの配列

def download_images(url):
    soup = BeautifulSoup(requests.get(url).content,'lxml') # Analyze the URL | URL内を解析
    for link in soup.find_all("img"): # Get 'img' tag and store in link | imgタグを取得しlinkに格納
        src_attr = link.get("src") # Get 'src' attribute and store in src_attr | srcを取得してsrc_attrに格納
        if src_attr.endswith(".jpg"): # Get '.jpg' | imgタグ内の.jpgであるsrcを取得
            sr = requests.compat.urljoin(url, src_attr) # Convert relative URL to absolute URL | 相対URLから絶対URLに変換
            images.append(sr) # Array of 'images' list | imagesリストに格納


def main():
    for target in images: # Insert from target to mages | imagesからtargetに入れる
        time.sleep(5.0) # Interval | 何秒間隔をおくか指定
        re = requests.get(target) # Array of target
        with open('img/' + str(uuid.uuid4()) + target.split('/')[-1], 'wb') as f: # Insert in img folder |imgフォルダに格納
            f.write(re.content) # Save image date  |.contentにて画像データとして書き込む

download_images(url) # Run
main() # Run
print("ok") # Check |確認
