import time

startTime = time.clock()
# formula Y^X(mod P)
# set Y and P for this run

# demo
y = 7
p = 11
a = 3
b = 6

# crack
# y = 453
# p = 21997
# a = 899
# b = 753

print('Y:' + str(y) + ' P: ' +str(p))

# Alice and Bobs secret keys

# Compute Alice's public key alpha
alpha = (y ** a) % p
print('alpha: ' + str(alpha))

# Compute Bob's public key beta
beta = (y ** b) % p
print('beta: ' + str(beta))

keyAlpha = (beta ** a) % p
keyBeta = (alpha ** b) % p


print ('keyAlpha ' + str(keyAlpha) + ' keyBeta ' + str(keyBeta))

endTime = time.clock()
print('runTime: ' + "{:.2f}".format((endTime - startTime)*1000) + ' ms')

