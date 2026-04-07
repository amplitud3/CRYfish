

# board reprsentation
# lower case for black
# upper case for white 
"""
board = [ 
            [ 'r','n','b','q','k','b','n','r' ],  # blacks backrank
            [ 'p','p','p','p','p','p','p','p' ],
            [ '.','.','.','.','.','.','.','.' ],
            [ '.','.','.','.','.','.','.','.' ], 
            [ '.','.','.','.','.','.','.','.' ], 
            [ '.','.','.','.','.','.','.','.' ], 
            [ 'P','P','P','P','P','P','P','P' ],
            [ 'R','N','B','Q','K','B','N','R' ] # whites backrank
            
         ]
            


            
def print_board(board):

    for i in range(8):
        rank = 8-i 
        print(rank, end=" ")
        for k in range(8):
            print(board[i][k],end=" ")
        print()    
         
    print("  " ,end="") 
    for  k in [ 'a','b','c','d','e','f','g','h']:
        print(k,end=" ")
    print()    
            
print_board(board)         
"""



class GameState:
    def __init__(self):
        self.board = [ 
        
            [ 'r','n','b','q','k','b','n','r' ],  # blacks backrank
            [ 'p','p','p','p','p','p','p','p' ],
            [ '.','.','.','.','.','.','.','.' ],
            [ '.','.','.','.','.','.','.','.' ], 
            [ '.','.','.','.','.','.','.','.' ], 
            [ '.','.','.','.','.','.','.','.' ], 
            [ 'P','P','P','P','P','P','P','P' ],
            [ 'R','N','B','Q','K','B','N','R' ] # whites backrank
            
         ]
        self.white_to_move = True # True-> white's turn False-> balck's turn
        self.move_log=[ ] # to record every  move
        
        
    def print_board(self):
        for i in range(8):
            rank = 8-i 
            print(rank, end=" ")
            for k in range(8):
                print(self.board[i][k],end=" ")
            print()    
         
        print("  " ,end="") 
        for  k in [ 'a','b','c','d','e','f','g','h']:
            print(k,end=" ")
        print()    
        
        
    def get_valid_moves(self):
        pass 
    
        
    def get_knight_moves(self,row,col,moves):
        
        knight_moves = [(-2,-1), (-2,+1), (-1,-2), (-1,+2),
                        (+1,-2), (+1,+2), (+2,-1), (+2,+1)]
              
        for m in knight_moves:
            i=row+m[0]
            j=col+m[1]
            
            if 0 <= i <= 7 and 0 <= j <= 7:
                destination = self.board[i][j]
                if self.white_to_move and not destination.isupper():
                    moves.append(Move((row, col), (i, j), self.board))
                elif not self.white_to_move and not destination.islower():
                    moves.append(Move((row, col), (i, j), self.board))
       
                    
                    
                    
                    
                
            
            
                                                       
               
gs=GameState()
gs.print_board()     
gs.get_knight_moves(5,5,board)   
        
        
        
class Move:
    def __init__(self, start , end , board):
        self.start_row = start[0]
        self.start_col = start[1]
        self.end_row = end[0]
        self.end_col = end[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        
        
               













 
           
