import time

startTime = time.perf_counter()
# formula Y^X(mod P)
# set Y and P for this run

# demo
# y = 7
# p = 11
# a = 3
# b = 6

# crack
# y = 453
# p = 21997
# a = 899
# b = 753

# crack long
y = 48032
p = 36945
a = 3204
b = 8363

print('Y:' + str(y) + ' P: ' +str(p))

# Alice and Bobs secret keys

# Compute Alice's public key alpha
startTimeAlpha = time.perf_counter()
alpha = (y ** a) % p
print('alpha: ' + str(alpha))
endTimeAlpha = time.perf_counter()
print('runTimeAlpha: ' + "{:.2f}".format((endTimeAlpha - startTimeAlpha)*1000) + ' ms')

# Compute Bob's public key beta
startTimeBeta = time.perf_counter()
beta = (y ** b) % p
print('beta: ' + str(beta))
endTimeBeta = time.perf_counter()
print('runTimeBeta: ' + "{:.2f}".format((endTimeBeta - startTimeBeta)*1000) + ' ms')


startTimeKeys = time.perf_counter()
keyAlpha = (beta ** a) % p
keyBeta = (alpha ** b) % p
endTimeKeys = time.perf_counter()
print('runTimeKeys: ' + "{:.2f}".format((endTimeKeys - startTimeKeys)*1000) + ' ms')

print ('keyAlpha ' + str(keyAlpha) + ' keyBeta ' + str(keyBeta))

endTime = time.perf_counter()
print('runTime: ' + "{:.2f}".format((endTime - startTime)*1000) + ' ms')

