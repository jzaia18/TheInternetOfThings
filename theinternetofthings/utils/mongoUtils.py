from pymongo import MongoClient

client = MongoClient()
db = client.internetofthings
things = db.things
users = db.users
stopwords = db.stopwords

def createThing(thing):
    if not getThing(thing["mid"]):
        things.insert_one({
            "likes": 0,
            "dislikes": 0,
            "name": thing["name"],
            "mid": thing["mid"],
        })

def getThing(mid):
    found = things.find_one({
        "mid": mid
    })
    return found

def like(mid):
    things.update({"mid": mid}, {"$inc": {"likes": 1}})

def dislike(mid):
    things.update({"mid": mid}, {"$inc": {"dislikes": 1}})

if __name__ == '__main__':
    import cloudFunctions
    resp = cloudFunctions.getImageContents("http://edge.rit.edu/edge/P15482/public/Photo Gallery/RIT_logo.jpg")
    createThing(resp[0])
    print(getThing(resp[0]["mid"]))
    like(resp[0]["mid"])
    dislike(resp[0]["mid"])
    print(getThing(resp[0]["mid"]))
