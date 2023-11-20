import pymongo
import gridfs
import base64

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["advertisement"]

fs = gridfs.GridFS(mydb)


def put_stat(stat: dict):
    mycol = mydb["stat"]
    stat.pop('_id', None)
    mycol.insert_one(stat)


def get_all_stats(month):
    mycol = mydb["stat"]
    filter = {"month": month}
    mydoc = mycol.find(filter).sort('_id', pymongo.DESCENDING)
    return mydoc[0]


def fetch_img_url(interest):
    mycol = mydb["ad"]

    filter = { "_id": 0, "interest": 1, "banner": 1 }
    myquery = {"interest": interest}

    mydoc = mycol.find(myquery, filter)

    return mydoc[0]["banner"]


def fetch_image(interest):
    interest = interest + ".jpg"
    file = fs.find_one({'filename': interest}, sort=[('uploadDate', -1)])
    if file:
        return file.read()
    else:
        return None


def fetch_all_images():
    # fetch 5 random images and their filenames
    random_files = fs._GridFS__files.aggregate([{'$sample': {'size': 5}}])
    results = []

    for file in random_files:
        filename = file['filename']
        file_data = fs.get(file['_id']).read()

        # Convert the binary data to base64
        file_data_base64 = base64.b64encode(file_data).decode('utf-8')

        results.append((filename, file_data_base64))

    return results


def put_image_path(name, file_path):
    with open(file_path, 'rb') as f:
        image_id = fs.put(f, filename=name)
    return str(image_id)


def put_image(name, file):
    image_id = fs.put(file, filename=name)
    return str(image_id)


# put_image("test2", 'D:/Projects/0 WORK/Roota ayiya/enhanced_advertising_backend_django'
#                    '/enhanced_advertising_backend_django/ad_engine/raw_ads/animals.jpg')

# print(fetch_image("gaming.jpg"))


# print(get_all_stats())
