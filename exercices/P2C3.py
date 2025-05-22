# Créez une fonction salaire_mensuel(salaire_annuel), en paramètre un salaire annuel,
# retourne le salaire mensuel correspondant en divisant le salaire annuel par 12.

def salaire_mensuel(salaire_annuel):
    return salaire_annuel/12

# Créez une fonction salaire_hebdomadaire(salaire_mensuel), en paramètre un salaire mensuel
# retourne le salaire hebdomadaire correspondant en divisant le salaire mensuel par 4.

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel/4

# Créez une fonction salaire_horaire(salaire_hebdomadaire, heures_travaillees), en paramètres un salaire hebdomadaire
# et le nombre d'heures travaillées par semaine,retourne le salaire horaire correspondant en divisant le salaire hebdomadaire
# par le nombre d'heures travaillées par semaine.

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

# Demandez à l'utilisateur de saisir son salaire annuel.

votre_salaire_annuel = float(input("Quel est votre salaire annuel (brut) ? "))

# Demandez à l'utilisateur de saisir le nombre d'heures travaillées par semaine.

vos_heures_travaillees = float(input("Combien d'heures travaillez-vous par semaine ? "))

# Appelez les fonctions précédemment créées pour calculer le salaire horaire correspondant.
votre_salaire_mensuel = salaire_mensuel(votre_salaire_annuel)
print(f"Votre salaire mensuel : {votre_salaire_mensuel}.")
votre_salaire_hebdomadaire = salaire_hebdomadaire(votre_salaire_mensuel)

# Affichez le résultat sous la forme : "Votre salaire horaire est de XX euros".

votre_salaire_horaire = round(salaire_horaire(votre_salaire_hebdomadaire, vos_heures_travaillees),2)
print(f"Votre salaire horaire est de {votre_salaire_horaire} euros bruts, ce qui représente environ {round(votre_salaire_horaire*0.77,2)} euros nets.")



# Attention : n'oubliez pas de convertir les valeurs fournies (chaînes de caractères) en nombres.
# Il est possible que les valeurs fournies soient des valeurs à virgule.
# Il faut alors utiliser float plutôt que int pour faire la conversion !
