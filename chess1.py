print('\033[1;32;40mHi player, welcome to the CHESS game\nGood luck :)\033[0m\n')

board = [   ['\033[35;1m  ','\u0332A','\u0332B','\u0332C','\u0332D','\u0332E','\u0332F','\u0332G','\u0332H\033[0m'],
            ['8|','r','n','b','q','k','b','n','r','|8'],
            ['7|','p','p','p','p','p','p','p','p','|7'],
            ['6|','□','□','□','□','□','□','□','□','|6'],
            ['5|','□','□','□','□','□','□','□','□','|5'],
            ['4|','□','□','□','□','□','□','□','□','|4'],
            ['3|','□','□','□','□','□','□','□','□','|3'],
            ['2|','P','P','P','P','P','P','P','P','|2'],
            ['1|','R','N','B','Q','K','B','N','R','|1'],
            ['\033[34;1m  ','\u0305A','\u0305B','\u0305C','\u0305D','\u0305E','\u0305F','\u0305G','\u0305H\033[0m']]

# board[row][column]

coordinatesX={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
coordinatesY={1:8,2:7,3:6,4:5,5:4,6:3,7:2,8:1}

def show_board():
    for x in range(10):
        print('   '.join(board[x]),)
    print('\n')

def clear_board():
    global board
    board= [   ['\033[35;1m  ','\u0332H','\u0332G','\u0332F','\u0332E','\u0332D','\u0332C','\u0332B','\u0332A\033[0m'],
            ['8|','r','n','b','q','k','b','n','r','|1'],
            ['7|','p','p','p','p','p','p','p','p','|2'],
            ['6|','□','□','□','□','□','□','□','□','|3'],
            ['5|','□','□','□','□','□','□','□','□','|4'],
            ['4|','□','□','□','□','□','□','□','□','|5'],
            ['3|','□','□','□','□','□','□','□','□','|6'],
            ['2|','P','P','P','P','P','P','P','P','|7'],
            ['1|','R','N','B','Q','K','B','N','R','|8'],
            ['\033[34;1m  ','\u0305A','\u0305B','\u0305C','\u0305D','\u0305E','\u0305F','\u0305G','\u0305H\033[0m']]
    
def movew():
    start = ask_start() # return a list [figure, coordinate]
    ask_end(start, True)
    show_board()

def moveb():
    start = ask_start()
    ask_end(start, False)
    show_board()


def ask_start():
    
    figw = "□"
    while figw == "□":
        a=input('Taking figure coordinate: ') #c2
        # in case user chooses coordinate bigger than board
        while not((a[0].upper() in ['A','B','C','D','E','F','G','H']) and (int(a[1]) in [1,2,3,4,5,6,7,8]) and len(a)== 2):

            print((a[1] in [1,2,3,4,5,6,7,8]))
            print("\033[31;1mthis coordinate doesnt exist, try again\033[0m")
            a=input('Taking figure coordinate: ')

        for x in coordinatesX:
            if x == a.upper()[0]:
                colw=coordinatesX[x]
                roww=int(a[1])
                roww=coordinatesY[roww]
    
        figw = board[roww].pop(colw)
        # print(figw)
        if figw == "□":
            continue

    board[roww].insert(colw,'□') # fill out the cell the piece was taken from
    return [figw,a]

def ask_end(start, white):
    # start[figure, bool]

    # this funct will check is the move is possible for given figure and board
    go = 1
    # if destination is occupied
    while go == 1:
        a = input('Placing coordinates: ')
        # in case user chooses coordinate bigger than board
        print(a.upper())
        while not((a[0].upper() in ['A','B','C','D','E','F','G','H']) and (int(a[1]) in [1,2,3,4,5,6,7,8]) and len(a)== 2):
            print("\033[31;1mthis coordinate doesnt exist, try again\033[0m")
            a=input('Placing coordinate: ')

        for y in coordinatesX:
            if y == a.upper()[0]:
                colw1=coordinatesX[y]
                roww1=int(a[1])
                roww1=coordinatesY[roww1] # traslated this for grid !!!!!!! MY MISTAKEEEE

        if white:                       # figure ,coordinate
            if a.upper() in possible_moves_white(start[0],start[1]) or a.lower() in possible_moves_white(start[0],start[1]):
                board[roww1][colw1]=start[0] # put the figure on the board
                go = 0
                break
            else:
                # move is not possible keep trying
                go=1
                continue

        else: # is black
            if a.upper() in possible_moves_black(start[0],start[1] ) or a.lower() in possible_moves_black(start[0],start[1] ):
                board[roww1][colw1]=start[0] # put the figure on the board
                go = 0
                break
            else:
                # move is not possible keep trying
                go=1
                continue


def possible_moves_white(figure,coordinate):
    # returns a list of all possibles moves for that figure in that position

    if figure.lower() == 'p':
        return possible_pawn(coordinate,True)
    if figure.lower() == 'r':
        return possible_rook(coordinate,True)
    if figure.lower() == 'n':
        return possible_knight(coordinate,True)
    if figure.lower() == 'b':
        return possible_bishop(coordinate,True)
    if figure.lower() == 'q':
        return possible_queen(coordinate,True)
    if figure.lower() == 'k':
        return possible_king(coordinate,True)

def possible_moves_black(figure, coordinate):
    if figure.lower() == 'p':
        return possible_pawn(coordinate,False)
    if figure.lower() == 'r':
        return possible_rook(coordinate,False)
    if figure.lower() == 'n':
        return possible_knight(coordinate,False)
    if figure.lower() == 'b':
        return possible_bishop(coordinate,False)
    if figure.lower() == 'q':
        return possible_queen(coordinate,False)
    if figure.lower() == 'k':
        return possible_king(coordinate,False)


def possible_pawn(coordinate, white):
    # white is boolean variable

    row = int(coordinate[1]) # 2
    row=coordinatesY[row] #7 (index in the grid for second row for the user)
    column = coordinate[0] # c
    column_index = coordinatesX[column.upper()] #3 (a,b,c)

    possible = []

    # white
    if row  == 7 and white and board[6][column_index] == "□" and board[5][column_index] == "□":
        possible.append(column+'4')
        possible.append(column+'3')
    elif row  == 7 and white and board[6][column_index] == "□":
        possible.append(column+'3')

    # black
    if row == 2 and not(white) and board[3][column_index] == "□" and board[4][column_index] == "□":
        possible.append(column+'5')
        possible.append(column+'6')
    elif row == 2 and not(white) and board[3][column_index] == "□":
        possible.append(column+'6')

    
    if (not row == 7) and white and (row - 1) > 0 and board[row-1][column_index] == "□": # basic forward for non row 2 , if not occupied by other or bigger than board
        rown = row - 1
        possible.append(column+str(coordinatesY[rown]))

    if (not row == 2) and not(white) and (row+1) < 9 and board[row+1][column_index] == "□":
        rown = row + 1
        possible.append(column+str(coordinatesY[rown]))

    if white and column_index+1 < 9 and row-1 > 0:
        if (board[row-1][column_index+1].islower()): # there is a BLACK (lower case) figure
            # capturing is happening pawn will take the figure diagonally
            for key, value in coordinatesX.items():
                if value == column_index+1:
                    possible.append(str(key)+str(coordinatesY[row-1]))
    if white and column_index-1 > 0 and row-1 > 0:
        if (board[row-1][column_index-1].islower()):
            for key, value in coordinatesX.items():
                if value == column_index-1:
                    possible.append(str(key)+str(coordinatesY[row-1]))

    if not white and column_index+1 < 9 and row+1 < 9:
        if (board[row+1][column_index+1].isupper()): #id there is a BLACK (lower case) figure
            # capturing is happening pawn will take the figure diagonally
            for key, value in coordinatesX.items():
                if value == column_index+1:
                    possible.append(str(key)+str(coordinatesY[row+1]))
    if not white and column_index-1 > 0 and row+1 < 9:
        if (board[row+1][column_index-1].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index+1:
                    possible.append(str(key)+str(coordinatesY[row+1]))
    # print (possible)
    return possible #[]

def possible_rook(coordinate, white):
    # up +
    # down +
    # left 
    # right

    row = int(coordinate[1]) # 1
    row = coordinatesY[row] # 8
    column = coordinate[0] #a
    column_index = coordinatesX[column.upper()] #1

    possible = []

    # down
    row_down = row+1
    while row_down < 9:
        if board[row_down][column_index] == '□':
            possible.append(column + str(coordinatesY[row_down]))

        if (white and board[row_down][column_index].islower()):
            possible.append(column + str(coordinatesY[row_down]))
            break # cant go over figures
        elif (white and board[row_down][column_index].isupper()):
            # dont append
            break # cant go over your own figures
        
        if (not white and board[row_down][column_index].isupper()):
            possible.append(column + str(coordinatesY[row_down]))
            break
        elif (not white and board[row_down][column_index].islower()):
            # dont append
            break

        row_down += 1 

    # up
    row_up = row - 1
    while row_up > 0:
        if board[row_up][column_index] == "□":
            possible.append(column + str(coordinatesY[row_up]))

        if (white and board[row_up][column_index].islower()):
            possible.append(column + str(coordinatesY[row_up]))
            break # cant go over figures
        elif (white and board[row_up][column_index].isupper()):
            # dont append
            break # cant go over your own figures
        
        if (not white and board[row_up][column_index].isupper()):
            possible.append(column + str(coordinatesY[row_up]))
            break
        elif (not white and board[row_up][column_index].islower()):
            # dont append
            break
        
        row_up -= 1
    
    # left
    column_left = column_index - 1
    while column_left > 0:
        for key, value in coordinatesX.items():
                if value == column_left:
                    column_left_letter = key # find the coorespoding letter for future

        if board[row][column_left] == "□":
            possible.append(column_left_letter + str(coordinatesY[row]))

        if (white and board[row][column_left].islower()):
            possible.append(column_left_letter + str(coordinatesY[row]))
            break # cant go over figures
        elif (white and board[row][column_left].isupper()):
            # dont append
            break # cant go over your own figures
        
        if (not white and board[row][column_left].isupper()):
            possible.append(column_left_letter + str(coordinatesY[row]))
            break
        elif (not white and board[row][column_left].islower()):
            # dont append
            break

        column_left -= 1

    # right
    column_right = column_index + 1
    while column_right < 9:
        # print("here")
        print(column_index)
        for key, value in coordinatesX.items():
            # print("is it")
            if value == column_right:
                column_right_letter = key # find the coorespoding letter for future
                print(column_right_letter)

        if board[row][column_right] == "□":
            possible.append(column_right_letter + str(coordinatesY[row]))

        if (white and board[row][column_right].islower()):
            possible.append(column_right_letter + str(coordinatesY[row]))
            break # cant go over figures
        elif (white and board[row][column_right].isupper()):
            # dont append
            break # cant go over your own figures
        
        if (not white and board[row][column_right].isupper()):
            possible.append(column_right_letter + str(coordinatesY[row]))
            break
        elif (not white and board[row][column_right].islower()):
            # dont append
            break
        column_right += 1

    return possible

def possible_knight(coordinate, white):
    # possible 8 situations
    # up (left, right)
    # down(left, right)
    # right (up, down)
    # left(up, down)

    possible = []

    row = int(coordinate[1]) # 2
    row=coordinatesY[row]
    column = coordinate[0] #c
    column_index = coordinatesX[column.upper()] 

    # down
    if (row + 2) < 9: # within the board
        # right
        if (column_index + 1) < 9 and (board[row+2][column_index+1] == "□"):
            for key, value in coordinatesX.items():
                if value == column_index + 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+2]))
        if white and (column_index + 1) < 9 and (board[row+2][column_index+1].islower()):
            for key, value in coordinatesX.items():
                if value == column_index + 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+2]))
        
        if not white and (column_index + 1) < 9 and (board[row+2][column_index+1].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index + 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+2]))
        
        # left
        if (column_index - 1) > 0 and (board[row+2][column_index-1] == "□"):
            for key, value in coordinatesX.items():
                if value == column_index - 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+2]))
        if white and (column_index - 1) > 0 and (board[row+2][column_index-1].islower()):
            for key, value in coordinatesX.items():
                if value == column_index - 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+2]))
        
        if not white and (column_index - 1) > 0 and (board[row+2][column_index-1].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index - 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+2]))
        

    # up
    if (row-2) > 0:
        # right
        if (column_index + 1) < 9 and (board[row-2][column_index+1] == "□"):
            for key, value in coordinatesX.items():
                if value == column_index + 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-2]))
        if white and (column_index + 1) < 9 and (board[row-2][column_index+1].islower()):
            for key, value in coordinatesX.items():
                if value == column_index + 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-2]))
        
        if not white and (column_index + 1) < 9 and (board[row-2][column_index+1].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index + 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-2]))
        
        # left
        if (column_index - 1) > 0 and (board[row-2][column_index-1] == "□"):
            for key, value in coordinatesX.items():
                if value == column_index - 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-2]))
        if white and (column_index - 1) > 0 and (board[row-2][column_index-1].islower()):
            for key, value in coordinatesX.items():
                if value == column_index - 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-2]))
        
        if not white and (column_index - 1) > 0 and (board[row-2][column_index-1].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index - 1:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-2]))
    
    # right
    if column_index + 2 < 9:
        # up
        if (row+1) < 9 and (board[row+1][column_index+2] == "□"):
            for key, value in coordinatesX.items():
                if value == column_index + 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+1]))
        if white and (row + 1) < 9 and (board[row+1][column_index+2].islower()):
            for key, value in coordinatesX.items():
                if value == column_index + 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+1]))
        
        if not white and (row + 1) < 9 and (board[row+1][column_index+2].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index + 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+1]))
        
        # down
        if (row-1) >0 and (board[row-1][column_index+2] == "□"):
            for key, value in coordinatesX.items():
                if value == column_index + 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-1]))
        if white and (row - 1) > 0 and (board[row-1][column_index+2].islower()):
            for key, value in coordinatesX.items():
                if value == column_index + 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-1]))
        
        if not white and (row - 1) > 0 and (board[row-1][column_index+2].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index + 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-1]))
    
    # left
    if column_index - 2 > 0:
        # up
        if (row+1) < 9 and (board[row+1][column_index-2] == "□"):
            for key, value in coordinatesX.items():
                if value == column_index - 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+1]))
        if white and (row + 1) < 9 and (board[row+1][column_index-2].islower()):
            for key, value in coordinatesX.items():
                if value == column_index - 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+1]))
        
        if not white and (row + 1) < 9 and (board[row+1][column_index-2].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index - 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+1]))
        
        # down
        if (row-1) >0 and (board[row-1][column_index-2] == "□"):
            for key, value in coordinatesX.items():
                if value == column_index - 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-1]))
        if white and (row - 1) > 0 and (board[row-1][column_index-2].islower()):
            for key, value in coordinatesX.items():
                if value == column_index - 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-1]))
        
        if not white and (row - 1) > 0 and (board[row-1][column_index-2].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index - 2:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-1]))

    return possible

