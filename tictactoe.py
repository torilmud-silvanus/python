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
    print '////////////////////////////////////////////////////'
    print '// Game: Tic Tac Toe'
    print '/////////////////////////'
    print '                       // Player X: ',user_x
    print '                       // Player O: ',user_o
    print '                       /////////////////////////////'
    print '     ',currentboard['square_1'],'|',currentboard['square_2'],'|',currentboard['square_3']
    print '     -----------'
    print '     ',currentboard['square_4'],'|',currentboard['square_5'],'|',currentboard['square_6']
    print '     -----------'
    print '     ',currentboard['square_7'],'|',currentboard['square_8'],'|',currentboard['square_9']
    print '               '
    print '               '
    print '               '
    print '////////////////////////////////////////////////////'
    
def move_select(user):
    move = None

    # Set whether this move is going to be an X or an O based on the current user
    if user == user_x:
        mark = 'X'
    elif user == user_o:
        mark = 'O'

    # USER MOVE: User inputs what square they want to mark
    print '',user,'which square would you like to mark with an',mark,'?'
    try:
        move = int(raw_input(':'))
    # Validation
    except:
        print ' VALIDATION ERROR: That is not a valid selection!'
        move_select(user)
            
    # Mark the square chosen  
    for key, val in currentboard.iteritems():
        if val.isdigit():
            if int(val) == int(move):
                currentboard[key] = mark
                print ' Marking Square',move,'with an',mark,'for',user
                break
            else:
                continue
        else:
            continue
    else:
        print ' VALIDATION ERROR: That square has already been used.'
        move_select(user)
        
    # After marking the square, reprint the board so the user can see the mark
    gameboard()
    
    # Check Game Over scenarios before handing off to the next player
    if checkwin():
        print ' *****************************'
        print ' * GAME OVER!'
        print ' *',user,'WINS!'
        print ' *****************************'
        return True
    elif checkstalemate():
        print ' *****************************'
        print ' * STALEMATE! EVERYONE LOSES!'
        print ' * NO MORE MOVES AVAILABLE'
        print ' *****************************'
        return True
    else:    
        # If the game hasn't been won, then give the other player a turn
        if user == user_x:
            move_select(user_o)
        else:
            move_select(user_x)

def checkwin():
    # Check the board for win scenarios
    # 123
    if currentboard['square_1'] == 'X' and currentboard['square_2'] == 'X' and currentboard['square_3'] == 'X':
        return True
    if currentboard['square_1'] == 'O' and currentboard['square_2'] == 'O' and currentboard['square_3'] == 'O':
        return True
    # 456
    if currentboard['square_4'] == 'X' and currentboard['square_5'] == 'X' and currentboard['square_6'] == 'X':
        return True
    if currentboard['square_4'] == 'O' and currentboard['square_5'] == 'O' and currentboard['square_6'] == 'O':
        return True
    # 789
    if currentboard['square_7'] == 'X' and currentboard['square_8'] == 'X' and currentboard['square_9'] == 'X':
        return True
    if currentboard['square_7'] == 'O' and currentboard['square_8'] == 'O' and currentboard['square_9'] == 'O':
        return True
    # 147
    if currentboard['square_1'] == 'X' and currentboard['square_4'] == 'X' and currentboard['square_7'] == 'X':
        return True
    if currentboard['square_1'] == 'O' and currentboard['square_4'] == 'O' and currentboard['square_7'] == 'O':
        return True
    # 258
    if currentboard['square_2'] == 'X' and currentboard['square_5'] == 'X' and currentboard['square_8'] == 'X':
        return True
    if currentboard['square_2'] == 'O' and currentboard['square_5'] == 'O' and currentboard['square_8'] == 'O':
        return True
    # 369
    if currentboard['square_3'] == 'X' and currentboard['square_6'] == 'X' and currentboard['square_9'] == 'X':
        return True
    if currentboard['square_3'] == 'O' and currentboard['square_6'] == 'O' and currentboard['square_9'] == 'O':
        return True
    # 159
    if currentboard['square_1'] == 'X' and currentboard['square_5'] == 'X' and currentboard['square_9'] == 'X':
        return True
    if currentboard['square_1'] == 'O' and currentboard['square_5'] == 'O' and currentboard['square_9'] == 'O':
        return True
    # 357
    if currentboard['square_3'] == 'X' and currentboard['square_5'] == 'X' and currentboard['square_7'] == 'X':
        return True
    if currentboard['square_3'] == 'O' and currentboard['square_5'] == 'O' and currentboard['square_7'] == 'O':
        return True

def checkstalemate():
    # STALEMATE: Wow they suck at this game
    boardvalues = currentboard.values()
    for x in boardvalues:
        if x.isdigit():
            break
    else:
        return True

# Launch
tictactoe()
