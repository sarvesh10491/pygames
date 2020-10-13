import pygame
import time
import random
import os

grid =  [   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
            [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ], 
            [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], 
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
            [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ], 
            [ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ], 
            [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ], 
            [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], 
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] 
        ]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        sum = 0
        
        if i==0 and j==0:
            sum += grid[i][j+1]%2+grid[i+1][j+1]%2+grid[i+1][j]%2
        elif i==0 and j==len(grid[0])-1:
            sum += grid[i][j-1]%2+grid[i+1][j-1]%2+grid[i+1][j]%2
        elif i==len(grid)-1 and j==0:
            sum += grid[i][j+1]%2+grid[i-1][j+1]%2+grid[i-1][j]%2
        elif i==len(grid)-1 and j==len(grid[0])-1:
            sum += grid[i][j-1]%2+grid[i-1][j-1]%2+grid[i-1][j]%2
        elif i==0:
            sum += grid[i][j-1]%2+grid[i+1][j-1]%2+grid[i][j+1]%2+grid[i+1][j+1]%2+grid[i+1][j]%2
        elif i==len(grid)-1:
            sum += grid[i][j+1]%2+grid[i-1][j+1]%2+grid[i-1][j]%2+grid[i-1][j-1]%2+grid[i][j-1]%2
        elif j==0:
            sum += grid[i][j+1]%2+grid[i+1][j+1]%2+grid[i+1][j]%2+grid[i-1][j+1]%2+grid[i-1][j]%2
        elif j==len(grid[0])-1:
            sum += grid[i][j-1]%2+grid[i-1][j-1]%2+grid[i-1][j]%2+grid[i+1][j-1]%2+grid[i+1][j]%2
        else:
            sum += grid[i][j+1]%2+grid[i-1][j+1]%2+grid[i-1][j]%2+grid[i-1][j-1]%2+grid[i][j-1]%2+grid[i+1][j-1]%2+grid[i+1][j]%2+grid[i+1][j+1]%2

        if grid[i][j]==0:
            if sum==3:
                grid[i][j] = 3
            else:
                grid[i][j] = 4
        
        if grid[i][j]==1:
            if sum<=1 or sum>=4:
                grid[i][j] = 4
            else:
                grid[i][j] = 3


for row in grid:
    for cell in row:
        print(str(cell%2), end = " ")
    print("\n")