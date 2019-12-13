from collections import deque
from WordsGame import WordsGame

def get_words():
    words = ["duque", "perro", "cosa", "persona", "cachon",
            "calculadora", "espejo", "universidad", "marcador",
            "computador", "carro", "cocuelo", "espantajopo", 
            "cacorro", "polombia"]
    words = deque(words)
    return words

def print_grid(grid):
    for i in grid.get_game():
        print(i)

if __name__=="__main__":

    words = get_words()

    grid = WordsGame(words)
    grid.generator()

    print_grid(grid)
