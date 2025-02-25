# KeyLogger & Mouse Tracker with Email Alert

Ce projet est une application Python qui combine plusieurs fonctionnalités :

- **Keylogging** : Enregistre les frappes clavier et les stocke dans un fichier `keylogs.txt`.
- **Suivi de la souris** : Enregistre les mouvements et clics de la souris dans un fichier `mouse.txt`.
- **Envoi d'email automatique** : Envoie périodiquement les fichiers de logs par email.
- **Tâches programmées** : Intègre des tâches planifiées via le module `TacheProgrammees` (setupCron).

> **Attention :** Ce projet à des fins éducatives et de démonstration uniquement. L'utilisation de keyloggers ou d'autres formes de surveillance sans consentement explicite est illégale et contraire à l'éthique. Utilisez ce code de manière responsable.

---

## Fonctionnalités

- **Keylogging** : 
  - Enregistrement des touches pressées avec horodatage.
- **Suivi de la souris** : 
  - Enregistrement des mouvements et des clics de la souris.
  - Identification de la direction du mouvement de la souris.
- **Envoi d'email** : 
  - Envoi automatique des fichiers `keylogs.txt` et `mouse.txt` via SMTP (configuration pour Gmail incluse).
  - Fonctionnement en thread séparé pour ne pas bloquer l'application.
- **Tâches programmées** : 
  - Mise en place de tâches programmées avec un module externe `TacheProgrammees`.

---

## Prérequis

- **Python 3.6+**
- Modules Python :
  - `logging`
  - `threading`
  - `pynput`
  - `smtplib`
  - `ssl`
  - `email`
  - `subprocess`
  - `time`
  - `os`
- Un module personnalisé : `TacheProgrammees` (incluant la fonction `setupCron`).

> **Note :** Assurez-vous d'installer les modules requis. Vous pouvez installer `pynput` via pip :

```bash
pip install pynput
