'''
    Program to view gridworlds
    to run type
    python load.py <gridworld.txt>
'''
import sys
import view

if len(sys.argv) == 1:
    print('Enter gridworld name as command line argument')
elif len(sys.argv) > 2:
    print('Error: too many arguments')
elif len(sys.argv) == 2:
    filename = list(sys.argv)[1]
    env = view.get_env('mazes/sidewinder1.txt')
    view.view_env(env)
