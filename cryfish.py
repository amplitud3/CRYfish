

# board reprsentation
# lower case for black
# upper case for white 

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
           
