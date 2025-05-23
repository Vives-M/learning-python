# Importation beautifulsoup
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

# Création d'un objet soup à partir du HTML récupéré dans les requêtes
with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# 1/ Récupérez les éléments suivants dans le code html et stockez-les dans des variables, puis affichez-les dans la console :
# le titre de la page (<title> )
title = soup.title
print(title.string)

# le texte de la balise <h1> avec ID "titre"
h1 = soup.h1
print(h1.string)

# les informations sur les produits :
# nom du produit
# prix du produit (par exemple: 20€)
produits = soup.find_all('li')
for produit in produits:
    noms = produit.find('h2').string
    prix = produit.find('p', class_ = 'price').string
    print(noms, prix)

# description



# utilisez un dictionnaire pour stocker ces informations pour tous les produits.
