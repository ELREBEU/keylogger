import os
import subprocess
import sys


def setupTaskScheduler(filename):
    # Chemin vers le script Python
    python_script = os.path.join(os.getcwd(), filename)

    # Commande pour ajouter une tâche au Planificateur de tâches
    task_name = "MyPythonScriptOnStartup"

    # Vérifier si la tâche existe déjà
    try:
        result = subprocess.run(
            ['schtasks', '/Query', '/TN', task_name],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print("La tâche est déjà présente dans le Planificateur de tâches.")
            return
    except subprocess.CalledProcessError:
        # La tâche n'existe pas encore
        pass

    # Ajouter une tâche qui lance le script Python au démarrage de l'ordinateur
    command = f"python {python_script}"

    try:
        subprocess.run(
            [
                'schtasks', '/Create',
                '/TN', task_name,  # Nom de la tâche
                '/TR', command,  # Commande à exécuter
                '/SC', 'ONSTART',  # Déclenchement à l'allumage du PC
                '/F'  # Forcer l'ajout de la tâche
            ],
            check=True
        )
        print("La tâche a été ajoutée au Planificateur de tâches.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'ajout de la tâche : {e}")


# Utilisation
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Veuillez fournir le nom du fichier Python à exécuter.")
    else:
        setupTaskScheduler(sys.argv[1])
