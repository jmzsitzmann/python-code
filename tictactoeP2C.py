import os
os.system('clear') # Clears terminal window

class Board:
    '''Create a tic tac toe board.'''
    def __init__(self):
        '''Zero in the list is just a place holder so that indexing matches the value in the list.'''
        self.myboard = [0,1,2,3,4,5,6,7,8,9]
        
    def display(self):
        '''Prints board'''
        print(" %s | %s | %s " %(self.myboard[1], self.myboard[2], self.myboard[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.myboard[4], self.myboard[5], self.myboard[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.myboard[7], self.myboard[8], self.myboard[9]))

    def Update_board1(self, symbol):
        while True:
            options = [1,2,3,4,5,6,7,8,9]
            player1_move = input('Enter a number to move.')
            if player1_move.isalpha():
                'That is not a valid move. Please enter a number 1 through 9.'
            
            
            
            elif int(player1_move) not in options:
                player1_move = int(player1_move)
                print("That key is not on the board. Please try again.")
                
            else:
                player1_move = int(player1_move)
                if self.myboard[player1_move] != 'X' and self.myboard[player1_move] != 'O':
                    self.myboard[player1_move] = symbol
                    break
                    
                else:
                    print("That spot is taken. Please try again.")
        
    def Update_board2(self, symbol):
        while True:
        
            options = [1,2,3,4,5,6,7,8,9]
            player2_move = int(input('Enter a number to move.'))
            if player2_move not in options:
                print("That key is not on the board. Please try again.")
            else:
                if self.myboard[player2_move] != 'X' and self.myboard[player2_move] != 'O':
                    self.myboard[player2_move] = symbol
                    break
                    
                else:
                    print("That spot is taken. Please try again.")
    
    def isTie(self):
        count = 0
        for i in self.myboard:
            if i == 'X' or i == 'O':
                count += 1
        if count == 9:
            return True 
        
    def Check_board(self, symbol):
        for check in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
            result = True
            for win in check:
                if self.myboard[win] != symbol:
                    result = False
            if result == True:
                return True
        return False

        
class Move:
    
    def __init__(self, grid):
        self.grid = grid
        self.makeMove('X')
            
    def makeMove(self, playerTag):
        self.grid.display() 
        while True: 
            options = [1,2,3,4,5,6,7,8,9]
            
            
            move = input("What move would you like to make player %s? Choose a number 1 through 9." %(playerTag))
            if move.isalpha():
                print('That is not a valid entry. Please enter a number 1 through 9.')
            
            elif int(move) not in options:
                move = int(move)
                print("That key is not on the board. Please try again.")
            else:
                move = int(move)
                if self.grid.myboard[move] != 'X':
                    self.grid.myboard[move] = 'X'
                    os.system('clear')
                    
                    break
                
                else:
                    print("That spot is taken. Please try again.")

class Game:
    
    def __init__(self, grid):
        self.grid = grid
        self.greeting(self.grid)
        
    def greeting(self, grid):
        '''Clear window, print greeting and display board. Takes a list as argument.'''
        os.system('clear')
        print("Welcome to Tic Tac Toe!!!")
        self.grid.display()

        
    def play(self):
    
        self.greeting(self.grid)
        while True:
        
            self.grid.Update_board1('X')
            self.greeting(self.grid)
            if self.grid.Check_board('X'):
                print('X wins!! Game over.')
                break
            
            if self.grid.isTie():
                print("Game over. It's a cats game!")
                break
            
            self.grid.Update_board2('O')
            self.greeting(self.grid)
            if self.grid.Check_board('O'):
                print('O wins!! Game over.')
                break
            if self.grid.isTie():
                print("Game over. It's a cats game!")
                break
        
class compMove:
    
    def __init__(self, grid, player1move):
        self.grid = grid
        self.player1move = player1move
    
    def response(self):
        while True:
            if self.grid.myboard[5] == 5:
                self.grid.myboard[5] = 'Y'
                self.player1move.makeMove('X')
                
                if self.grid.myboard[1] == 'X' and self.grid.myboard[7] == 'X':
                    self.grid.myboard[4] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[6] != 'X':
                        self.grid.myboard[6] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[8] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[2] != 'X':
                            self.grid.myboard[2] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[3] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                            
                            
                
                elif self.grid.myboard[1] == 'X' and self.grid.myboard[3] == 'X':
                    self.grid.myboard[2] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[8] != 'X':
                        self.grid.myboard[8] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[4] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[6] != 'X':
                            self.grid.myboard[6] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[9] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                            
                    
                elif self.grid.myboard[3] == 'X' and self.grid.myboard[9] == 'X':
                    self.grid.myboard[6] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[4] != 'X':
                        self.grid.myboard[4] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[8] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[2] != 'X':
                            self.grid.myboard[2] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[1] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                
                elif self.grid.myboard[7] == 'X' and self.grid.myboard[9] == 'X':
                    self.grid.myboard[8] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[2] != 'X':
                        self.grid.myboard[2] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[4] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[6] != 'X':
                            self.grid.myboard[6] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[3] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                    
                elif self.grid.myboard[1] == 'X' and self.grid.myboard[2] == 'X':
                    self.grid.myboard[3] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[7] != 'X':
                        self.grid.myboard[7] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[4] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[6] != 'X':
                            self.grid.myboard[6] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[9] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                
                elif self.grid.myboard[2] == 'X' and self.grid.myboard[3] == 'X':
                    self.grid.myboard[1] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[9] != 'X':
                        self.grid.myboard[9] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[6] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[4] != 'X':
                            self.grid.myboard[4] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[8] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                
                elif self.grid.myboard[1] == 'X' and self.grid.myboard[4] == 'X':
                    self.grid.myboard[7] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[3] != 'X':
                        self.grid.myboard[3] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[2] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[8] != 'X':
                            self.grid.myboard[8] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[9] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                    
                elif self.grid.myboard[3] == 'X' and self.grid.myboard[6] == 'X':
                    self.grid.myboard[9] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[1] != 'X':
                        self.grid.myboard[1] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[2] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[8] != 'X':
                            self.grid.myboard[8] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[7] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                
                elif self.grid.myboard[6] == 'X' and self.grid.myboard[9] == 'X':
                    self.grid.myboard[3] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[7] != 'X':
                        self.grid.myboard[7] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[8] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[2] != 'X':
                            self.grid.myboard[2] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[4] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                
                elif self.grid.myboard[7] == 'X' and self.grid.myboard[8] == 'X':
                    self.grid.myboard[9] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[1] != 'X':
                        self.grid.myboard[1] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[4] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[6] != 'X':
                            self.grid.myboard[6] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[2] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                
                elif self.grid.myboard[8] == 'X' and self.grid.myboard[9] == 'X':
                    self.grid.myboard[7] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[3] != 'X':
                        self.grid.myboard[3] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[6] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[4] != 'X':
                            self.grid.myboard[4] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[2] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                
                elif self.grid.myboard[4] == 'X' and self.grid.myboard[7] == 'X':
                    self.grid.myboard[1] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[9] != 'X':
                        self.grid.myboard[9] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[8] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[2] != 'X':
                            self.grid.myboard[2] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[3] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break

                elif self.grid.myboard[1] == 'X' and self.grid.myboard[9] == 'X':
                    self.grid.myboard[2] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[8] != 'X':
                        self.grid.myboard[8] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[7] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[3] == 'X':
                            self.grid.myboard[6] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                            
                        elif self.grid.myboard[6] == 'X':
                            self.grid.myboard[3] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                            
                elif self.grid.myboard[3] == 'X' and self.grid.myboard[7] == 'X':
                    self.grid.myboard[1] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[9] != 'X':
                        self.grid.myboard[9] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                        
                    else:
                        self.grid.myboard[8] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[2] != 'X':
                            self.grid.myboard[2] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        elif self.grid.myboard[2] == 'X':
                            self.grid.myboard[6] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                        
                
                
            elif self.grid.myboard[1] != 'X':
                self.grid.myboard[1] = 'Y'
                self.player1move.makeMove('X')
                
                if self.grid.myboard[4] == 'X':
                    self.grid.myboard[6] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[3] == 'X':
                        self.grid.myboard[7] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[2] != 'X':
                            self.grid.myboard[2] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                        
                        else:
                            self.grid.myboard[8] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                        
                    elif self.grid.myboard[7] == 'X':
                        self.grid.myboard[3] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[9] != 'X':
                            self.grid.myboard[9] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                        
                        elif self.grid.myboard[2] != 'Y':
                            self.grid.myboard[2] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                        
                        else:
                            self.grid.myboard[9] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                        
                    elif self.grid.myboard[2] == 'X':
                        self.grid.myboard[8] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[3] == 'X':
                            self.grid.myboard[9] = 'Y'
                            print("Cats game! Game over.")
                            break
                            
                        else:
                            self.grid.myboard[3] = 'Y'
                            print("Cats game! Game over.")
                            break
                        
                    elif self.grid.myboard[8] == 'X':
                        self.grid.myboard[9] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[3] != 'X':
                            self.grid.myboard[3] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                        
                        else:
                            self.grid.myboard[2] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                        
                    elif self.grid.myboard[9] == 'X':
                        self.grid.myboard[3] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[2] != 'X':
                            self.grid.myboard[2] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                        
                        else:
                            self.grid.myboard[8] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                        
                        
                elif self.grid.myboard[7] =='X':
                    self.grid.myboard[3] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[2] != 'X':
                        self.grid.myboard[2] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                    
                    else:
                        self.grid.myboard[6] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[9] != 'X':
                            self.grid.myboard[9] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                        
                        else:
                            self.grid.myboard[8] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break

                elif self.grid.myboard[3] =='X':
                    self.grid.myboard[7] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[4] != 'X':
                        self.grid.myboard[4] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                    
                    else:
                        self.grid.myboard[6] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[8] != 'X':
                            self.grid.myboard[8] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                            
                        elif self.grid.myboard[8] == 'X':
                            self.grid.myboard[2] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                            
                elif self.grid.myboard[9] =='X':
                    self.grid.myboard[7] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[4] != 'X':
                        self.grid.myboard[4] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                    
                    else:
                        self.grid.myboard[6] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[8] != 'X':
                            self.grid.myboard[8] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                            
                        elif self.grid.myboard[8] == 'X':
                            self.grid.myboard[2] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                
                elif self.grid.myboard[6] =='X':
                    self.grid.myboard[4] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[7] != 'X':
                        self.grid.myboard[7] = 'Y'
                        self.grid.display()
                        print("You lose! Game over.")
                        break
                    
                    else:
                        self.grid.myboard[3] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[2] != 'X':
                            self.grid.myboard[2] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                            
                        elif self.grid.myboard[2] == 'X':
                            self.grid.myboard[8] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                            
                elif self.grid.myboard[2] == 'X':
                    self.grid.myboard[8] = 'Y'
                    self.player1move.makeMove('X')
                    
                    if self.grid.myboard[3] == 'X':
                        self.grid.myboard[7] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[9] != 'X':
                            self.grid.myboard[9] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                        
                        elif self.grid.myboard[9] == 'X':
                            self.grid.myboard[6] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                        
                    elif self.grid.myboard[7] == 'X':
                        self.grid.myboard[3] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[6] != 'X':
                            self.grid.myboard[6] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                        
                        elif self.grid.myboard[6] == 'X':
                            self.grid.myboard[4] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                        

                    elif self.grid.myboard[9] == 'X':
                        self.grid.myboard[4] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[7] != 'X':
                            self.grid.myboard[7] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                        
                        elif self.grid.myboard[7] == 'X':
                            self.grid.myboard[3] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break   
                            

                    elif self.grid.myboard[6] == 'X':
                        self.grid.myboard[4] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[7] != 'X':
                            self.grid.myboard[7] = 'Y'
                            self.grid.display()
                            print("You lose! Game over.")
                            break
                        
                        elif self.grid.myboard[7] == 'X':
                            self.grid.myboard[3] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break

                    elif self.grid.myboard[4] == 'X':
                        self.grid.myboard[6] = 'Y'
                        self.player1move.makeMove('X')
                        
                        if self.grid.myboard[7] != 'X':
                            self.grid.myboard[7] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break
                            
                            if self.grid.myboard[3] != 'X':
                                self.grid.myboard[3] = 'Y'
                                self.player1move.makeMove('X')
                                print("Cats game! Game over.")
                                break
                            
                            elif self.grid.myboard[3] == 'X':
                                self.grid.myboard[9] = 'Y'
                                self.player1move.makeMove('X')
                                print("Cats game! Game over.")
                                break   
                            
                        
                        elif self.grid.myboard[7] == 'X':
                            self.grid.myboard[3] = 'Y'
                            self.player1move.makeMove('X')
                            print("Cats game! Game over.")
                            break   
                        
                    
                                
def main():
    os.system('clear')
    
    
    
    
    while True:
        decision = input('Would you like to play against the computer? "Y" if you would like to, and "N" if you would like to play a friend.').upper()
        if decision == 'Y':
            gameboard = Board()
            move = Move(gameboard)
            AI = compMove(gameboard, move)
            AI.response()
            break
            
        
        elif decision == 'N':
            gameboard = Board() 
            XvsO = Game(gameboard)
            XvsO.play()
            break

main()
            
            

                        
                        
                    
                    
                
                
                
                
        
        
    
    



