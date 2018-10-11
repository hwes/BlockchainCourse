from random import shuffle

example_table = list(range(0, 10))

print('Original table')
for i in range(0,10):
    print('Element ' + str(i) + ': ' + str(example_table[i]))

shuffle(example_table)

print('Shuffled table')
for i in range(0,10):
    print('Element ' + str(i) + ': ' + str(example_table[i]))
