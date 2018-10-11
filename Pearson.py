
# A simple implementation of the Pearson hash algorithm for 8 bit computers

def hash8(message, table):
    # define hash as length of message modulo 256 (i.e. a number between 0 and 255)
    hash = len(message) % 256
    for i in message:
        # compute hash as previous hash xor ascii value of current character modulo 256
        hash = table[(hash ^ ord(i)) % 256]
    return hash

