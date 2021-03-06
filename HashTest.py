from Pearson import hash8
# from random import shuffle

# exampleTable = list(range(0, 256))
# shuffle(exampleTable)

exampleTable = [168, 44, 254, 252, 133, 130, 33, 43, 141, 229, 62,
                152, 223, 55, 241, 68, 183, 242, 121, 73, 69,
                99, 244, 134, 237, 228, 169, 47, 233, 224, 77,
                236, 179, 84, 158, 17, 63, 12, 71, 135, 221,
                190, 220, 187, 59, 243, 38, 4, 25, 186, 92,
                24, 122, 101, 116, 217, 161, 57, 222, 67, 14,
                144, 95, 98, 66, 253, 147, 180, 196, 118, 177,
                42, 21, 218, 154, 171, 9, 123, 110, 102, 124,
                127, 79, 234, 18, 34, 156, 167, 140, 78, 28,
                206, 22, 160, 232, 214, 155, 185, 178, 119, 109,
                175, 245, 139, 148, 8, 115, 76, 162, 60, 0,
                125, 192, 45, 93, 209, 157, 108, 90, 56, 182,
                35, 150, 126, 170, 48, 153, 184, 103, 145, 50,
                199, 40, 211, 114, 72, 16, 198, 23, 86, 61,
                149, 203, 202, 230, 205, 94, 75, 231, 132, 20,
                213, 250, 216, 112, 70, 51, 136, 120, 227, 58,
                137, 83, 251, 142, 27, 207, 100, 37, 210, 31,
                107, 131, 138, 165, 195, 151, 52, 164, 11, 172,
                82, 128, 5, 193, 173, 2, 106, 219, 74, 97,
                255, 246, 26, 225, 191, 105, 240, 29, 88, 239,
                129, 3, 85, 166, 19, 197, 238, 174, 235, 249,
                113, 13, 188, 6, 41, 247, 189, 111, 104, 32,
                96, 248, 146, 10, 80, 176, 49, 87, 204, 208,
                143, 81, 159, 215, 39, 89, 30, 1, 117, 7,
                65, 15, 163, 54, 226, 36, 91, 212, 181, 200,
                194, 201, 53, 46]

plainTextMessage = 'Ferie'
hashedMessage = hash8(plainTextMessage, exampleTable)

print('Message: ' + plainTextMessage)
print('Hashed Message: ' + str(hashedMessage))

plainTextMessage = 'Ferie7'
hashedMessage = hash8(plainTextMessage, exampleTable)

print('Message: ' + plainTextMessage)
print('Hashed Message: ' + str(hashedMessage))

plainTextMessage = 'Ferid'
hashedMessage = hash8(plainTextMessage, exampleTable)

print('Message: ' + plainTextMessage)
print('Hashed Message: ' + str(hashedMessage))

plainTextMessage = 'I am married to Margrete'
hashedMessage = hash8(plainTextMessage, exampleTable)

print('Message: ' + plainTextMessage)
print('Hashed Message: ' + str(hashedMessage))

plainTextMessage = 'I am married to Margrethe'
hashedMessage = hash8(plainTextMessage, exampleTable)

print('Message: ' + plainTextMessage)
print('Hashed Message: ' + str(hashedMessage))