def possible_bishop(coordinate, white):
    # 1 2 3 4 chetverti
    possible = []

    row = int(coordinate[1]) # 2
    row=int(coordinatesY[row])
    column = coordinate[0] #c
    column_index = coordinatesX[column.upper()] 

    # 1 
    a = 1
    while True:
        if a == 8:
            break
        if row + a < 9 and column_index + a < 9 and board[row+a][column_index+a] == "□":
            for key, value in coordinatesX.items():
                if value == column_index +a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+a]))

        if white and (column_index + a) < 9 and (row+a < 9) and (board[row+a][column_index+a].islower()):
            for key, value in coordinatesX.items():
                if value == column_index + a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+a]))
            break
        
        if not white and (column_index + a) < 9 and (row+a < 9) and (board[row+a][column_index+a].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index + a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+a]))
            break
        a += 1
    # 2
    a = 1
    while True:
        if a == 8:
            break
        if row + a < 9 and column_index - a > 0 and board[row+a][column_index-a] == "□":
            for key, value in coordinatesX.items():
                if value == column_index - a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+a]))
            

        if white and (column_index - a) > 0 and (row+a < 9) and (board[row+a][column_index-a].islower()):
            for key, value in coordinatesX.items():
                if value == column_index - a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+a]))
            break
        
        if not white and (column_index - a) > 0 and (row+a < 9) and (board[row+a][column_index-a].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index - a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row+a]))
            break
        a += 1
    # 3
    a = 1
    while True:
        if a == 8:
            break
        if row - a > 0 and column_index - a > 0 and board[row-a][column_index-a] == "□":
            for key, value in coordinatesX.items():
                if value == column_index - a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-a]))

        if white and (column_index - a) > 0 and (row-a > 0) and (board[row-a][column_index-a].islower()):
            for key, value in coordinatesX.items():
                if value == column_index - a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-a]))
            break
        
        if not white and (column_index - a) > 0 and (row-a >0) and (board[row-a][column_index-a].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index - a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-a]))
            break   
        a += 1
    
    #4 # column + (row -)
    a = 1
    while True:
        if a == 8:
            break
        if row - a > 0 and column_index + a < 9 and board[row-a][column_index+a] == "□":
            for key, value in coordinatesX.items():
                if value == column_index + a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-a]))

        if white and (column_index + a) < 9 and (row-a > 0) and (board[row-a][column_index+a].islower()):
            for key, value in coordinatesX.items():
                if value == column_index + a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-a]))
            break
        
        if not white and (column_index + a) < 9 and (row-a >0) and (board[row-a][column_index+a].isupper()):
            for key, value in coordinatesX.items():
                if value == column_index + a:
                    column_letter = key
            possible.append(column_letter+str(coordinatesY[row-a]))
            break   
        a += 1
    return possible

