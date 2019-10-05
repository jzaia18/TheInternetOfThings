import requests

url = "https://us-central1-theinternetofthings.cloudfunctions.net/ProcessImage"

def getImageContents(img_url):
    query_string = "?"
    query_string += "image="+img_url
    r = requests.get(url + query_string)

    return eval(r.text)


if __name__ == '__main__':
    print("Testing mode....")
    img_url = "http://edge.rit.edu/edge/P15482/public/Photo Gallery/RIT_logo.jpg"
    print("Getting image: " + img_url + "...")
    resp = getImageContents(img_url)
    print("Response received!")
    for entry in resp:
        print(entry)
