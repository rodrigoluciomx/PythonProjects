from Classes import Player
from Classes import Board

def printBoard(r1,r2,r3):
    print(r1)
    print(r2)
    print(r3)


def run():
    welcome = """ 
    Welcome to Tic-tac-toe
    
    This a solo player or 2 players game, please select the mode you want to play by input 
    the corresponding number (1 = Solo player , 2 = Two players):
    
    """

    #In this line, the user choce 
    mode = int(input(welcome))

    Instructions = """
    
    For this terminal game, you will need to enter de number of the box where you want to put your mark, example:

    'Turn of player 1 (x) , select the box = 1 '

    _1_|_2_|_3_
    _4_|_5_|_6_
     7 | 8 | 9

    'Turn of player 1 (o) , select the box = 4 '

     x |_2_|_3_
    _4_|_5_|_6_
     7 | 8 | 9

    'Turn of player 1 (x) , select the box = 1 '

     x |_2_|_3_
     o |_5_|_6_
     7 | 8 | 9

    And so on ...

    The player who will start the game will be choose randomly

    Press 1 to start the game: 
    """
    
    while mode <=0 or mode > 2:
        mode = int(input("Please select a correct value for a mode: "))
    
    if mode == 2:
        Player_1 = Player(input("Ënter the name of the first player: "))

        Player_2 = Player(input("Ënter the name of the second player: "))
        Player_2.actualizarID()

        print("\n"+"Good luck" + "\n")
        Game_board = Board()
        Answer = int(input(Instructions))
        
        while Answer != 1:
            Answer = int(input("Please input the right number: "))

        win = False
        while win is False:
            for turns in range(1,10):
                if turns % 2 != 0:
                    print("It's " + Player_1.Name + " turn.")
                    r1, r2, r3 = Game_board.makeBoard()
                    printBoard(r1, r2, r3)
                    value = Player_1.makeTurn()
                    Game_board.updateTemplate(value," x ")
                    possible_win = Game_board.possibleWin()
                    if possible_win is True:
                        win = True
                        winner = Player_1.Name
                        break
                else:
                    print("It's " + Player_2.Name + " turn.")
                    r1, r2, r3 = Game_board.makeBoard()
                    printBoard(r1, r2, r3)
                    value = Player_2.makeTurn()
                    Game_board.updateTemplate(value," o ")
                    r1, r2, r3 = Game_board.makeBoard()
                    printBoard(r1, r2, r3)
                    possible_win = Game_board.possibleWin()
                    if possible_win is True:
                        win = True
                        winner = Player_2.Name
                        break
                print("\n")
        
        print("\n")
        r1, r2, r3 = Game_board.makeBoard()
        printBoard(r1, r2, r3)
        print("The winner is " + winner)

    else:
        pass


if __name__ == '__main__':
    run()


