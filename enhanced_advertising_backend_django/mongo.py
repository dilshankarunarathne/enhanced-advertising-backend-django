import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["advertisement"]


def put_stat(stat: dict):
    mycol = mydb["stat"]
    stat.pop('_id', None)
    mycol.insert_one(stat)


def get_all_stats():
    mycol = mydb["stat"]
    mydoc = mycol.find().sort('_id', pymongo.DESCENDING)
    return mydoc[0]


def fetch_img_url(interest):
    mycol = mydb["ad"]

    filter = { "_id": 0, "interest": 1, "banner": 1 }
    myquery = {"interest": interest}

    mydoc = mycol.find(myquery, filter)

    return mydoc[0]["banner"]


# print(get_all_stats())
