'''
    Program to view gridworlds without pygame
    to run type
    python load.py <gridworld.txt>
    0 is unblocked path
    1 is blocked path
'''
import sys

if len(sys.argv) == 1:
    print('Enter gridworld name as command line argument')
elif len(sys.argv) > 2:
    print('Error: too many arguments')
elif len(sys.argv) == 2:
    filename = list(sys.argv)[1]
    print(filename)
    file = open(filename, 'r')
    str = file.read()
    file.close()
    print(str)
