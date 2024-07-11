import curses
from curses import wrapper
import queue
import time

maze = [
    ["O", "@", "@", "@", "@", "@", "@", "@", "@"],
    [" ", " ", " ", " ", " ", " ", " ", " ", "@"],
    ["@", " ", "@", "@", "@", "@", "@", "@", "@"],
    ["@", " ", " ", " ", " ", " ", " ", " ", "@"],
    ["@", " ", "@", "@", "@", "@", " ", "@", "@"],
    ["@", " ", "@", " ", " ", " ", " ", " ", "@"],
    ["@", " ", "@", " ", "@", "@", "@", "@", "@"],
    ["@", "@", " ", " ", " ", " ", " ", "@", "@"],
    ["@", "@", " ", "@", "@", "@", " ", "@", "@"],
    ["@", "@", " ", " ", "@", "@", " ", " ", "@"],
    ["@", "@", "@", "@", "@", "@", "@", "X", "@"]
]


def print_maze(stdscr, maze, path=[]): # function to print the maze
    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i*2, j*2, col, GREEN)

def find_maze(maze, start):
    for i, row in enumerate(maze):
        for j, col in enumerate(maze):
            if col == start:
                return i, j

def find_path(maze, stdscr):
    start = "O"
    end = "X"


def main(stdscr): # stdscr is the standard output screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # initialize a color pair (ID, foreground, background)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()
    print_maze(stdscr, maze) # Corrected the order of arguments
    stdscr.refresh()
    time.sleep(2) # sleep for 2 seconds
    stdscr.getch() 

wrapper(main) # wrapper is a function that sets up the curses environment and then calls the function passed to it

