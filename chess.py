# chess.py 

from termcolor import colored
RANK = 'abcdefgh'
board = [['0' for x in range(8)] for y in range(8)]

test = ['RNBQKBNR', 'PPPP0PPP', '00000000','00000000','000pPp00','0000p000','pppppppp','rnbqkbnr']
testboard = [[] for n in range(8)]
board = testboard
for i in range(8):
    testboard[i] = [p for p in test[i]]

def printboard(board):
    for row in reversed(board): 
        for piece in row: 
            if piece == '0': 
                print('.',end=' ')
            else:
                if piece.islower(): 
                    print(colored(piece,'red'), end=' ')
                else: 
                    print(colored(piece, 'green'), end=' ')
        print()

def piecelegalmoves(x,y, lastmove):
    # CAPTURES 
    moves = []
    piece = board[x][y]
    
    if piece == '0':
        return []
    
    if piece in 'RrQq': 
        #build straight lines until collision
        UP = (1,0) 
        DOWN = (-1,0)
        LEFT = (0,1)
        RIGHT = (0,-1)

        for dirn in (UP, DOWN, LEFT, RIGHT): 
            i,j = x,y
            while True: 
                i += dirn[0]
                j += dirn[1]
                if i < 0 or j < 0:
                    break
                
                try: 
                    if board[i][j] == '0': 
                        moves.append(piece + RANK[j] + str(i+1))
                    elif piece.isupper():
                        if board[i][j].islower():
                            moves.append(piece+'x'+RANK[j]+str(i+1))
                        break
                    elif piece.islower():
                        if board[i][j].isupper():
                            moves.append(piece+'x'+RANK[j]+str(i+1))
                        break
                except Exception as e: 
                    print(e)
                    break 

    if piece in 'BbQq':
        # build diagonals until collision
        dirns = ((1,1), (-1,-1), (1,-1), (-1,1))
        for dirn in dirns:
            i,j = x,y
            while True: 
                i += dirn[0]
                j += dirn[1]
                if i < 0 or j < 0:
                    break
                
                try: 
                    if board[i][j] == '0': 
                        moves.append(piece + RANK[j] + str(i+1))
                    elif piece.isupper():
                        if board[i][j].islower():
                            moves.append(piece+'x'+RANK[j]+str(i+1))
                        break
                    elif piece.islower():
                        if board[i][j].isupper():
                            moves.append(piece+'x'+RANK[j]+str(i+1))
                        break
                except Exception as e: 
                    print(e)
                    break    

    if piece in 'Kk':
    	dirns = ((1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1), (1,-1), (-1,1))
    	for dirn in dirns: 
    		i,j = x,y
    		while True: 
    			i+=dirn[0]
    			j+=dirn[1]
    			if i < 0 or j <0: 
    				break 

    			try: 
    				if board[i][j] == '0': 
    					moves.append(piece + RANK[j] + str(i+1))
    				elif piece.isuper(): 
    					if board[i][j].islower(): 
    						moves.append(piece+'x'+RANK[j]+str(i+1))
    					break 
    				elif piece.islower(): 
    					if board[i][j].isupper(): 
    						moves.append(piece+'x'+RANK[j]+str(i+1))
    					break 
    			except Exception as e: 
    				print(e) 
    				break

    if piece in 'Nn': 
    	dirns = ((2,1),(1,2),(2,-1),(1,-2),(-1,2),(-2,1),(-1,-2),(-2,-1))
    	while True: 
    			i+=dirn[0]
    			j+=dirn[1]
    			if i < 0 or j <0: 
    				break 
    			try: 
    				if board[i][j] == '0': 
    					moves.append(piece + RANK[j] + str(i+1))
    				elif piece.isuper(): 
    					if board[i][j].islower(): 
    						moves.append(piece+'x'+RANK[j]+str(i+1))
    					break 
    				elif piece.islower(): 
    					if board[i][j].isupper(): 
    						moves.append(piece+'x'+RANK[j]+str(i+1))
    					break 
    			except Exception as e: 
    				print(e) 
    				break
    if piece == 'P': 
    	if x == 1: # first move, double move possible 
    		if board[x+1][y] == '0':
    			moves.append(RANK[y]+str(x+2))
    		if board[x+2][y] == '0':
    			moves.append(RANK[y]+str(x+3))

    	# check for captures 
    	try:
    		if board[x+1][y+1].islower(): 
    			moves.append(RANK[y]+'x'+RANK[y+1]+str[x+2])
    		if board[x+1][y-1].islower(): 
    			moves.append(RANK[y]+'x'+RANK[y-1]+str[x+2])
    	except Exception as e: 
    		print(e)
    	# check for en passant
    	try: 
    		if x == 4: 
    			# if there is an enemy pawn adjacent
    			if board[x][y+1] == 'p': 
    				if lastmove == (RANK[y+1]+'5'): 
    					moves.append(RANK[y]+'x'+RANK[y+1]+str(x+1)+' e.p.')
    			if board[x][y-1] == 'p': 
    				if lastmove == (RANK[y-1]+'5'): 
    					moves.append(RANK[y]+'x'+RANK[y-1]+str(x+1)+' e.p.')
    	except Exception as e: 
    		print(e)


    return moves

def main():
    
    printboard(board)
    print(board[0][0], board[0][1], board[1][0])
    moves = piecelegalmoves(4,4,'f5')
    print(moves)
    print('Rxa7' in moves)


if __name__ == '__main__': 
    main()