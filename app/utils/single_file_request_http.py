import requests

url = 'http://localhost:4747/upload'
file = {'file': open('images/1.jpeg', 'rb')}
resp=requests.post(url=url,files=file)
print(resp.json)



url = 'http://127.0.0.1:8000/upload'
files = [('files', open('images/1.png', 'rb')), ('files', open('images/2.png', 'rb'))]
resp = requests.post(url=url, files=files)
print(resp.json())