def possible_queen(coordinate, white):
    possible = possible_rook(coordinate,white) + possible_bishop(coordinate,white)
    return possible

def possible_king(coordinate, white):
    possible = []

    row = int(coordinate[1]) # 2
    row=coordinatesY[row]
    column = coordinate[0] #c
    column_index = coordinatesX[column.upper()] 

    # 1
    if row + 1 < 9 and ((board[row+1][column_index] == "□") or (white and board[row+1][column_index].islower()) or (not white and board[row+1][column_index].isupper())):
        possible.append(column + str(coordinatesY[row+1]))
    
    # 2
    if row+1 < 9 and column_index + 1 < 9 and ((board[row+1][column_index+1] == "□") or (white and board[row+1][column_index+1].islower()) or (not white and board[row+1][column_index+1].isupper())):
        for key, value in coordinatesX.items():
                if value == column_index + 1:
                    column_letter = key
        possible.append(column_letter + str(coordinatesY[row+1]))
    
    # 3
    if column_index+1 <9 and ((board[row][column_index+1] == "□") or (white and board[row][column_index+1].islower()) or (not white and board[row][column_index+1].isupper())):
        for key, value in coordinatesX.items():
                if value == column_index + 1:
                    column_letter = key
        possible.append(column_letter + str(coordinatesY[row+1]))
    # 4
    if row-1 > 0 and column_index + 1 < 9 and ((board[row-1][column_index+1] == "□") or (white and board[row-1][column_index+1].islower()) or (not white and board[row-1][column_index+1].isupper())):
        for key, value in coordinatesX.items():
                if value == column_index + 1:
                    column_letter = key
        possible.append(column_letter + str(coordinatesY[row-1]))
    #5
    if row-1 > 0 and ((board[row-1][column_index] == "□") or (white and board[row-1][column_index].islower()) or (not white and board[row-1][column_index].isupper())):
        possible.append(column + str(coordinatesY[row-1]))
    # 6
    if row-1 > 0 and column_index - 1 >0 and ((board[row-1][column_index-1] == "□") or (white and board[row-1][column_index-1].islower()) or (not white and board[row-1][column_index-1].isupper())):
        for key, value in coordinatesX.items():
                if value == column_index - 1:
                    column_letter = key
        possible.append(column_letter + str(coordinatesY[row-1]))
    # 7
    if column_index-1 > 0 and ((board[row][column_index-1] == "□") or (white and board[row][column_index-1].islower()) or (not white and board[row][column_index-1].isupper())):
        for key, value in coordinatesX.items():
                if value == column_index - 1:
                    column_letter = key
        possible.append(column_letter + str(coordinatesY[row]))
    # 8
    if row+1 < 9 and column_index - 1 > 0 and ((board[row+1][column_index-1] == "□") or (white and board[row+1][column_index-1].islower()) or (not white and board[row+1][column_index-1].isupper())):
        for key, value in coordinatesX.items():
                if value == column_index - 1:
                    column_letter = key
        possible.append(column_letter + str(coordinatesY[row+1]))

    return possible


