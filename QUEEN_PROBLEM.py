#FAMOUS QUEENS PROBLEM : PLACING THE QUEENS ON CHESS BOARD SO THAT THEY DO NOT CANCEL EACH OTHER THAT IS
#NO SAME COLOUMN,NO SAME ROW AND NOT DAIGONALLY.

class NQueens:
    def __init__(self,n):
        self.n=n
        self.chess_table=[[0 for i in range(n)] for j in range(n)]

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j]==1:
                    print("Q", end='')
                else:
                    print("-",end='')
        print("/n")
    
    def is_place_safe(self,row,col):
        for i in range(self.n):
            if self.chess_table[row][i]==1:    #horizontal check
                return False
        j=col      #top left to right bottom
        for i in range(row,-1,-1):
            if i<0:
                break
            if self.chess_table[i][j]==1:
                return False
            j=j-1
        j=col        #top right to left bottom
        for i in range(row,self.n): 
            if i<0:
                break
            if self.chess_table[i][j]==1:
                return False
            j=j-1
        return True

    def solve(self,col):
        if col==self.n:     #successfully placed
            return True 
        for row in range(self.n):   
            if self.is_place_safe(row,col):     #checking
                self.chess_table[row][col]=1
                if self.solve(col+1):
                    return True             #next queen
            self.chess_table[row][col]=0
        return False
    
    def solve_NQueens(self):
        if self.solve(0):           # zero index
            self.print_queens()
        else:
            print('There is no solution for problem')

queens=NQueens(4)           #if three, no solution
queens.solve_NQueens()                
                       