import sidewinder as sw
import forward_astar as fa
import adaptive_astar as aa
import view
import time

env = view.get_env('mazes/sidewinder0.txt')
# TODO
# Sam fix repeated_astar_backwards view.py file, getting error
'''
start = time.time()
forward_path, cells_expanded = aa.repeated_astar((0,0), (100, 100), env, (101, 101), 1)
end = time.time()
print('\tExpanded:', cells_expanded, 'cells')
print('\tRuntime:', str((end-start)), 'seconds')
view.view_path(forward_path, env)
'''

view.view_all_path((0,0), (100,100), env)


'''
# TODO fix me
env = view.get_env('mazes/sidewinder1.txt')
forward_path, cells_expanded = fa.repeated_astar_backwards((0,0),(100,100), env, (101, 101), -1)
view.view_path(forward_path, env)
'''


'''
env = view.get_env('mazes/sidewinder1.txt')
forward_path, cells_expanded = aa.repeated_astar((0,0),(100,100), env, (101, 101), -1)
view.view_path(forward_path, env)
'''
