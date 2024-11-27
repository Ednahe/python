note_examen = float(input('entrez votre note '))

if note_examen < 0 or note_examen > 20:
    print("Veuillez entrer une note entre 0 et 20.")

if note_examen >=0 and note_examen < 10:
    print("recalé")

if note_examen >=10 and note_examen < 12:
    print('aucune mention')

if note_examen >=12 and note_examen < 14:
    print('mention assez bien')

if note_examen >=14 and note_examen < 16:
    print('mention bien')

if note_examen >=16 and note_examen < 18:
    print('mention très bien')

if note_examen >=18 and note_examen <=20:
    print('félicitation du jury')