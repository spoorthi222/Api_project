import requests

def testUserAPI():
    dummy_json ={
        "name" : "Spoorthi",
        "age"  : 21,
        "email_id" : "spoorthi.n222@gmail.com",
        "password" : "Spoorthin222"
    }
    url = "http://localhost:8081/user/"
    response = requests.post(url, json = dummy_json)
    print response.json()


testUserAPI()
