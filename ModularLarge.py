import time

startTime = time.perf_counter()

for x in range(0, 10000):
    # print('X = ' + str(x))
    y = 453 ** x
    # print('Y = ' + str(y))
    z = y % 21997
    # print('Z = '+ str(z))
    if z == 5787:
        print('X was ' + str(x))
        endTime = time.perf_counter()
        print('\n'+'runTime: ' +"{:.2f}".format((endTime - startTime)*1000) + ' ms')
        break

        # print('Y is ' + "{:2e}".format(y))
        # print('X: ' + str(x) + '           Y: ' + str(y) + '       Z: ' +str(z))

