### BONJOUR ALEXANDRA, ICI JEAN-HUGUES ROY
### TOUS MES COMMENTAIRES SERONT EN MAJUSCULES ET PRÉCÉDÉS DE 3 # (HASHTAGS)

### TON SCRIPT FAIT L'ESSENTIEL:
### LA CONCATÉNATION D'UNE PARTIE DE L'URL QUI NE CHANGE PAS ("http://montrealcampus.ca?p=")
### AVEC UNE PARTIE QUI CHANGE (LE NUMÉRO D'IDENTIFICATION)

### IL MANQUAIT SIMPLEMENT D'AJOUTER TOUTES LES URL DANS UNE LISTE
### TU POURRAIS LE FAIRE EN CRÉANT UNE LISTE VIDE AU DÉBUT DE TON SCRIPT

lesURL = [] ### CRÉATION D'UNE LISTE VIDE

montrealcampus = "http://montrealcampus.ca?p="
n=0 ### UN COMPTEUR EST UNE BONNE STRATÉGIE POUR S'ASSURER D'AVOIR LE NOMBRE D'URLS QU'ON VISE
for url in range(20000,30151):
    web = montrealcampus + str(url)
    n += 1
    # print (n,web) ### JE METS CETTE LIGNE EN COMMENTAIRE
    lesURL.append(web)

### UNE FOIS QUE LA BOUCLE A FAIT TOUT SON TRAVAIL TU PEUX EN VOIR LE RÉSULTAT
### EN AFFICHANT LE CONTENU DE LA LISTE "lesURL" ET DE TA VARIABLE "n"

print(lesURL,n)

### ENFIN, IL MANQUAIT CERTAINS COMMENTAIRES POUR QUE TU M'EXPLIQUES CE QUE TU SOUHAITAIS FAIRE.