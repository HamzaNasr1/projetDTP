# scraper.py

import requests
from bs4 import BeautifulSoup

# URL du site à scraper
url = "http://quotes.toscrape.com/"

# Envoyer la requête GET
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Parser le contenu HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraire la première citation
    first_quote = soup.find("span", class_="text").get_text()
    
    # Afficher la citation
    print("Première citation trouvée :", first_quote)
else:
    print("Erreur lors de la requête :", response.status_code)