def find_king(white, check):
    # if white is true it will find black king
    if white:
        for i in range(1, 9):
            for j in range(1,9):
                if board[i][j] == 'k':
                    king_row_index = i
                    king_column_index = j
                    for key, value in coordinatesX.items():
                        if value == j:
                            column_letter = key
                    king_coordinate = str(column_letter) + str(coordinatesY[i])
                    break
    else:
        for i in range(8, 0,-1):
            for j in range(1,9):
                if board[i][j] == 'K':
                    king_row_index = i
                    king_column_index = j
                    for key, value in coordinatesX.items():
                        if value == j:
                            column_letter = key
                    king_coordinate = str(column_letter) + str(coordinatesY[i])
    if check:
        return [king_row_index, king_column_index]
    else:
        return king_coordinate


def check(white, mate = False,fake_coordinate_x = 0, fake_coordinate_y = 0):
    # lets find the coordinate of the oponent's king
    
    if mate:
        king_row_index = fake_coordinate_x
        king_column_index = fake_coordinate_y
    else:
        king_row_index = find_king(white, True)[0]
        king_column_index = find_king(white, True)[1]

    # pawn attack
    if king_row_index-1 > 0 and king_column_index +1 < 9 :
        if not white and board[king_row_index-1][king_column_index+1] =="p":
            return True
    if king_row_index-1 > 0 and king_column_index +1 < 9 and king_column_index-1 > 0:
        if not white and board[king_row_index-1][king_column_index-1] =="p":
            return True
    
    if king_row_index+1 < 9 and king_column_index +1 < 9:
        if white and board[king_row_index+1][king_column_index+1] =="P":
            return True
    if king_row_index+1 < 9 and king_column_index - 1 > 0:
        if white and board[king_row_index+1][king_column_index-1] =="P":
            return True

    # rook & queen
    # up
    up = king_row_index - 1
    while up > 0:
        if white and (board[up][king_column_index] == 'R' or board[up][king_column_index] == "Q"):
            return True
        if not white and (board[up][king_column_index] == "r" or board[up][king_column_index] == "q"):
            return True
        
        if white and board[up][king_column_index].islower():
            break
        if not white and board[up][king_column_index].isupper():
            break
        up -=1
    # down
    down = king_row_index + 1
    while down < 9:
        if white and (board[down][king_column_index] == 'R' or board[up][king_column_index] == "Q"):
            return True
        if not white and (board[down][king_column_index] == "r" or board[up][king_column_index] == "q"):
            return True
        
        if white and board[down][king_column_index].islower():
            break
        if not white and board[down][king_column_index].isupper():
            break
        down +=1
    # left
    left = king_column_index - 1
    while left > 0:
        if white and (board[king_row_index][left] == 'R' or board[king_row_index][left] == "Q"):
            return True
        if not white and (board[king_row_index][left] == "r" or board[up][left] == "q"):
            return True
        
        if white and board[king_row_index][left].islower():
            break
        if not white and board[king_row_index][left].isupper():
            break
        left -=1
    # right
    right = king_column_index + 1
    while right < 9:
        if white and (board[king_row_index][right] == 'R' or board[king_row_index][right] == "Q"):
            return True
        if not white and (board[king_row_index][right] == 'r' or board[king_row_index][right] == "q"):
            return True
        
        if white and board[king_row_index][right].islower():
            break
        if not white and board[king_row_index][right].isupper():
            break
        right +=1

    
    # bishop and queen
    # 1
    a = 1
    while True:
        if a == 8:
            break
        if white and king_row_index + a < 9 and king_column_index + a < 9 and (board[king_row_index+a][king_column_index+a] == "B" or board[king_row_index+a][king_column_index+a] == "Q"):
            return True
        if white and king_row_index + a < 9 and king_column_index + a < 9 and (board[king_row_index+a][king_column_index+a].islower()):
            break

        if not white and king_row_index + a < 9 and king_column_index + a < 9 and (board[king_row_index+a][king_column_index+a] == "b" or board[king_row_index+a][king_column_index+a] == "q"):
            return True
        if not white and king_row_index + a < 9 and king_column_index + a < 9 and (board[king_row_index+a][king_column_index+a].isupper()):
            break
        a += 1
    # 2
    a = 1
    while True:
        if a == 8:
            break
        if white and king_row_index + a < 9 and king_column_index - a > 0 and (board[king_row_index+a][king_column_index-a] == "B" or board[king_row_index+a][king_column_index-a] == "Q"):
            return True
        if white and king_row_index + a < 9 and king_column_index - a > 0 and (board[king_row_index+a][king_column_index-a].islower()):
            break

        if not white and king_row_index + a < 9 and king_column_index - a > 0 and (board[king_row_index+a][king_column_index-a] == "b" or board[king_row_index+a][king_column_index-a] == "q"):
            return True
        if not  white and king_row_index + a < 9 and king_column_index - a > 0 and (board[king_row_index+a][king_column_index-a].isupper()):
            break
        a += 1
    # 3
    a = 1
    while True:
        if a == 8:
            break
        if white and king_row_index - a > 0 and king_column_index - a > 0 and (board[king_row_index-a][king_column_index-a] == "B" or board[king_row_index-a][king_column_index-a] == "Q"):
            return True
        if white and king_row_index - a > 0 and king_column_index - a > 0 and (board[king_row_index-a][king_column_index-a].islower()):
            break

        if not white and king_row_index - a > 0 and king_column_index - a > 0 and (board[king_row_index-a][king_column_index-a] == "b" or board[king_row_index-a][king_column_index-a] == "q"):
            return True
        if not  white and king_row_index - a > 0 and king_column_index - a > 0 and (board[king_row_index-a][king_column_index-a].isupper()):
            break
        a += 1

    # 4
    a = 1
    while True:
        if a == 8:
            break
        if white and king_row_index - a > 0 and king_column_index + a < 9 and (board[king_row_index-a][king_column_index+a] == "B" or board[king_row_index-a][king_column_index-a] == "Q"):
            return True
        if white and king_row_index - a > 0 and king_column_index + a < 9 and (board[king_row_index-a][king_column_index+a].islower()):
            break

        if not white and king_row_index - a > 0 and king_column_index + a < 9 and (board[king_row_index-a][king_column_index+a] == "b" or board[king_row_index-a][king_column_index-a] == "q"):
            return True
        if not  white and king_row_index - a > 0 and king_column_index + a < 9 and (board[king_row_index-a][king_column_index+a].isupper()):
            break
        a += 1


    # knight
    if white and king_row_index - 2 > 0 and king_column_index + 1 < 9 and board[king_row_index - 2][king_column_index + 1] =='N':
        return True
    if not white and king_row_index - 2 > 0 and king_column_index + 1 < 9 and board[king_row_index - 2][king_column_index + 1] =='n':
        return True
    
    if white and king_row_index - 1 > 0 and king_column_index + 2 < 9 and board[king_row_index - 1][king_column_index + 2] =='N':
        return True
    if not white and king_row_index - 1 > 0 and king_column_index + 2 < 9 and board[king_row_index - 1][king_column_index + 2] =='n':
        return True
    
    if white and king_row_index + 1 < 9 and king_column_index + 2 < 9 and board[king_row_index + 1][king_column_index + 2] =='N':
        return True
    if not white and king_row_index + 1 < 9 and king_column_index + 2 < 9 and board[king_row_index + 1][king_column_index + 2] =='n':
        return True
    
    if white and king_row_index + 2 < 9 and king_column_index + 1 < 9 and board[king_row_index + 2][king_column_index + 1] =='N':
        return True
    if not white and king_row_index + 2 < 9 and king_column_index + 1 < 9 and board[king_row_index + 2][king_column_index + 1] =='n':
        return True
    
    if white and king_row_index + 2 < 9 and king_column_index - 1 > 0 and board[king_row_index + 2][king_column_index - 1] =='N':
        return True
    if not white and king_row_index + 2 < 9 and king_column_index - 1 > 0 and board[king_row_index + 2][king_column_index - 1] =='n':
        return True
    
    if white and king_row_index + 1 < 9 and king_column_index - 2 > 0 and board[king_row_index + 1][king_column_index - 2] =='N':
        return True
    if not white and king_row_index + 1 < 9 and king_column_index - 2 > 0 and board[king_row_index + 1][king_column_index - 2] =='n':
        return True
    
    if white and king_row_index - 1 > 0 and king_column_index - 2 > 0 and board[king_row_index - 1][king_column_index - 2] =='N':
        return True
    if not white and king_row_index - 1 > 0 and king_column_index - 2 > 0 and board[king_row_index - 1][king_column_index - 2] =='n':
        return True
    
    if white and king_row_index - 2 > 0 and king_column_index - 1 > 0 and board[king_row_index - 2][king_column_index - 1] =='N':
        return True
    if not white and king_row_index - 2 > 0 and king_column_index - 1 > 0 and board[king_row_index - 2][king_column_index - 1] =='n':
        return True

    return False


