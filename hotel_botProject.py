import requests
from bs4 import BeautifulSoup

payload={"username":"kubra",
    "password":"qweasdzxc",}
headers={
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "Upgrade-Insecure-Requests":"1"
}
login_url = 'http://localhost:8080/signin'
 
payload_new_hotel={
    "address":"abcddd",
    "category":"3*",
    "city":"abcddd",
    "code":"ilhan0123",
    "country":"abcddd",
    "email":"abcddd",
    "fax":"abcddd",
    "hotel_confirmation_types_id":"abcddd",
    "location":"abcddd",
    "manager":"abcddd",
    "name":"ilhan0123",
    "phone":"abcddd",
    "post_code":"abcddd",
    "service_type_id":"abcddd",
    "transfer_zone":"abcddd",
    "zone":"abcddd"
}
hotel_url="http://localhost/api/sejour/hotels?d=232de5ed&k=8d047ba30cf99be&s=a30cf99be0fd802b8"

url_contract="http://localhost/api/sejour/contracts?d=232de5ed&k=8d047ba30cf99be&s=a30cf99be0fd802b8"

with requests.Session() as s: 
    response = requests.post(login_url , payload) 
    response1=requests.post(hotel_url,payload_new_hotel)

    res1=response1.json()
    payload_test=res1['data'] 

    response2=requests.post(url_contract,payload_test) 
    print(response2.text)