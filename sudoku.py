import random

with open('sudoku.txt','r') as f:
    puzzles = f.readlines()
for i,puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()
#print(puzzles)

puzzle = random.choice(puzzles)
print(puzzle)


class Sudoku:


    def __init__(self,puzzle):
        self.empty_space = '.'
        self.grid_length = 9
        self.box_length = 3
        self.full_grid_size = self.grid_length * self.grid_length
        self.puzzle = puzzle
        self.grid = {}
        self.resetGrid()



    def resetGrid(self):
        for i in range(1,self.grid_length+1):
            for j in range(1,self.grid_length+1):
                self.grid[(i,j)] = self.empty_space

        assert (len(self.puzzle)==self.full_grid_size)
        i = 0
        y = 1
        while(i<self.full_grid_size):
            for x in range(1,self.grid_length+1):
                self.grid[(x,y)] = self.puzzle[i]
                i += 1
            y += 1

    def display(self):
        print('  ABC DEF GHI')
        for y in range(self.grid_length):
            for x in range(self.grid_length):
                if x==0:
                    print(str(y+1)+'|',end=' ')
                print(self.grid[(x+1,y+1)],end ='')
                if(x == 2 or x== 5):
                    print('|',end='')
            print()
            if(y == 2 or y==5):
                print('_'*12)


grid = Sudoku(puzzle)
grid.display()






