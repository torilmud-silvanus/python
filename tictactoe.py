from IPython.display import clear_output

# Globals' Starting Position
def newgame():
    # The board squares are filled with numbers to label the squares until they are marked during gameplay
    global currentboard
    currentboard = {'square_1':'1','square_2':'2','square_3':'3','square_4':'4','square_5':'5','square_6':'6','square_7':'7','square_8':'8','square_9':'9'}
    
    # Player identities
    global user_x
    global user_o
    user_x = None
    user_o = None
    
    # Number of players
    global usercount
    usercount = 0

    # Defining input choices
    # use lower() when matching input to choices
    global yes
    global no
    yes = ('yes', 'y', 'sure', 'ok', 'okay', 'yep', 'yup', 'ya', 'agree', 'accept')
    no = ('no', 'n', 'nah', 'naw', 'nope', 'disagree', 'decline')
    
def tictactoe():
    # This function controls navigation flow for the game from a high level
    
    # Game setup 
    newgame()
    gameboard()
    welcome('Tic Tac Toe')
    login()

    # Game board
    gameboard()

    # Game play
    move_select(user_x)

def validation(error):
    # this function handles the message display for validation errors
    # this function lets us unify message styling
    print ' '
    print ' VALIDATION ERROR:',error
    print ' '

def confirm():
    # This function is versatile and can be used to prompt the user to confirm any selection
    print 'Are you sure?'
    try:
        confirm = str(raw_input(':')).lower()
        if confirm in yes:
            return True
        elif confirm in no:
            return False
        else:
            validation('To accept, the choices are',yes)
            validation('To decline, the choices are',no)
            confirm()
    except:
        validation('To accept, the choices are',yes)
        validation('To decline, the choices are',no)
        confirm()


def welcome(game):
    print ' '
    print ' Welcome to the game',game
    print ' '

def login():
    global usercount
    global user_x
    global user_o
    
    if usercount == 0:
        try:
            print ' How many players?'
            usercount = int(raw_input(':'))
        except ValueError:
            validation('That is not a valid selection. Try a number!')
            login()
    if usercount == 1:
        print ' Just you eh? Fine, I will play against you.'
        print ' What is your name?'
        user1 = str(raw_input(':'))
        try:
            print' Do you want to be X or O?'
            user1_mark = str(raw_input(':')).upper()
            if user1_mark == 'X':
                user_x = user1
                user_o = 'Computer'
            elif user1_mark == 'O':
                user_o = user1
                user_x = 'Computer'
            else:
                login()
        except:
            validation('You can only choose X or O')
            login()
    elif usercount == 2:
        if user_x is None:
            print ' Who wants to be X?'
            user_x = raw_input(':')
        if user_o is None:
            print ' Who wants to be O?'
            user_o = raw_input(':')
    else:
        validation('That is not a valid selection. This game can only be played with 1 or 2 players.')
        usercount = 0
        login()

def gameboard():
    # Always clear the screen before rendering the game board
    clear_output()

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
    print ' '
    
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
            validation('That is not a valid selection. Try again!')
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
        validation('That square has already been used.')
        move_select(user)
        
    # After marking the square, reprint the board so the user can see the mark
    gameboard()
    
    # Check Game Over scenarios before handing off to the next player
    checkgameover()

    # If the game hasn't been won, then give the other player a turn
    if user == user_x:
        move_select(user_o)
    else:
        move_select(user_x)

def checkwin():
    # Check the board for win scenarios
    # 123.
    # This only checks for wins, to check for all gameover scenarios use checkgameover()
    if currentboard['square_1'] == 'X' and currentboard['square_2'] == 'X' and currentboard['square_3'] == 'X':
        win(user_x)
    if currentboard['square_1'] == 'O' and currentboard['square_2'] == 'O' and currentboard['square_3'] == 'O':
        win(user_o)
    # 456
    if currentboard['square_4'] == 'X' and currentboard['square_5'] == 'X' and currentboard['square_6'] == 'X':
        win(user_x)
    if currentboard['square_4'] == 'O' and currentboard['square_5'] == 'O' and currentboard['square_6'] == 'O':
        win(user_o)
    # 789
    if currentboard['square_7'] == 'X' and currentboard['square_8'] == 'X' and currentboard['square_9'] == 'X':
        win(user_x)
    if currentboard['square_7'] == 'O' and currentboard['square_8'] == 'O' and currentboard['square_9'] == 'O':
        win(user_o)
    # 147
    if currentboard['square_1'] == 'X' and currentboard['square_4'] == 'X' and currentboard['square_7'] == 'X':
        win(user_x)
    if currentboard['square_1'] == 'O' and currentboard['square_4'] == 'O' and currentboard['square_7'] == 'O':
        win(user_o)
    # 258
    if currentboard['square_2'] == 'X' and currentboard['square_5'] == 'X' and currentboard['square_8'] == 'X':
        win(user_x)
    if currentboard['square_2'] == 'O' and currentboard['square_5'] == 'O' and currentboard['square_8'] == 'O':
        win(user_o)
    # 369
    if currentboard['square_3'] == 'X' and currentboard['square_6'] == 'X' and currentboard['square_9'] == 'X':
        win(user_x)
    if currentboard['square_3'] == 'O' and currentboard['square_6'] == 'O' and currentboard['square_9'] == 'O':
        win(user_o)
    # 159
    if currentboard['square_1'] == 'X' and currentboard['square_5'] == 'X' and currentboard['square_9'] == 'X':
        win(user_x)
    if currentboard['square_1'] == 'O' and currentboard['square_5'] == 'O' and currentboard['square_9'] == 'O':
        win(user_o)
    # 357
    if currentboard['square_3'] == 'X' and currentboard['square_5'] == 'X' and currentboard['square_7'] == 'X':
        win(user_x)
    if currentboard['square_3'] == 'O' and currentboard['square_5'] == 'O' and currentboard['square_7'] == 'O':
        win(user_o)

def win(winner):
    print ' *****************************'
    print ' * GAME OVER!'
    print ' *',winner,'WINS!'
    print ' *****************************'
    playagain()

def checkstalemate():
    # STALEMATE: Wow they suck at this game
    boardvalues = currentboard.values()
    for x in boardvalues:
        if x.isdigit():
            break
    else:
        print ' *****************************'
        print ' * STALEMATE! EVERYONE LOSES!'
        print ' * NO MORE MOVES AVAILABLE'
        print ' *****************************'
        playagain()

def playagain():
    try:
        print 'Would you like to play again?'
        choice = str(raw_input(':')).lower()
        if choice in yes:
            tictactoe()
        elif choice in no:
            endgame()
        else:
            print 'Please choose y or n'
            playagain()
    except:
        validation('Please choose y or n')
        playagain()

def checkgameover():
    if checkwin(): return True
    if checkstalemate(): return True

# this function needs to be the last function listed because i don't know how to quit properly
def endgame():
    try:
        print 'Are you sure you want to quit the game?'
        quit = str(raw_input(':')).lower()
        if quit in yes:
            if confirm:
                print 'K, BYE!'
                import sys
                sys.exit(0)
                return True
            else:
                endgame()
        elif quit in no:
            playagain()
        else:
            validation('To accept, the choices are',yes)
            validation('To decline, the choices are',no)
            endgame()
    except:
        validation('Please choose y or n')
        endgame()

# Launch
tictactoe()