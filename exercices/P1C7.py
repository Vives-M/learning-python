# Créez un dictionnaire appelé  fruits  avec les clés  pomme  ,  banane  et  orange  , et les valeurs  rouge  ,  jaune  et  orange  .
fruits = {}
fruits["pomme"] = "rouge"
fruits["banane"] = "jaune"
fruits["orange"] = "orange"
# Ajoutez la clé  kiwi  avec la valeur  vert  au dictionnaire  fruits  .
fruits["kiwi"] = "vert"
print(f"Dictionnaire de fruits : {fruits}")
# Accédez à la valeur correspondant à la clé  banane  et stockez-la dans une variable appelée  couleur_banane  .
couleur_banane = fruits["banane"]
# Modifiez la valeur associée à la clé  pomme  pour  vert  .
fruits["pomme"] = "vert"
print(f"Dictionnaire de fruits : {fruits}")
# Supprimez la clé  banane  du dictionnaire  fruits  .
del fruits["banane"]
# Affichez les clés restantes dans le dictionnaire.
print(f"Clés restantes : {fruits.keys()}")
