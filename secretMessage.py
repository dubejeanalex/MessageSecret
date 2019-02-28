alphabet = 'abcdefghijklmnopqrstuvwxyz'


key=  3
newMessage=""
message = input("Entrez un message: ")
for character in message:
	if character in alphabet:
		position = alphabet.find(character)
		newPosition = (position + key) % 26
		newCharacter = alphabet[newPosition]
		newMessage+=newCharacter
	else: 
		newMessage+=character

print (newMessage)
cleDechiffrage =  key*-1
nouvellePosition = (newPosition +cleDechiffrage) % 26





