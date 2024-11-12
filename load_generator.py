import requests, random
from datetime import datetime, timedelta


def secondsCalculated():
    segundos = 0
    tempoAtual = datetime.now()
    while segundos < 1:
        tempSec = datetime.now()
        diferenca = tempSec - tempoAtual
        diferenca_timedelta = timedelta(days=diferenca.days, seconds=diferenca.seconds)
        segundos = diferenca_timedelta.seconds % 60
    
    return segundos

def getHomePage(base_url):
    requests.get(base_url+"/")

def getSignUpPage(base_url):
    requests.get(base_url+"/cadastro.html")

def getErrorPage(base_url):
    requests.get(base_url+"/error")


base_url = "http://localhost:5000"
user_request = -1
seconds = 10

while seconds >= 1:
    user_request = random.randint(1,50)
    print("I will do %d home requests!" % user_request)
    for i in range(user_request):
        getHomePage(base_url)
    if user_request > 45:
        print("I will do %d sign up requests!" % (i+1))
        for i in range(5):
            getSignUpPage(base_url)
    if user_request > 49:
        print("I will do %d error requests!" % (i+1))
        for i in range(2):
            getErrorPage(base_url)
    seconds = secondsCalculated()
    print(seconds)


