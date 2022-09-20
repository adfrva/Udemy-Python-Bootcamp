print("Welcome to the Caesar Cipher")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def listToString(list): 
    string = " "
    
    return (string.join(list))

def stringToList(string):
    return list(string)

def encrypt(phrase, shiftNum):
    encryptedStr = ""
    encryptedList = stringToList(phrase)

    for i in range(0, len(encryptedList)):

        for n in range(0, len(letters)):

            if letters[n] == encryptedList[i]:
                shiftIndex = n +  shiftNum

                if shiftIndex >= len(letters):
                    shiftIndex = shiftIndex - len(letters)
                    encryptedList[i] = letters[shiftIndex]
                    break
                else:
                    encryptedList[i] = letters[shiftIndex]
                    break

    encryptedStr = listToString(encryptedList)

    return(encryptedStr)

def decrypt(phrase, shiftNum):
    decryptedStr = ""
    decryptedList = stringToList(phrase)

    for i in range(0, len(decryptedList)):

        for n in range(0, len(letters)):

            if letters[n] == decryptedList[i]:
                shiftIndex = n - shiftNum

                if shiftIndex < 0:
                    shiftIndex = len(letters) - shiftNum
                    decryptedList[i] = letters[shiftIndex]
                    break
                else:
                    decryptedList[i] = letters[shiftIndex]
                    break

    decryptedStr = listToString(decryptedList)

    return(decryptedStr)

userChoice = input("Would you like to encrypt or decrypt a text?\n")

if userChoice.lower() == "encrypt":
    userPhrase = input("Enter the phrase you'd like to Encrypt: \n")
    shiftNum = input("Enter your shift number: \n")

    encryptedPhrase = encrypt(userPhrase, int(shiftNum))

    print("Here is your encrypted phrase: " + encryptedPhrase)

else:
    userPhrase = input("Enter the phrase you'd like to Decrypt: \n")
    shiftNum = input("Enter your shift number: \n")

    decryptedPhrase = decrypt(userPhrase, int(shiftNum))

    print("Here is your decrypted phrase: " + decryptedPhrase)
