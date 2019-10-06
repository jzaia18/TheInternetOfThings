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


if __name__ == '__main__':
    print("Testing mode....")
    img_url = "https://media.discordapp.net/attachments/564894502725222400/630160881715511356/20191005_175333.jpg"
    #img_url = "http://edge.rit.edu/edge/P15482/public/Photo Gallery/RIT_logo.jpg"
    print("Getting image: " + img_url + "...")
    resp = getImageText(img_url)
    print("Response received!")
    print(resp)
    # for entry in resp:
    #    print(entry)
