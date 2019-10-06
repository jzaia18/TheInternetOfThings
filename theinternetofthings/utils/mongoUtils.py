from pymongo import MongoClient
from hashlib import sha256

client = MongoClient()
db = client.internetofthings
things = db.things
users = db.users
stopwords = db.stopwords

def hashPass(username, password):
    return sha256(str(username+password).encode('utf-8')).hexdigest()

def create_user(username, password):
    if get_user(username) == None:
        users.insert_one({
            "username": username,
            "password": hashPass(username, password),
            "likes": [],
            "dislikes": [],
        })
        return True
    return False

def get_user(username):
    return users.find_one({"username": username})

def authenticate(username, password):
    user = get_user(username)
    if user == None:
        return False
    return user["password"] == hashPass(username, password)

def create_thing(thing):
    if not get_thing(thing["mid"]):
        things.insert_one({
            "likes": 0,
            "dislikes": 0,
            "name": thing["name"],
            "mid": thing["mid"],
        })
        return True
    return False

def get_thing(mid):
    found = things.find_one({
        "mid": mid
    })
    return found

def like(mid):
    things.update({"mid": mid}, {"$inc": {"likes": 1}})

def dislike(mid):
    things.update({"mid": mid}, {"$inc": {"dislikes": 1}})

def add_stopword(word):
    if word not in get_stopwords():
        stopwords.insert_one({"word": word})

def get_stopwords():
    return [x["word"] for x in stopwords.find()]

if __name__ == '__main__':
    import cloudFunctions
    resp = cloudFunctions.getImageContents("http://edge.rit.edu/edge/P15482/public/Photo Gallery/RIT_logo.jpg")
    create_thing(resp[0])
    print(get_thing(resp[0]["mid"]))
    like(resp[0]["mid"])
    dislike(resp[0]["mid"])
    print(get_thing(resp[0]["mid"]))
