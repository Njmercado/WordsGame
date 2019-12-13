import copy
import numpy as np
from random import randint

class WordsGame:
    def __init__(self, words, cols=15):

        self.cols = cols
        self.bit_map= [ [ "." for i in range(self.cols) ] for j in range(self.cols)] 
        self.grid = self.bit_map
        self.words = words 

    def get_game(self):
        return self.grid

    def get_words(self):
        return self.words

    def __random(self):
        cols = self.cols - 1
        return [randint(0,cols), randint(0,cols)]

    def __is_valid(self, word, x, y, hor_ver):

        grid = grid_t = []

        if hor_ver == 0: #horizontal
            grid = self.grid[y][x:] 
            grid_t = self.grid[y][x:x+len(word)]
        else:#vertical
            grid = self.grid[y:]
            grid_t = [ val[x] for val in self.grid[y:y+len(word)] ]
        
        if len(grid) >= len(word):
            for (index, val) in enumerate(grid_t):
                if val != '.' and val != word[index]:
                    return False
            return True
        else: 
            return False

    def __fill_row(self, word, x, y, iteration=0):

        if self.__is_valid(word, x, y, 0):
            for j, w in zip(range(x, x+len(word)), word):
                self.grid[y][j] = w
        else:
            if iteration <= 50:
                x,y=self.__random()
                self.__fill_row(word, x, y, iteration+1)
            else:
                self.__fill_col(word, x, y)


    def __fill_col(self, word, x, y, iteration=0):

        if self.__is_valid(word, x, y, 1):
            for j, w in zip(range(y, y+len(word)), word):
                self.grid[j][x] = w
        else: 
            if iteration <= 50:
                x,y=self.__random()
                self.__fill_col(word, x, y, iteration+1)
            else:
                self.__fill_row(word, x, y)

    
    def generator(self):

        for (index, word) in enumerate(self.words):

            x,y=self.__random()

            if index%2 == 0: 
                self.__fill_col(word, x, y)
            else: 
                self.__fill_row(word, x, y) 
