from caesar_ciper import logo
# ord() function is used to get the ascii of a letter.
# chr() function is used to convert ascii to a letter.
# A => 65 , Z => 90 | a => 97 , z => 122
def checkAlphabeticOrNot(char):
    charAscii = ord(char)
    return (charAscii >= 65 and charAscii <= 90) or (charAscii >= 97 and charAscii <= 122)

def encrypt(msg,shiftNumber):
    shiftNumber = shiftNumber % 26 # 26 letters in english ,then shiftNumber is in range from 0 to 25
    encryptedMsg = ""
    for char in msg:
        if(not checkAlphabeticOrNot(char)):
            encryptedMsg += char
            continue
        newCharAscii = ord(char) + shiftNumber
        if ord(char) >= 65 and ord(char) <= 90 and newCharAscii > 90:                 # char from A to Z
            newCharAscii -= 26
        elif newCharAscii > 122:                                                      # char from a to z
            newCharAscii -= 26
        encryptedMsg += chr(newCharAscii)
    print(f"Your encrypted Message : {encryptedMsg}")


def decrypt(msg,shiftNumber):
    shiftNumber = shiftNumber % 26 # 26 letters in english ,then shiftNumber is in range from 0 to 25
    decryptedMsg = ""
    for char in msg:
        if(not checkAlphabeticOrNot(char)):
            decryptedMsg += char
            continue
        newCharAscii = ord(char) - shiftNumber
        if ord(char) >= 97 and ord(char) <= 122 and newCharAscii < 97:       # char from a to z
            newCharAscii += 26
        elif newCharAscii < 65:                                              # char from A to Z
            newCharAscii += 26
        decryptedMsg += chr(newCharAscii)
    print(f"Your decrypted Message : {decryptedMsg}")


print(logo)
again = 'yes'
while again.lower() == 'yes':
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if operation != 'encode' and operation != 'decode':
        print('invalid operation, please try again !!')
    else:
        userMessage = input("Type your message: \n")
        shiftAmount = int(input("Type the shift number: \n"))
        if operation.lower() == 'encode':
            encrypt(msg = userMessage,shiftNumber = shiftAmount)
        elif operation.lower() == 'decode':
            decrypt(msg = userMessage,shiftNumber = shiftAmount)
    again = input("Type 'yes' to go again. otherwise type anything.\n")
