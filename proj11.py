##########################################################
# CSE Project 11
# Created December 4, 2020
#
# Pokemon
#
# Algorithm
#   Read pokemon and move data into lists
#   Ask players if they'd like to battle
#   Prompt players for pokemon and enter game loop
#   For each player's turn:
#       Display pokemon data and moves
#       Prompt to show move stats or select move
#       Display opponent's health before and after attack
#           Game ends once a pokemon dies or player quits
#   Prompts players to play again
##########################################################
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #same events always happen


#DO NOT CHANGE!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    '''takes file pointer and returns a list of move objects'''
    moves_list = []
    reader = csv.reader(fp)
    next(reader, None) #skip header line
    for line in reader:
        generation_id = int(line[2])
        name = line[1]
        attack_type = int(line[9])
        if (generation_id == 1) and (attack_type != 1): #must be first gen and attack 2 or 3
            try: #account for missing accuracy or power
                element_id = int(line[3])
                element = element_id_list[element_id] #element_id represents index
                accuracy = int(line[6])
                power = int(line[4])
                move = Move(name, element, power, accuracy, attack_type) 
                #create move instance
                moves_list.append(move)
            except:
                next(reader, None)
    return moves_list


def read_file_pokemon(fp):
    '''takes file pointer and returns a list of pokemon objects'''
    pokemon_list = []
    id_list = []
    reader = csv.reader(fp)
    next(reader, None) #skip header line
    for line in reader:
        generation_id = int(line[11])
        ID = int(line[0]) #use to avoid duplicates
        if (generation_id == 1) and (ID not in id_list):
            #must be first gen and not already in the pokemon_list
            id_list.append(ID)
            name = line[1].lower()
            element1 = line[2].lower()
            element2 = line[3].lower()
            hp = int(line[5])
            patt = int(line[6]) #attack
            pdef = int(line[7]) #defense
            satt = int(line[8]) #special attack
            sdef = int(line[9]) #special defense
            pokemon = Pokemon(name, element1, element2, None, hp, 
                              patt, pdef, satt, sdef) #create pokemon instance
            pokemon_list.append(pokemon)
    return pokemon_list

def choose_pokemon(choice,pokemon_list):
    '''takes user input (string or int--for indexing) and returns corresponding 
    pokemon object'''
    try:
        choice = int(choice)-1
        return deepcopy(pokemon_list[choice])
    except: #if choice is not an int
        choice = choice.lower()
        for pokemon in pokemon_list:
            if pokemon.get_name() == choice: #iterate through all pokemon and return match
                return deepcopy(pokemon)
    
def add_moves(pokemon,moves_list):
    '''Assigns pokemon a random move, and 3 random moves of the same element type'''
    int1 = randint(0,len(moves_list)-1)
    move1 = moves_list[int1] #first 'random' move
    pokemon.add_move(move1)
    count = 0
    while (count < 200) and (pokemon.get_number_moves() < 4):
        count += 1
        rand_int = randint(0,len(moves_list)-1)
        move = moves_list[rand_int]
        if (move.get_element() == pokemon.get_element1()) or (
                move.get_element() == pokemon.get_element2()):
            #move must macth one of the pokemon's elements
            if move not in pokemon.get_moves():
                #pokemon must not already know move
                pokemon.add_move(move)
    if pokemon.get_number_moves() == 4:
        return True
    else: #return false if 200 tries were not successful
        return False

def turn (player_num, player_pokemon, opponent_pokemon):
    '''Prompt player for index into the list of moves, a request, or quit'''
    if player_num == 1:
        num2 = 2 #variable of other player's number
    else: num2 = 1
    print("Player {:d}'s turn".format(player_num))
    print(player_pokemon)
    
    x = True
    while x == True: #loop until attack is made or quit
        print("\nShow options: 'show ele', 'show pow', 'show acc'")
        request = input("Select an attack between 1 and 4 or show option or 'q': ")
        try: #catch if not int
            request = int(request)
            move = player_pokemon.choose(request-1)
            print(move)
            name = opponent_pokemon.get_name() #pokemon name, for printing
            
            print('Selected move: ', move, '\n') #display move
            print(name, 'hp before:', opponent_pokemon.get_hp()) #opponent's starting hp
            player_pokemon.attack(move, opponent_pokemon)
            print(name, ' hp after: ', opponent_pokemon.get_hp()) #ending hp display
            if opponent_pokemon.get_hp() == 0: #pokemon died, game ends
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(
                    num2, player_num))
                return False
            return True #game is not over
        
        except: #display move elements, power, or accuracy
            if request == 'show ele':
                player_pokemon.show_move_elements()
            elif request == 'show pow':
                player_pokemon.show_move_power()
            elif request == 'show acc':
                player_pokemon.show_move_accuracy()
            elif request == 'q':
                print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, num2))
                return False #player quits, game ends
             
def main():
    '''opens and reads files, prompts for user input pokemon, and battles until quit'''
    file_obj_p = open('pokemon.csv', 'r')
    pokemon_list = read_file_pokemon(file_obj_p)
    file_obj_m = open('moves.csv', 'r')
    moves_list = read_file_moves(file_obj_m)
    file_obj_p.close()
    file_obj_m.close()
    
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
        #gets valid input
    a = True
    while a == True: #game loop
        
        if usr_inp != 'y':
            print("Well that's a shame, goodbye")
            return
        
        else:
            player1 = input('Player 1, choose a pokemon by name or index: ')
            pokemon1 = choose_pokemon(player1, pokemon_list)
            print('pokemon1:\n', pokemon1) #displays player 1 pokemon object
            add_moves(pokemon1, moves_list) #assigns pokemon 1 moves
            
            player2 = input('Player 2, choose a pokemon by name or index: ')
            pokemon2 = choose_pokemon(player2, pokemon_list)
            print('pokemon2:\n', pokemon2, '\n') #displays player 2 pokemon
            add_moves(pokemon2, moves_list) #assigns pokemon 2 moves
            
            game = True
            while game == True: #True until a player loses or quits during turn
                game = turn(1, pokemon1, pokemon2)
                print()
                if game == True:
                    game = turn(2, pokemon2, pokemon1)
                    print()
            if game == False:
                usr_inp = input('Battle over, would you like to have another? ').lower()
                if usr_inp == 'n':
                    a = False #exit game loop
                    print("Well that's a shame, goodbye")
                    
if __name__ == "__main__":
    main()
