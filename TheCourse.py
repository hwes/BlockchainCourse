# A simple implementation of the Pearson hash algorithm for 8 bit computers
def hash8(message, table):
    # define hash as length of message modulo 256 (i.e. a number between 0 and 255)
    hash = len(message) % 256
    for i in message:
        # compute hash as previous hash xor ascii value of current character modulo 256
        hash = table[(hash ^ ord(i)) % 256]
    return hash


# A function to sign transactions and blocks
def sign(private_key, public_key, transaction):

    # compute hash of transaction to be signed
    transaction_hash = hash8(transaction, example_table)

    # compute the signing key using Diffie Hellman
    signing_key = (public_key ** private_key) % p

    # compute the signature as an xor of the hash and the key
    signature = transaction_hash ^ signing_key

    return signature


# A function to verify transaction and block signatures
def verify(private_key, public_key, transaction, signature):

    # compute hash of transaction to be verified
    transaction_hash = hash8(transaction, example_table)

    # compute key to be used in verification using Diffie Hellman
    verification_key = (public_key ** private_key) % p

    # compute verification signature

    verification = signature ^ verification_key

    if verification == transaction_hash:
        return True
    else:
        return False


def calculate_nonce(block_hash):
    for i in range(0,256):
        test_hash = str(block_hash) + str(i)
        calculated_hash = hash8(test_hash, example_table)
        if calculated_hash <= difficulty:
            nonce = i
            return nonce


# Verify nonce
def verify_nonce(block_hash, nonce):
    test_hash = str(block_hash) + str(nonce)
    verified_hash = hash8(test_hash, example_table)
    if verified_hash <= difficulty:
        return True
    else:
        return False


# define a hashing table to be used throughout the calculations
example_table = [168, 44, 254, 252, 133, 130, 33, 43, 141, 229, 62,
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
                 194, 201, 53, 46, 256]

# define the two constants used in the key calculations
y = 7
p = 11

# define the difficulty in Nonce calculations
difficulty = 16


# Define all the private and public keys needed throughout

# Miner key, will be used to sign all transactions towards
miner_private_key = 7
miner_public_key = (y ** miner_private_key) % p

# Alice
alice_private_key = 3
alice_public_key = (y ** alice_private_key) % p

# Bob
bob_private_key = 6
bob_public_key = (y ** bob_private_key) % p

# Charlie
charlie_private_key = 4
charlie_public_key = (y ** charlie_private_key) % p

# David
david_private_key = 8
david_public_key = (y ** david_private_key) % p

# Eve
eve_private_key = 5
eve_public_key = (y ** eve_private_key) % p

# Define transaction 1
transaction_1 = 'Alice pays Bob 5000 cryptoleums'

# Alice and Bob signs transaction 1
alice_signature_t1 = sign(alice_private_key, miner_public_key, transaction_1)
bob_signature_t1 = sign(bob_private_key, miner_public_key, transaction_1)

# Miner verifies transaction 1
if verify(miner_private_key, bob_public_key, transaction_1, bob_signature_t1) and \
    verify(miner_private_key, alice_public_key, transaction_1, alice_signature_t1):
    print('Transaction 1 verified by Miner with Alice signature ' + str(alice_signature_t1) + ' and Bob signature ' + str(bob_signature_t1))

# Define transaction 2
transaction_2 = 'David pays Charlie 15 000 cryptoleums'
david_signature_t2 = sign(david_private_key, miner_public_key, transaction_2)
charlie_signature_t2 = sign(charlie_private_key, miner_public_key, transaction_2)

# Miner verifies transaction 2
if verify(miner_private_key, david_public_key, transaction_2, david_signature_t2) and \
        verify(miner_private_key, charlie_public_key, transaction_2, charlie_signature_t2):
    print('Transaction 2 verified by Miner with David signature ' + str(david_signature_t2) + ' and Charlie signature ' + str(charlie_signature_t2))

# Define transaction 3
transaction_3 = "Eve pays Alice 125 000 cryptoleums"
eve_signature_t3 = sign(eve_private_key, miner_public_key, transaction_3)
alice_signature_t3 = sign(alice_private_key, miner_public_key, transaction_3)

# Miner verifies transaction 3
if verify(miner_private_key, eve_public_key, transaction_3, eve_signature_t3) and \
        verify(miner_private_key, alice_public_key, transaction_3, alice_signature_t3):
    print('Transaction 3 verified by Miner with Eve signature ' + str(eve_signature_t3) + ' and Alice signature ' + str(alice_signature_t3))

# Define transaction 4
transaction_4 = "Bob pays Charlie 37 000 cryptoleums"
bob_signature_t4 = sign(bob_private_key, miner_public_key, transaction_4)
charlie_signature_t4 = sign(charlie_private_key, miner_public_key, transaction_4)

# Miner verifies transaction 4
if verify(miner_private_key, bob_public_key, transaction_4, bob_signature_t4) and \
        verify(miner_private_key, charlie_public_key, transaction_4, charlie_signature_t4):
    print('Transaction 4 verified by Miner with Bob signature ' + str(bob_signature_t4) + ' and Charlie signature ' + str(charlie_signature_t4))

# Miner builds a block
block = transaction_1 + str(alice_signature_t1) + str(bob_signature_t1) \
        + transaction_2 + str(david_signature_t2) + str(charlie_signature_t2) \
        + transaction_3 + str(eve_signature_t3) + str(alice_signature_t3) \
        + transaction_4 + str(charlie_signature_t4) + str(bob_signature_t4)

block_hash = hash8(block, example_table)
block_nonce = calculate_nonce(block_hash)

miner_block_signature = sign(miner_private_key, alice_public_key, block + str(block_nonce))
print('Miner signs block with hash ' + str(block_hash) + ' and nonce ' + str(block_nonce) + ' to signature ' + str(miner_block_signature))

if verify(alice_private_key, miner_public_key, block + str(block_nonce), miner_block_signature):
    print('Block signature verified by Alice')

if verify_nonce(block_hash, block_nonce):
    print('Block nonce verified')
