from random import randint

class Game():

    def __init__(self):
        while True:
            scoring_dict = {
                'Rock': 1,
                'Paper': 2,
                'Scissors': 3
            }
            player_response = input('Would you like to play? ')
            comp_input = randint(1, 3)
            self.comp_input = comp_input
            if player_response.lower() == 'yes':
                player_input = input('Rock, paper, or scissors? ')
                self.player_input = player_input
                Game.rps(self)
            else:
                quit_statement = input('Would you like to quit? ')
                if quit_statement.lower() == 'yes':
                    break
                else:
                    pass
    
    def rps(self):
        if self.player_input.lower() == 'rock': 
            if self.comp_input == 1:
                print('Computer also chooses rock! Try again! ')
                Game()
            elif self.comp_input == 2:
                print('Computer chooses paper! Paper covers rock! You lose! ')
                Game()
            else:
                print('Computer chooses scissors! Rock breaks scissors! You win! ')
                Game()
        elif self.player_input.lower() == 'paper':
            if self.comp_input == 1:
                print('Computer chooses rock! Paper covers rock! You win! ')
                Game()
            elif self.comp_input == 2:
                print('Computer also chooses paper! Try again! ')
                Game()
            else:
                print('Computer chooses scissors! Scissors cut paper! You lose! ')
                Game()
        elif self.player_input.lower() == 'scissors':
            if self.comp_input == 1:
                print('Computer chooses rock! Scissors are broken by rock! You lose! ')
                Game()
            elif self.comp_input == 2:
                print('Computer chooses paper! Scissors cut paper! You win! ')
                Game()
            else: 
                print('Computer also chooses scissors! Try again! ')
                Game()

def launcher():
    my_game = Game()

launcher()