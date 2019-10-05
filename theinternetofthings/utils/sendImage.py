import requests

url = "https://us-central1-theinternetofthings.cloudfunctions.net/ProcessImage"

def sendImage(img_url):
    query_string = "?"
    query_string += "image="+img_url
    r = requests.get(url + query_string)

    print(r.text)


sendImage("http://edge.rit.edu/edge/P15482/public/Photo Gallery/RIT_logo.jpg")
