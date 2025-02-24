import subprocess

utilisateur = subprocess.run(["whoami"], capture_output=True, text=True)

print(utilisateur.stdout.strip())
