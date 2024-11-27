mot_de_passe = input('entrez un mot de passe ')

if (len(mot_de_passe)) < 5 :
    if len(mot_de_passe) == 0:
        print("il faut écrire quelque chose")
    else :
        print('le mot de passe est trop court')

elif mot_de_passe == '12345' :
    print('ok')
else:
    print('mauvais mot de passe')
print("programme terminé")

