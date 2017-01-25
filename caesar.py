def alphabet_position(letter): # Returns alphabet position of the letter
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in upperCase:
        return ord(letter) - 65
    else:
        return ord(letter) - 97

def rotate_character(char , rot): # Returns encrypted character
    rotated_index = 0
    encrypted = ''
    if char.isalpha():
        if char == char.lower():
            rotated_index = alphabet_position(char)
            rotated_index += rot
            rotated_index = rotated_index % 26
            encrypted += chr(rotated_index + 97)
        else:
            rotated_index = alphabet_position(char)
            rotated_index += rot
            rotated_index = rotated_index % 26
            encrypted += chr(rotated_index + 65)
    else:
        encrypted += char
    return encrypted

def encrypt(text, rot):
    encryptedMsg = ""
    for character in text:
        encryptedMsg += rotate_character(character, rot)
    return encryptedMsg
