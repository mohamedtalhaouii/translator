#Deep_translator Libary #Mohamed Talhaoui
from deep_translator import GoogleTranslator

#Utilisez n'importe quel traducteur de votre choix
TEXT = str(input("\nEntrer le Texte : "))
LANGUE = str(input("\nQuelle est la langue que vous voulez traduire? : "))

#traduction de la texte
translated = GoogleTranslator(source='auto', target = LANGUE ).translate( TEXT )
print(translated)