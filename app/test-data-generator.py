'''
generate a list of test data for the database
'''

from random import randint

items = '''cap-nut
carriage-bolt
castle-nut
coupling-nut
double-end-bolt
flange-bolt
flange-serrated-nut
hex-bolt
hex-finish-nut
hex-jam-nut
keps-k-lock-nut
knurled-thumb-nut
lag-bolt
locking-nut-(friction)
locking-nut-(positive)
machine-screw
nylon-hex-jam-nut
nylon-insert-lock-nut
penta-head-bolt
prevailing-torque-lock-nut
round-head-bolt
shear-nut
shoulder-bolt
slotted-hex-nut
socket-head-bolt
square-nut
structural-hex-nut
t-head-bolt
t-nut
tri-groove-nut
u-bolt
wing-nut'''.split('\n')

size = len(items)

data = tuple(zip(['{0:02d}'.format(i+1) for i in range(size)], items, [str(randint(0, 1000)) for _ in range(size)]))

with open('test-data.txt', 'w') as test_file:

    test_file.write('\n'.join([
        ' '.join(i) for i in data
    ]))