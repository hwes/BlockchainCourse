from Pearson import hash8

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


alicePrivateKey = 3
bobPrivateKey = 6

y = 7
p = 11

# compute public keys
alicePublicKey = (y ** alicePrivateKey) % p
bobPublicKey = (y ** bobPrivateKey) % p

print('Alice public key: ' + str(alicePublicKey) + ', Bob public key: ' + str(bobPublicKey))

# compute transaction hash
transaction = 'Alice pays Bob 500 cryptoleums'
transactionHash = hash8(transaction, exampleTable)
print('Transaction hash: ' + str(transactionHash))

# Alice signs transaction
# compute session key
signingKey = (bobPublicKey ** alicePrivateKey) % p
print('Signing key: ' + str(signingKey))

signature = transactionHash ^ signingKey
print('Signature: ' + str(signature))

# Bob verifies transaction
verificationKey = (alicePublicKey ** bobPrivateKey) % p
print ('Verification key: ' + str(verificationKey))

verification = signature ^ verificationKey
print('Verification: ' + str(verification))

if verification == transactionHash:
    print('Alice signed this transaction, verified by her private key')

# Do the proof of work for the block

difficulty = 2

for i in range(0,256):
    plainTextMessage = str(transactionHash) + str(i)
    hashedMessage = hash8(plainTextMessage, exampleTable)
    if hashedMessage <= difficulty:
        nonce = i
        print('Nonce: ' + str(i))
        print('Hashed Message: ' + str(hashedMessage))
        break

# Verify nonce

verificationMessage = str(transactionHash) + str(nonce)
verifiedHash = hash8(verificationMessage, exampleTable)
if verifiedHash <= difficulty:
    print('Proof of work verified')