def check_mate(white):
    # for every move of black check sitiation appears
    # we can create a fake board for each situation BUT
    # lets find the coordinate of the oponent's king

    king_coordinate = find_king(white, False)

    all = possible_king(king_coordinate, not white)
    counter = 0

    for i in all:
        # print(i)
        row = int(i[1])
        fake_coodinate_y = coordinatesX[i[0].upper()]
        fake_coodinate_x = coordinatesY[row]
        if check(white, True, fake_coodinate_x, fake_coodinate_y):
            counter += 1
    if counter == len(all):
        return True
    
    return False



def game():
    while True:
        show_board()
        print("\033[34;1mwhite's move\033[0m")
        movew()
        if check(True):
            print("\033[31;1mCheck\033[0m")
            if check_mate(True):
                print("\033[31;1mgame over\033[0m")
                return True
        
        print("\033[35;1mblack's move\033[0m")
        moveb()
        if check(False):
            print("\033[31;1mCheck\033[0m")
            if check_mate(False):
                print("\033[31;1mGame over\033[0m")
                return True


while True: # Until user decides not to play again
    game()
    again = input("want to play again?: (Y/N)")
    if again.lower() == 'y':
        clear_board()
        continue
    else:
        print("\033[32;1mthanks for playing, see you again!\033[0m")
        break
