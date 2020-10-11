
import requests
import random

def getUserLocation ():
    #some work to be done
    location = "Tunis"
    return location

def apiCall () :

    try:
        response = requests.get('http://api.aladhan.com/v1/timingsByCity?city=Tunis&country=Tunisia&method=8').json()
        print(response.get('data'))
    except ConnectionError:
        print("Connection failed ")

apiCall()