import requests


def getImageContents(img_url):
    url = "https://us-central1-theinternetofthings.cloudfunctions.net/ProcessImage"
    query_string = "?"
    query_string += "image="+img_url
    r = requests.get(url + query_string)

    return eval(r.text)

def getImageText(img_url):
    url = "https://us-central1-theinternetofthings.cloudfunctions.net/DefineCard"
    query_string = "?"
    query_string += "image="+img_url
    r = requests.get(url + query_string)

    return r.text

def translateText(text):
    url = "https://us-central1-theinternetofthings.cloudfunctions.net/translateLabel"
    query_string = "?"
    query_string += "text=" + text
    r = requests.get(url + query_string)

    return r.text


if __name__ == '__main__':
    print("Testing mode....")
    while (True):
        img_url = input("Enter URL: ")
        if img_url == '':
            break
        img_url = img_url.split("?")[0]
        #img_url = "http://edge.rit.edu/edge/P15482/public/Photo Gallery/RIT_logo.jpg"
        print("Getting image: " + img_url + "...")
        resp = getImageText(img_url)
        print("Response received!")
        print(resp)
        # for entry in resp:
        #    print(entry)
