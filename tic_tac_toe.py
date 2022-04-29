global board
board=[[" "," "," "],[" "," "," "],[" "," "," "]]
player ="X"

def pinboard(board):
    for line in board:
        print(line)



def makemove():
    global player
    x=int (input("player " +  player  + ",what is x cordinate"))

    y= int(input("y coordinate?"))

    while board[x][y] != " ":
        print("you must choose an empty spot!")
        break

    if player =="X":
        board[x][y]="X"
        player ="0"

    else:
        board[x][y]='0'
        player ="X"

""" did the player that just went ,win?? """

def isWin():
    global player
    if player == "X":
        p="0"
    else:
        p="X"
    #row
    for c in range(len(board)):
        win = True
        for r in range(len(board)):
            if board[c][r] != p:
                win = False
                break
        if win:
            return True    
    #column
    for c in range(len(board)):
            win = True
            for r in range(len(board)):
                if board[r][c] != p:
                    win = False
                    break
            if win:
                return True  


    #diagonals
    win =True
    for c in range(3):
        if board[c][c] != p:
            win = False
            break
    if win:
        return True

    win = True 
    for r in range(len(board)):
        if board[r][len(board)-1-r] != p:
            win = False
            break     
    if win:
        return True
        
    return False    


def main():
    gamewon=False
    while gamewon == False:
        pinboard(board)
        makemove()
        gamewon = isWin()
    print("GAMEOVER")
    pinboard(board)

main()        
