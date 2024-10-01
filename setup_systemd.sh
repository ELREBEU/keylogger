#!/bin/bash

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
