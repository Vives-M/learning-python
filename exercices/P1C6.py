# Créer une liste fruits
fruits = ["pomme", "banane", "orange"]
# Ajouter kiwi à la liste
fruits.append("kiwi")
print(fruits)
# Supprimer orange
fruits.remove("orange")
print(fruits)
# Modifier le deuxième élément de la liste  fruits  en  ananas
fruits[1] = "ananas"
# Afficher la longueur de la liste  fruits
print(f"Longueur de la liste : {len(fruits)}")
# Trier la liste  fruits  par ordre alphabétique et afficher
fruits.sort()
print(f"Liste triée :{fruits}")
