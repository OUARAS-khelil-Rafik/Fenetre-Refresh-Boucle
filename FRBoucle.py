import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from plyer import notification

# URL à ouvrir
url = "https://aadl3inscription2024.dz/AR/Inscription-desktop.php"

# Fonction pour initialiser le driver (Edge)
def init_driver():
    service = EdgeService(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")  # Ouvrir le navigateur en plein écran
    options.add_argument("--disable-extensions")  # Désactiver les extensions
    driver = webdriver.Edge(service=service, options=options)
    return driver

"""
# Fonction pour initialiser le driver (Chrome)
def init_driver():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Ouvrir le navigateur en plein écran
    options.add_argument("--disable-extensions")  # Désactiver les extensions
    driver = webdriver.Chrome(service=service, options=options)
    return driver
"""

"""
# Fonction pour initialiser le driver (Firefox)
def init_driver():
    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")  # Ouvrir le navigateur en plein écran
    options.add_argument("--disable-extensions")  # Désactiver les extensions
    driver = webdriver.Firefox(service=service, options=options)
    return driver
"""

"""
# Fonction pour initialiser le driver (Safari)
def init_driver():
    options = webdriver.SafariOptions()
    driver = webdriver.Safari(options=options)
    driver.maximize_window()  # Ouvrir le navigateur en plein écran
    return driver
"""

# Initialisation du driver
driver = init_driver()

# Essayer d'ouvrir l'URL jusqu'à ce que la page soit chargée
while True:
    try:
        driver.set_page_load_timeout(30)  # Augmenter le délai d'attente à 30 secondes
        driver.get(url)
        
        # Vérifier le titre de la page jusqu'à ce qu'il soit le titre attendu
        while True:
            if driver.title == "Plateforme AADL3 : Inscription":
                print("Page chargée avec succès.")
                notification_title = "Page chargée avec succès"
                notification_message = "La page AADL3 Inscription est chargée avec succès."
                notification.notify(
                    title=notification_title,
                    message=notification_message,
                    app_name='Python Script',
                    timeout=10  # Durée d'affichage de la notification en secondes
                )
                
                # Ajouter d'autres instructions ici sans fermer le navigateur
                time.sleep(10)  # Attente de 10 secondes avant de continuer
                
                break  # Sortir de la boucle intérieure si la page est chargée
                
            print("Titre actuel:", driver.title)
            driver.refresh()  # Recharger la page si le titre n'est pas celui attendu
            time.sleep(1)  # Attendre 1 seconde avant de vérifier à nouveau
        
        # Sortir de la boucle principale si la page est chargée avec succès
        break
    
    except Exception as e:
        print(f"Erreur lors du chargement de la page: {e}")
        time.sleep(5)  # Attendre quelques secondes avant de réessayer

# Ne pas fermer le navigateur ici pour maintenir la session ouverte

# Vous pouvez ajouter d'autres instructions ici sans fermer le navigateur

# Par défaut, le navigateur ne se fermera pas automatiquement à la fin du script
# Vous pouvez continuer à interagir avec le navigateur ouvert

# Par exemple, vous pouvez ajouter une attente pour garder le script actif
while True:
    time.sleep(10)  # Attente de 10 secondes avant de répéter une action ou autre

# Vous pouvez choisir de fermer le navigateur plus tard avec driver.quit() lorsque vous avez terminé
# driver.quit()
