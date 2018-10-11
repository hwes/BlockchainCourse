
clearText = ord('X')
encryptionKey = ord('9')
encryptedText = ''
encryptedText = clearText ^ encryptionKey
newClearText = encryptedText ^ encryptionKey

print(str(clearText) + '/' + str(encryptionKey) + '/' + str(encryptedText) + '/' + str(newClearText))
print(bin(clearText) + '/' + bin(encryptionKey) + '/' + bin(encryptedText) + '/' + bin(newClearText))
# print(clearText + '/' + encryptionKey + '/' + encryptedText)


