

import random

def response_corrector(input_response) -> str:
    """ Function to correct user typed responses for clearly known responses to fit for function """
    if input_response in ['r','rock','Rock','R']:
        print('You chose ROCK')
        return 'r'
    elif input_response in ['p','paper','P','Paper']:
        print('You chose PAPER')
        return 'p'
    elif input_response in ['s','scissors','S','Scissors']:
        print('You chose SCISSORS')
        return 's'
    else:
        return input_response
    


def player_input() -> str:
    """ Prompts the user for a choice for a rock paper scissors game """
    response = input("Please select your play:\nType 'r' for rock,\nType 'p' for paper, or\nType 's' for scissors\n ")
    while True:
        response = response_corrector(response)
        if response in ['r','p','s']:
            break
        else:
            response = input("Please please only enter the specified inputs. \nType 'r' for rock,\nType 'p' for paper, or\nType 's' for scissors\n ")
    return response



def computer_choice() -> str:
    """ Generates a random choice for a rock paper scissors game """
    choice_num = random.randint(0,2)
    if choice_num == 0:
        choice = 'r'
        print('Computer chose ROCK')
    elif choice_num == 1:
        choice = 'p'
        print('Computer chose PAPER')
    else:
        choice = 's'
        print('Computer chose SCISSORS')
    return choice



def game_outcome(player1_choice: str, player2_choice: str) -> str:
    """ Calculates the outcome of the rock paper scissors game given the choices of player1 and player2 """
    choice_combination: str = player1_choice + player2_choice
    outcome_dict = {'p1_win':['sp','pr','rs'],
                    'p2_win':['sr','ps','rp'],
                    'tie':['ss','pp','rr']}
    for key, values in outcome_dict.items():
        if choice_combination in values:
            return key
        

def rps_v_computer():
    record = {'wins':0,'ties':0,'losses':0}
    play_again = 'y'
    while play_again == 'y':
        print('===================================')
        p_choice: str = player_input()
        c_choice: str = computer_choice()
        outcome: str = game_outcome(p_choice,c_choice)
        if outcome == 'p1_win':
            record['wins'] += 1
            print("You win!")
            if record['wins'] > (record['losses'] + 2):
                print('Dang, you are on fire!')
        elif outcome == 'p2_win':
            record['losses'] += 1
            print("You lose!")
            if record['losses'] > (record['wins'] + 2):
                print('ooof you are unlucky!')
        else:
            record['ties'] += 1
            print("It's a tie!")
        print(f"Your record is {record}\n")
        play_again = input("Would you like to play again? (y/n)\n ")
        while True:
            if play_again in ['y','n']:
                break
            else:
                print("Please enter only y or n")
                play_again = input("Would you like to play again? (y/n)\n ")