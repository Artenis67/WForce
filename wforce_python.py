from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configuration de Selenium et du navigateur (Chrome)
driver = webdriver.Chrome()  # Assurez-vous d'avoir installé ChromeDriver et que son chemin est configuré
driver.get("https://svt-erlich.fr/seconde/enseignement-obligatoire/theme-2-la-terre-la-vie-et-lorganisation-du-vivant/")

# Attendre que la page se charge
time.sleep(5)

# Cliquez sur l'élément spécifique (ajustez le sélecteur CSS en conséquence)
try:
    element = driver.find_element_by_css_selector('votre_selecteur_css')  # Remplacez "votre_selecteur_css" par le sélecteur approprié
    element.click()
except Exception as e:
    print("Erreur lors de la recherche de l'élément :", e)

# Attendez un court instant
time.sleep(1)

# Générez tous les chiffres
def generer_tous_les_chiffres():
    chiffres = [str(i).zfill(8) for i in range(1, 100000000)]
    return chiffres

chiffres = generer_tous_les_chiffres()

# Boucle pour envoyer chaque chiffre à un emplacement spécifique sur la page
for chiffre in chiffres:
    # Copiez le chiffre dans le presse-papiers (en utilisant JavaScript)
    driver.execute_script(f"navigator.clipboard.writeText('{chiffre}')")

    # Collez le chiffre dans un champ de saisie (ajustez l'élément selon votre page)
    champ_saisie = driver.find_element_by_id("champ")  # Remplacez "champ" par l'ID de votre champ
    champ_saisie.clear()  # Effacez le champ s'il contient déjà du texte
    champ_saisie.send_keys(Keys.CONTROL, 'v')

    # Appuyez sur Entrée
    champ_saisie.send_keys(Keys.ENTER)

    # Attendez un certain temps
    time.sleep(1)

# Fermez le navigateur
driver.quit()