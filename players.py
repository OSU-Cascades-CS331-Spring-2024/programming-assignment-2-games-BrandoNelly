'''
    Defines Player class, and subclasses Human and Minimax Player.
'''
import time
from time import time

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row
    


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        self.depth = 5
        self.total_time = 0
        self.total_moves = 0
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'


    def average_time(self):
        return self.total_time / self.total_moves


    def get_move(self, board):
        col, row = self.minimax(board)
        return col, row



    def utility(self, board, player_symbol):
        if player_symbol == 1:
            return board.count_score(self.symbol) - board.count_score(self.oppSym)
        else:
            return board.count_score(self.oppSym) - board.count_score(self.symbol)

    

    def successor(self,  board, symbol):
        return board.total_legal_moves(symbol)
    

    def minimax(self, board):
        start = time()
        value, best_move = self.max_value(board)
        end = time()

        self.total_time += end - start

        self.total_moves += 1

        print("time: " , end - start)
        return best_move


    def max_value(self, board):

        if not board.has_legal_moves_remaining(self.symbol) or self.depth == 0:
            return self.utility(board, 1), None
        
        move = None
        value = float('-inf')
        for a in self.successor(board, self.symbol):
            cloned_board = board.clone_of_board()
            cloned_board.play_move(a[0], a[1], self.symbol)
            self.depth -= 1 
            v2, temp = self.min_value(cloned_board)
            self.depth += 1
            if v2 > value:
                value, move = v2, a

        return value, move
                
            
    def min_value(self, board):
        if not board.has_legal_moves_remaining(self.oppSym) or self.depth == 0:
            return self.utility(board, None), None
        
        move = None
        value = float('inf')
        for a in self.successor(board, self.oppSym):
            cloned_board = board.clone_of_board()
            cloned_board.play_move(a[0], a[1], self.oppSym) 
            self.depth -= 1 
            v2, temp = self.max_value(cloned_board)
            self.depth += 1 
            if v2 < value:
                value, move = v2, a

        return value, move



        
        






