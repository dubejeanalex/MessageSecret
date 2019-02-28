alphabet = 'abcdefghijklmnopqrstuvwxyz'

print( alphabet[2])
key = 3
character = input("Entrez un caractère: ")
position = alphabet.find(character)

print(position)
newPosition = (position + key) % 26

newCharacter = alphabet[newPosition]
print ("The new character is: ",newCharacter)
