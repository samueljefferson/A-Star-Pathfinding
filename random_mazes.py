import numpy as np
import forward_astar as fa

rows = cols = 101

rows = 101
cols = 101
env_count = 50
name = "random_mazes/rand_maze"
ext = ".txt"

current = 0
while current < env_count:
    path = None
    while path == None:
        filename = name + str(current) + ext
        print("generating", filename)
        env = np.random.randint(0, 11,(rows*cols)).reshape(rows,cols)

        for i in range(0, rows):
            for j in range(0, cols):
                if env[i][j] < 9:
                    env[i][j] = 0
                else:
                    env[i][j] = 1
        env[0][0] = 0
        env[rows-1][cols-1] = 0
        print('finding path')
        #path = fa.astar_env((0,0), (rows-1, cols-1), env, (rows, cols))
        path = 1
    print('path found for maze', current)
    np.savetxt(filename, env, fmt='%d', delimiter='')
    current += 1
print('trace')
