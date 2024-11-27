life = 7

mot = 'python'

mot_user = '_' * len(mot)

while life > 0 and mot != mot_user:
    lettre = input('entrez une lettre : ')

    if lettre in mot:
        for i in range(len(mot)):
            if mot[i] == lettre:
                mot_user = mot_user[:i] + lettre + mot_user[i + 1:]
    else:
        life -= 1

    if mot_user == mot:
        print('bravo vous avez trouvé le mot ', mot)
    elif life == 0:
        print('vous avez perdu')
    else:
        print('vous avez encore ', life, ' vie')
        print('le mot est : ', mot_user)