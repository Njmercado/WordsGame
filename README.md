# Words Game

This is a simple implementation of the famous **Words Game**, *sopa de letras*. This implementation was writen on **Python 3.7.1**

## Content
In this project you gonna be able to find bunch of files. */WordsGame.py* constains the principal algorithm as a class which is referenced by */test.py*.

-  **/WordsGame.py**:
	

        def __init__(self, words, cols=15):
	        self.cols = cols
	        self.grid = [ [ "." for i in range(self.cols) ] for j in range(self.cols)] 
	        self.words = words 

	***self.grid***: matrix which gonna store words to the game. This matrix is main in this project.

	

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


	Allow to know if the given word and its random coordinates are valid to introduce in the ***self.grid*** matrix. This method is necesary because tell me if the entry word could fit on some available space into the matrix. If there are a case which could not be possible to fit it gonna evaluate if in some of those found possibilities there are letters which could be used by actual word.

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

	***__fill_row*** and ***__fill_col*** do exactly the same work but each one is used by different purposes. As its names says each one is used to push a word into ***grid*** matrix taking on mind than this word can fit and in its corresponding orientation. If word do not fit on ***grid*** is passed to a different orientation, just after pass through **50** iteration getting different **(x,y)** positions.

