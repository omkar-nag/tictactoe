import os,time,sys,json,shutil

from source import actions,result,terminal,utility,initial_state
from minimax import minimax
from view import display_board

def MainGame():
    os.system('cls' if os.name == 'nt' else 'clear')
    board = initial_state()
    s = "TIC TAC TOE"

    print(s.center(shutil.get_terminal_size().columns))
    print("")
    print('Choose X or O: '.center(shutil.get_terminal_size().columns))

    player = input().capitalize()

    print("")

    while player != 'X' and player!='O':
        print('Enter a valid character'.center(shutil.get_terminal_size().columns))
        player = input().capitalize()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(s.center(shutil.get_terminal_size().columns))
    print("\n")

    print('Use this as a guide to the board:'.center(shutil.get_terminal_size().columns))
    print(display_board(board,True))

    ai_turn = False 
    if player == 'O':
        ai_turn = True
    tiles = {1:(0,0) , 2:(0,1) , 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    tiles2 = {(0,0):1 , (0,1):2 , (0,2):3, (1,0):4, (1,1):5, (1,2):6, (2,0):7, (2,1):8, (2,2):9}
    
    while not terminal(board):
        if ai_turn:
            
            print('AI is making its move...'.center(shutil.get_terminal_size().columns))
            print('')
            time.sleep(3)
            ai_action = minimax(board)
            board = result(board,ai_action)
            ai_turn = False
        else:
            while True:
                print('Insert a value between 1-9: '.center(shutil.get_terminal_size().columns),end="")
                while True:
                    try:
                        player_action = int(input())
                        print("")
                        break
                    except:
                        print('Please enter an integer value'.center(shutil.get_terminal_size().columns))
                

                possible_actions = actions(board)
                try: 
                    board = result(board,tiles[player_action])
                    ai_turn = True
                    break
                except Exception:
                    x=[]
                    for i in possible_actions:
                        x.append(tiles2[i])
                    print('Invalid move! Your possible moves are:'.center(shutil.get_terminal_size().columns))
                    
                    print(json.dumps(sorted(x)).center(shutil.get_terminal_size().columns))
                    print("")
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print(s.center(shutil.get_terminal_size().columns))
        print("\n")
        print("Guide".center(shutil.get_terminal_size().columns))
        print(display_board(board,True))
        print(display_board(board,False))

    if utility(board)==1:
        if player == 'X':
            print('Congratulations, you win!'.center(shutil.get_terminal_size().columns))
        else:
            print('Sorry, you lose!'.center(shutil.get_terminal_size().columns))
    elif utility(board)==-1:
        if player == 'O':
            print('Congratulations, you win!'.center(shutil.get_terminal_size().columns))
        else:
            print('Sorry, you lose!'.center(shutil.get_terminal_size().columns))
    else:
        print('The game ended in a draw!'.center(shutil.get_terminal_size().columns)) 
    

    print('Would you like to play again? (Y/N)'.center(shutil.get_terminal_size().columns))
    play_again = input().lower()
    if play_again == 'y':
        MainGame()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n')
        print('Thank you for playing!'.center(shutil.get_terminal_size().columns))
        sys.exit()