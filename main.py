import requests
from bs4 import BeautifulSoup
import pandas as pd

names_list = []
model_list = []
price_list = []
img_list = []
url = "https://www.ampto.com/collections"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"lxml")

box = soup.find("div",class_="grid")
# print(box)
names = box.find_all("p",class_ ="collection-block-item__title heading h2")
# print(items)

for n in range(0,35):
    items = box.find_all("a",class_ = "collection-block-item collection-block-item--overlay")[n].get("href")
    # print(items)
    new_url = "https://www.ampto.com" + items 

    url = new_url
    r = requests.get(url)
    # print(r)
    soup = BeautifulSoup(r.text,"lxml")
    item_box = soup.find("div",class_ = "product-list product-list--collection")
    # print(item_box)
    # # --------------- Model image
    # imgs = item_box.find_all("img",class_ = "product-item__primary-image")
    # # print(imgs)

    # for j in imgs:
    #     image = j['src']
    #     img_list.append(image)

    # # print(len(img_list))
    # --------------- Model Name and Model price
    models_info = item_box.find_all("div",class_ = "product-item__info-inner")
    # print(models_info)
    for i in models_info:
        name = i.a.text
        model_list.append(name)
        name1 = i.span.text.strip().replace("Sale price$","")
        price_list.append(name1)
        for j in names[n]:
            name = j.text
            names_list.append(name)
        
    # print(len(model_list))
    # print(price_list)   
    # -------------------
    url = "https://www.ampto.com/collections"
    r = requests.get(url)
    # print(r)
    soup = BeautifulSoup(r.text,"lxml")

    box = soup.find("div",class_="grid")


df = pd.DataFrame({"Items":names_list,"Models":model_list,"Prices":price_list})
# print(df)
df.to_csv("Inventory.csv")



