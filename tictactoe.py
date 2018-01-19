currentboard = {'square_1':'1','square_2':'2','square_3':'3','square_4':'4','square_5':'5','square_6':'6','square_7':'7','square_8':'8','square_9':'9'}

def tictactoe():
    login()
    gameboard()
    move_select(user_x)

def login():
    global user_x
    user_x = None
    global user_o
    user_o = None
    
    if user_x is None:
        user_x = raw_input('Who wants to be X: ')
    
    if user_o is None:
        user_o = raw_input('Who wants to be O: ')

def gameboard():
    # Display the board
    
    print 'Game: Tic Tac Toe'
    print '                       Player X: ',user_x
    print '                       Player O: ',user_o
    print '               '
    print '     ',currentboard['square_1'],'|',currentboard['square_2'],'|',currentboard['square_3']
    print '     -----------'
    print '     ',currentboard['square_4'],'|',currentboard['square_5'],'|',currentboard['square_6']
    print '     -----------'
    print '     ',currentboard['square_7'],'|',currentboard['square_8'],'|',currentboard['square_9']
    print '               '
    
def move_select(user):
    # User prompted for text input
    # TBC: need to handle text input vs raw_input strings
    move = None

    # Set whether this move is going to be an X or an O based on the current user
    if user == user_x:
        mark = 'X'
    elif user == user_o:
        mark = 'O'

    # User inputs what square they want to mark
    print user,'which square would you like to mark with an',mark
    try:
        move = int(raw_input(':'))
    # Validation
    except:
        print 'VALIDATION ERROR: That is not a valid selection!'
        move_select(user)
            
    # Mark the square
    if move == 1:
        if currentboard['square_1'] != '1':
            print 'Sorry that square has already been marked, try another one!'
            move_select(user)
        else:
            currentboard['square_1'] = mark
            print 'Marking Square',move,'with an',mark,'for',user
    elif move == 2:
        if currentboard['square_2'] != '2':
            print 'Sorry that square has already been marked, try another one!'
            move_select(user)
        else:
            currentboard['square_2'] = mark
            print 'Marking Square',move,'with an',mark,'for',user
    elif move == 3:
        if currentboard['square_3'] != '3':
            print 'Sorry that square has already been marked, try another one!'
            move_select(user)
        else:
            currentboard['square_3'] = mark
            print 'Marking Square',move,'with an',mark,'for',user
    elif move == 4:
        if currentboard['square_4'] != '4':
            print 'Sorry that square has already been marked, try another one!'
            move_select(user)
        else:
            currentboard['square_4'] = mark
            print 'Marking Square',move,'with an',mark,'for',user
    elif move == 5:
        if currentboard['square_5'] != '5':
            print 'Sorry that square has already been marked, try another one!'
            move_select(user)
        else:
            currentboard['square_5'] = mark
            print 'Marking Square',move,'with an',mark,'for',user
    elif move == 6:
        if currentboard['square_6'] != '6':
            print 'Sorry that square has already been marked, try another one!'
            move_select(user)
        else:
            currentboard['square_6'] = mark
            print 'Marking Square',move,'with an',mark,'for',user
    elif move == 7:
        if currentboard['square_7'] != '7':
            print 'Sorry that square has already been marked, try another one!'
            move_select(user)
        else:
            currentboard['square_7'] = mark
            print 'Marking Square',move,'with an',mark,'for',user
    elif move == 8:
        if currentboard['square_8'] != '8':
            print 'Sorry that square has already been marked, try another one!'
            move_select(user)
        else:
            currentboard['square_8'] = mark
            print 'Marking Square',move,'with an',mark,'for',user
    elif move == 9:
        if currentboard['square_9'] != '9':
            print 'Sorry that square has already been marked, try another one!'
            move_select(user)
        else:
            currentboard['square_9'] = mark
            print 'Marking Square',move,'with an',mark,'for',user
    else:
        print 'VALIDATION ERROR: That is not a valid selection!'
        move_select(user)
    
    # After marking the square, reprint the board and give the other player a turn
    gameboard()
    
    # Add a check here to see if this was the winning move
    
    # If the game hasn't been won, then give the other player a turn
    if user == user_x:
        move_select(user_o)
    else:
        move_select(user_x)

# Launch
tictactoe()