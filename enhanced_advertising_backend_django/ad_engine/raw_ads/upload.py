import pymongo
import gridfs

import os
from os import walk

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["advertisement"]

fs = gridfs.GridFS(mydb)


def fetch_image(interest):
    file = fs.find_one({'filename': interest})
    if file:
        return file.read()
    else:
        return None


def put_image(name, file_path):
    with open(file_path, 'rb') as f:
        image_id = fs.put(f, filename=name)
    return str(image_id)


# put_image("test2", 'D:/Projects/0 WORK/Roota ayiya/enhanced_advertising_backend_django'
#                    '/enhanced_advertising_backend_django/ad_engine/raw_ads/animals.jpg')

# print(fetch_image("test2"))


# need to walk and find all images in raw_ads folder and put them in mongo


mypath = 'D:/Projects/0 WORK/Roota ayiya/enhanced_advertising_backend_django/enhanced_advertising_backend_django/ad_engine/raw_ads'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

for file in f:
    put_image(file, mypath + '/' + file)


