# Maze Problem
A hero is trapped in a maze and he wants to escape from it. The maze can be represented as an m × n matrix of cells. Each cell in the map is referred to by a pair of coordinates that represent the cell’s “location”. Specifically, the location of the upper left corner cell of the map is (0,0), and the location of the lower right corner cell of the map is (m − 1, n − 1). Each cell in the maze can assume one of two values, namely, 0 or 1. A 0-cell is a cell of empty space where the hero can move to. A 1-cell a cell of solid wall where the hero cannot occupy.



# Rules
The Hero’s movements are restricted by two rules: (1) The hero can move only within the map. (2) The
hero can move up, down, left or right. Each valid move takes 1 time unit. Also, the starting and exiting
cells are both empty.



# Part A
  Given the locations (coordinates) of the starting and exiting cells, and the maze (as represented by
  a matrix), compute the minimum amount of time it takes the hero to escape the maze. If the hero
  cannot reach the exiting cell, your program should return -1.



# Part B
  The hero has learned a powerful skill - Flash. He can choose one direction from {up, down, left, right}
  and teleport to a target cell in the chosen direction. When using Flash, the hero can pass through any
  wall cells (and of course any empty cells). However, the target cell must be an empty cell. (Otherwise,
  the hero will be trapped inside the concrete wall.) The hero hasn’t mastered this skill perfectly yet, and
  1
  so he can only Flash once with his (limited) superpower. The maximum distance the hero can travel
  with Flash is F cells. Regardless of the distance traveled using Flash, the time taken by Flash-ing is
  1 unit.
  Given a starting cell, an exiting cell, F, and a maze, please compute the minimum amount of time for
  the hero to escape. If the hero cannot reach the exit, return -1.



# Part C

  The hero becomes proficient at Flash now. He can use Flash multiple times as long as the total
  distance traveled with Flash does not exceed F. Regardless of the distance traveled, the time used by
  each Flash is 1 unit.
  Given the hero’s start, the destination, maximum distance traveled by Flash, and the maze, compute
  the minimum amount of time for him to escape. If the hero cannot reach the destination, return -1.
