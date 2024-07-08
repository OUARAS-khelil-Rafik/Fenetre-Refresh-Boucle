## Description

Ce script, développé par OUARAS Khelil Rafik, utilise Selenium pour automatiser l'ouverture et le rechargement d'une page web spécifique jusqu'à ce qu'elle soit chargée avec succès. Lorsqu'elle est chargée, une notification est envoyée pour informer l'utilisateur. Le script est configuré pour utiliser le navigateur Microsoft Edge par défaut, mais peut facilement être modifié pour utiliser d'autres navigateurs comme Chrome, Firefox, ou Safari.

## Prérequis

- Python 3.12.2
- Selenium
- webdriver-manager
- plyer

## Installation

1. Cloner le dépôt ou télécharger le fichier `FRBoucle.py`.
2. Installer les dépendances nécessaires avec pip :

```bash
pip install selenium webdriver-manager plyer
```

## Configuration

### URL

L'URL à ouvrir peut être modifiée dans la variable `url` au début du script :

```python
url = "https://aadl3inscription2024.dz/AR/Inscription-desktop.php"
```

### Navigateur

Par défaut, le script est configuré pour utiliser Microsoft Edge. Pour utiliser un autre navigateur, décommentez la section correspondante et commentez les autres. Par exemple, pour utiliser Chrome :

```python
# Fonction pour initialiser le driver (with Chrome)
def init_driver():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Ouvrir le navigateur en plein écran
    options.add_argument("--disable-extensions")  # Désactiver les extensions
    driver = webdriver.Chrome(service=service, options=options)
    return driver
```

## Utilisation

Exécutez le script avec Python :

```bash
python FRBoucle.py
```

Le script va tenter d'ouvrir la page web spécifiée, recharger la page jusqu'à ce que le titre corresponde à "Plateforme AADL3 : Inscription", et envoyer une notification lorsque la page est chargée avec succès.

## Personnalisation

- **Délai d'attente de chargement de la page :**
  Le délai d'attente par défaut pour le chargement de la page est de 30 secondes. Cela peut être modifié dans la ligne suivante :

  ```python
  driver.set_page_load_timeout(30)
  ```

- **Intervalle de rechargement :**
  L'intervalle par défaut entre chaque tentative de rechargement est de 1 seconde. Cela peut être modifié dans la ligne suivante :

  ```python
  time.sleep(1)
  ```

## Notification

Une notification sera envoyée lorsque la page sera chargée avec succès. Le titre et le message de la notification peuvent être personnalisés ici :

```python
notification_title = "Page chargée avec succès"
notification_message = "La page AADL3 Inscription est chargée avec succès."
```

## Avertissement

Utilisez ce script de manière responsable et assurez-vous de respecter les termes et conditions du site web que vous essayez d'accéder.

## Auteur

OUARAS Khelil Rafik
