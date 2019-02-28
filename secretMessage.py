alphabet = 'abcdefghijklmnopqrstuvwxyz'

print( "Veuillez choisir votre clé")
key=  int (input())

character = input("Entrez un caractère: ")
position = alphabet.find(character)

print(position)
newPosition = (position + key) % 26

newCharacter = alphabet[newPosition]
print ("The new character is: ",newCharacter)

cleDechiffrage =  key*-1
nouvellePosition = (newPosition +cleDechiffrage) % 26

print (alphabet [nouvellePosition])



