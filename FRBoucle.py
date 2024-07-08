""" OUARAS Khelil Rafik """
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from plyer import notification

# URL à ouvrir
url = "https://aadl3inscription2024.dz/AR/Inscription-desktop.php" # Ici vous pouvez changer l'url

# Fonction pour initialiser le driver (with Edge)
def init_driver():
    service = EdgeService(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")  # Ouvrir le navigateur en plein écran
    options.add_argument("--disable-extensions")  # Désactiver les extensions
    driver = webdriver.Edge(service=service, options=options)
    return driver

"""
# Fonction pour initialiser le driver (with Chrome)
def init_driver():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Ouvrir le navigateur en plein écran
    options.add_argument("--disable-extensions")  # Désactiver les extensions
    driver = webdriver.Chrome(service=service, options=options)
    return driver
"""

"""
# Fonction pour initialiser le driver (with Firefox)
def init_driver():
    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")  # Ouvrir le navigateur en plein écran
    options.add_argument("--disable-extensions")  # Désactiver les extensions
    driver = webdriver.Firefox(service=service, options=options)
    return driver
"""

"""
# Fonction pour initialiser le driver (with Safari)
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
            if driver.title == "Plateforme AADL3 : Inscription" :
                print("Page chargée avec succès.")
                notification_title = "Page chargée avec succès"
                notification_message = "La page AADL3 Inscription est chargée avec succès."
                notification.notify(
                    title=notification_title,
                    message=notification_message,
                    app_name='Page chargée avec succès',
                    timeout=20  # Durée d'affichage de la notification en secondes
                )
                
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

# Vous pouvez choisir de fermer le navigateur avec driver.quit() lorsque vous avez terminé
# driver.quit()
