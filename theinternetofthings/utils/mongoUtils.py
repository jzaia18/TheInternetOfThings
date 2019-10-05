from pymongo import MongoClient

client = MongoClient()
db = client.internetofthings
things = db.things
users = db.users
stopwords = db.stopwords

def createThing(thing):
    things.insert_one({
        "likes": 0,
        "dislikes": 0,
        "name": thing["name"],
        "mid": thing["mid"],
    })

def getThing(mid):
    db.things.find({
        "mid": mid
    })


if __name__ == '__main__':
    import cloudFunctions
    resp = cloudFunctions.getImageContents("http://edge.rit.edu/edge/P15482/public/Photo Gallery/RIT_logo.jpg")
    createThing(resp[0])
    print(getThing(resp[0]["mid"]))
