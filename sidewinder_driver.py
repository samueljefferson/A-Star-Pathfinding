import sidewinder as sw
import forward_astar as fa
import adaptive_astar as aa
import view


'''
env = sw.gen_maze(101, 101, 1)
np.savetxt(filename, env, fmt='%d', delimiter='')
#sw.write_maze(101, 101)
'''


sw.write_maze("mazes/sidewinder", 101, 101, 50)

env = view.get_env('mazes/sidewinder1.txt')
#env = view.get_env('sidewinder0.txt')
path = fa.astar_env((0,0), (100,100), env, (101,101))

print(path)
view.view_env(env)

forward_path, cells_expanded = fa.repeated_astar((0,0),(100,100), env, (101, 101), -1)
#print('forward expanded', cells_expanded, 'cells')
#forward_path, cells_expanded = fa.repeated_astar_backwards((0,0),(100,100), env, (101, 101), -1)
print('backwards expanded', cells_expanded, 'cells')
view.view_path(forward_path, env)

#adaptive_path = aa.repeated_astar((0,0), (100,100), env, (101,101), -1)
#print(adaptive_path)
#view.view_path(adaptive_path, env)


'''
env = view.get_env('sidewinder0.txt')
path = fa.astar_env((0,0), (2,2), env, (3,3))
print(path)
'''
