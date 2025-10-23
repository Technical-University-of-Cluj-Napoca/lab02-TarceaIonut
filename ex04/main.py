"""
Store words in a BST and return suggestions for a prefix that you type in.

(1) Define the Node class, which represents each node in the BST. Each node contains
a word and pointers to the left and right children.

(2) Define the BST class, which contains methods to insert words and to find all words
that start with a given prefix.
"""
import os
import sys

from BST import Bst
from search_engine import *




if __name__ == "__main__":
    """create a loop that asks the user to input a prefix and prints out the suggestions after each character,
    until the user types 'exit' to quit the program.
    """
    print("Start typing (press ESC to quit):")
    prefix = ""

    #bst = Bst("D:\\Faculta\\AN3 S1\\AI\\words.txt", file=True)
    bst = Bst("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt", url=True)

    bst.print_list()

    search_loop(bst)

    pass
