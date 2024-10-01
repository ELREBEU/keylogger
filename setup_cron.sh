#!/bin/bash

# Variables
PYTHON_SCRIPT_PATH="/chemin/vers/monscript.py"

# Chemin vers l'interpréteur Python
PYTHON_EXEC=$(which python3)

# Ajouter la tâche @reboot à la crontab de l'utilisateur courant
echo "Ajout de la tâche cron pour lancer le script Python au démarrage..."

# Vérification pour éviter les doublons
(crontab -l 2>/dev/null | grep -v "@reboot $PYTHON_EXEC $PYTHON_SCRIPT_PATH"; echo "@reboot $PYTHON_EXEC $PYTHON_SCRIPT_PATH") | crontab -

echo "La tâche cron a été ajoutée pour exécuter le script Python au démarrage."
