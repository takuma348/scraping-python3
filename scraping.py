# coding: utf-8
import requests, uuid, time
from requests.compat import urljoin
from bs4 import BeautifulSoup


url = 'https://www.kikkoman.co.jp/homecook/search/recipe/00003600/index.html'
images = [] # 画像リストの配列

def download_images(url):
    soup = BeautifulSoup(requests.get(url).content,'lxml') # bsでURL内を解析
    for link in soup.find_all("img"): # imgタグを取得しlinkに格納
        src_attr = link.get("src")
        if src_attr.endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
            sr = requests.compat.urljoin(url, src_attr) # 相対URLから絶対URLに変換
            images.append(sr) # imagesリストに格納


def main():
    for target in images: # imagesからtargetに入れる
        time.sleep(5.0) # 何秒間隔をおくか指定
        re = requests.get(target)
        with open('img/' + str(uuid.uuid4()) + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
            f.write(re.content) # .contentにて画像データとして書き込む

download_images(url)
main()
print("ok") # 確認
