import re
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

coordinatesX={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
coordinatesY={1:8,2:7,3:6,4:5,5:4,6:3,7:2,8:1}
def show_board():
    for x in range(10):
        print('   '.join(board[x]),)
    print('\n')
show_board() 

def clearb():
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
def movew(a):
    a=str(a)
    for x in coordinatesX:
        if x ==a.upper()[0]:
            colw=coordinatesX[x]
            roww=int(a[1])
            roww=coordinatesY[roww]
            
    for y in coordinatesX:
        if y ==a.upper()[2]:
            colw1=coordinatesX[y]
            roww1=int(a[3])
            roww1=coordinatesY[roww1]
   
    figw=board[roww].pop(colw)
    board[roww].insert(colw,'□')
    board[roww1][colw1]=figw
    show_board()

def moveb(b):
    b=str(b)
    for x in coordinatesX:
        if x ==b.upper()[0]:
            colb=coordinatesX[x]
            rowb=int(b[1])
            rowb=coordinatesY[rowb]

    for y in coordinatesX:
        if y ==b.upper()[2]:
            colb1=coordinatesX[y]
            rowb1=int(b[3])
            rowb1=coordinatesY[rowb1]
    figb=board[rowb].pop(colb)
    
    board[rowb].insert(colb,'□')
    board[rowb1][colb1]=figb
    show_board()

a=input('WHITE: insert coord for taking and putting figure: (example:c2c4)')
movew(a)
b=input('BLACK: insert coord for taking and putting figure: (example:c2c4)')
moveb(b)
def checkmate():
    if re.search(r'k',board)==False:
        print('WHITE WIN')

checkmate()
# comment from azerin
