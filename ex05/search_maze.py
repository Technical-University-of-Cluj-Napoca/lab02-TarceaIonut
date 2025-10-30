import sys

from collections import deque
from colorama import Fore

def read_maze(filename: str) -> list[list[str]]:
    """Reads a maze from a file and returns it as a list of lists (i.e. a matrix).

    Args:
        filename (str): The name of the file containing the maze.
    Returns:
        list: A 2D list (matrix) representing the maze.
    """
    with open(filename) as f:
        strings = f.readlines()
        matrix = []
        for line in strings:
            matrix.append(list_(line))
        return matrix


def find_start_and_target(maze: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Finds the coordinates of start ('S') and target ('T') in the maze, i.e. the row and the column
    where they appear.

    Args:
        maze (list[list[str]): A 2D list (matrix) representing the maze.
    Returns:
        tuple[int, int]: A tuple containing the coordinates of the start and target positions.
        Each position is represented as a tuple (row, column).
    """
    rows = len(maze)
    columns = len(maze[0])
    start = (0, 0)
    target = (0, 0)
    for i in range(rows):
        for j in range(columns):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'T':
                target = (i, j)

    return start, target


def _inline(row: int, column: int, lines:int, columns: int) -> bool:
    return not (row < 0 or row >= lines or column < 0 or column >= columns)


def get_neighbors(maze: list[list[str]], position: tuple[int, int]) -> list[tuple[int, int]]:
    """Given a position in the maze, returns a list of valid neighboring positions: (up, down, left, right)
    where the player can be moved to. A neighbor is considered valid if (1) it is within the bounds of the maze
    and (2) not a wall ('#').

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        position (tuple[int, int]): The current position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of valid neighboring positions.
    """
    # construct the direction array: list[tuple[int, int]] (up, down, left, right)
    # test the position in each direction

    d1 = [-1, 0, 0, 1]
    d2 = [0, -1, 1, 0]

    lines = len(maze)
    columns = len(maze[0])

    list_ = []

    for i in range(4):
        if _inline(position[0] + d1[i], position[1] + d2[i], lines, columns):
            list_.append((position[0] + d1[i], position[1] + d2[i]))
    return list_




def bfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a breadth-first search (BFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    # from collections you can import deque for using a queue.

    lines = len(maze)
    columns = len(maze[0])
    matrix = []
    for i in range(lines):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(-1)

    queue:deque = deque()
    queue.appendleft((start[0], start[1], 0))
    matrix[start[0]][start[1]] = 0
    end = target
    while queue:
        #print("current queue:", queue)
        current = queue.pop()
        #if current[0] == 9 and current[1] == 3:
            #print("muie")
        #if current[0] == 8 and current[1] == 3:
            #print("muie")
        matrix[current[0]][current[1]] = current[2]
        neighbors = get_neighbors(maze, (current[0], current[1]))
        for neighbor in neighbors:
            if matrix[neighbor[0]][neighbor[1]] == -1 and maze[neighbor[0]][neighbor[1]] != '#':
                queue.appendleft((neighbor[0], neighbor[1], current[2] + 1))
                matrix[neighbor[0]][neighbor[1]] = current[2] + 1

    path = []
    current_poz = end
    while True:
        path.append(current_poz)
        if current_poz == start:
            break
        neighbors = get_neighbors(maze, current_poz)
        for neighbor in neighbors:
            if matrix[neighbor[0]][neighbor[1]] == matrix[current_poz[0]][current_poz[1]] - 1 and maze[neighbor[0]][neighbor[1]] != '#':
                current_poz = neighbor
                break
        #print("current_poz", current_poz)
        #print("neighbors", neighbors)


    return path

def dfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a depth-first search (DFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    # you can use a list as a stack in Python.
    lines = len(maze)
    columns = len(maze[0])
    matrix = []
    for i in range(lines):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(-1)

    stack = []
    stack.append((start[0], start[1], 0))
    matrix[start[0]][start[1]] = 0
    end = target
    while stack:
        # print("current queue:", queue)
        current = stack.pop()
        # if current[0] == 9 and current[1] == 3:
        # print("muie")
        # if current[0] == 8 and current[1] == 3:
        # print("muie")
        matrix[current[0]][current[1]] = current[2]
        neighbors = get_neighbors(maze, (current[0], current[1]))
        for neighbor in neighbors:
            if matrix[neighbor[0]][neighbor[1]] == -1 and maze[neighbor[0]][neighbor[1]] != '#':
                stack.append((neighbor[0], neighbor[1], current[2] + 1))
                matrix[neighbor[0]][neighbor[1]] = current[2] + 1

    path = []
    current_poz = end
    while True:
        path.append(current_poz)
        if current_poz == start:
            break
        neighbors = get_neighbors(maze, current_poz)
        for neighbor in neighbors:
            if matrix[neighbor[0]][neighbor[1]] == matrix[current_poz[0]][current_poz[1]] - 1 and maze[neighbor[0]][
                neighbor[1]] != '#':
                current_poz = neighbor
                break
        # print("current_poz", current_poz)
        # print("neighbors", neighbors)

    return path
    pass



def print_maze_with_path(maze: list[list[str]], path: list[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]) -> None:
    """Prints the maze to the console, marking the path with '.' characters.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        path (list[tuple[int, int]]): A list of positions representing the path to be marked.
    Returns:
        None
    """
    # # ANSI escape code for red
    #colorama.init()
    RED = "\033[91m"
    RESET = "\033[0m"
    # encode a character with red color: RED + char + RESET
    for poz in path:
        maze[poz[0]][poz[1]] = '*'

    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'T'

    for list_ in maze:
        s = "".join(list_)
        for c in s:
            if c == '*':
                print(Fore.RED + c, end='')
            elif c == 'S' or s == 'T':
                print(Fore.GREEN + c, end='')
            else:
                print(Fore.BLACK + c, end='')
        print()

    pass



if __name__ == "__main__":
    # Example usage: py maze_search.py dfs/bfs maze.txt
    maze_path = sys.argv[1]
    #maze_path = "../maze3.txt"
    list_:list[str] = open(maze_path, 'r').readlines()
    maze_:list[list[str]] = []
    for i in range(len(list_)):
        maze_.append([])
        list_[i] = list_[i].strip()
        for j in range(len(list_[i])):
            maze_[i].append(list_[i][j])

    (start, target) = find_start_and_target(maze_)
    path = bfs(maze_, start, target)
    print_maze_with_path(maze_, path, start, target)
    pass
