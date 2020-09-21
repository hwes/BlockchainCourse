import time

# y = 7
# p = 11
# interceptedAlpha = 2
# interceptedBeta = 4
# maxA = 10
# maxB = 10

y = 453
p = 21997
interceptedAlpha = 12271
interceptedBeta = 7790
maxA = 1024
maxB = 1024

# y = 48032
# p = 36945
# interceptedAlpha = 34516
# interceptedBeta = 26873
# maxA = 10000
# maxB = 10000

i = 0
startTime = time.perf_counter()
for a in range(0, maxA):
    for b in range(0, maxB):
        # print a '.' for every 100.000 loops just to show progress
        if i % 100000 == 0:
            print('.', end='', flush=True)

        # compute alpha and beta for comparison
        alpha = (y ** a) % p
        beta = (y ** b) % p

        # compare to captured alpha and beta and print if match
        if alpha == interceptedAlpha and beta == interceptedBeta:
            print('\n'+'Alice Secret Key: '+ str(a) + ' alpha: ' + str(alpha) + ' Bob Secret Key: ' + str(b) + ' beta: ' + str(beta))

            # print the key
            keyAlpha = (beta ** a) % p
            keyBeta = (alpha ** b) % p
            crackTime = time.perf_counter()
            print('Time to crack: ' +"{:.2f}".format((crackTime - startTime)*1000) + ' ms')

            print ('keyAlpha ' + str(keyAlpha) + ' keyBeta ' + str(keyBeta))
        i = i+1

# display total computing time
endTime = time.perf_counter()
print('\n'+'runTime: ' +"{:.2f}".format((endTime - startTime)*1000) + ' ms')




