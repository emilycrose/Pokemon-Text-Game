##########################################################
# CSE Project 11: Move and Pokemon Classes
# Created December 4, 2020
#
# Move Class:
#   Contains name, element, (strings)
#       power, accuracy, and attack type attributes (ints)
#   Methods return or display each attribute
# 
# Pokemon Class:
#    Contains name, element1, element2, (strings)
#       health points, attack, defense, special attack, and special deffense (ints)
#       and moves (class objects) attributes
#    Methods:
#       Return or display each attribute
#       Moves can be assigned to pokemon
#       Pokemon can attack another pokemon and subtract its health 
##########################################################

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
        '''Returns the name of the move (for printing)'''  
        return '{}'.format(self.name)

    def __repr__(self):
        '''returns name of the move (for shell display)'''
        return '{}'.format(self.name)
    
    def get_name(self):
        '''returns the name attribute'''
        return self.name
    
    def get_element(self):
        '''returns the element attribute'''
        return self.element
    
    def get_power(self):
        '''returns the power attribute'''
        return self.power
    
    def get_accuracy(self):
        '''returns the accuracy attribute'''
        return self.accuracy
    
    def get_attack_type(self):
        '''returns the attack_type attribute'''
        return self.attack_type

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''returns a string containing the parts of the pokemon divided into 3 lines'''
        line1 = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n'.format( \
            self.name, self.hp, self.patt, self.pdef, self.satt, self. sdef)
        line2 = '{:<15}{:<15}\n'.format(self.element1, self.element2)
        line3 = ''
        for item in self.moves:
            move = item.get_name()
            line3 += '{:<15}'.format(move)
        return (line1 + line2 + line3)
    
    def __repr__(self):
        '''returns a string containing the parts of the pokemon divided into 3 lines'''
        return self.__str__()

    def get_name(self):
        '''returns the name attribute'''
        return self.name
    
    def get_element1(self):
        '''returns the element1 attribute'''
        return self.element1
    
    def get_element2(self):
        '''returns the element2 attribute'''
        return self.element2
    
    def get_hp(self):
        '''returns the hp attribute'''
        return self.hp
    
    def get_patt(self):
        '''returns the patt attribute'''
        return self.patt

    def get_pdef(self):
        '''returns the pdef attribute'''
        return self.pdef

    def get_satt(self):
        '''returns the satt attribute'''
        return self.satt

    def get_sdef(self):
        '''returns the sdef attribute'''
        return self.sdef
    
    def get_moves(self):
        ''''returns the moves attribute'''
        return self.moves

    def get_number_moves(self):
        '''returns number of moves'''
        return len(self.moves)

    def choose(self,index):
        '''takes index and returns corresponding move from moves list'''
        try:
            return self.moves[index]
        except IndexError:
            return None
    
    def show_move_elements(self):
        '''displays the elements of the pokemon's moves'''
        elements_str = ''
        for item in self.moves:
            element = item.get_element()
            elements_str += '{:<15}'.format(element)
        print(elements_str)

    def show_move_power(self):
        '''displays the power of the pokemon's moves'''
        power_str = ''
        for item in self.moves:
            power = item.get_power()
            power_str += '{:<15}'.format(power)
        print(power_str)

    def show_move_accuracy(self):
        '''displays the accuracy of the pokemon's moves'''
        accuracy_str = ''
        for item in self.moves:
            accuracy = item.get_accuracy()
            accuracy_str += '{:<15}'.format(accuracy)
        print(accuracy_str)
        
    def add_move(self, move):
        '''adds move if pokemon has less than 4 moves'''
        if len(self.moves) <= 3:
            self.moves.append(move)
                 
    def attack(self, move, opponent):
        '''takes move used by the attacker and deals damage to the opponent'''
        mp = move.get_power()
        attack_t = move.get_attack_type()
        if attack_t == 2:
            A = self.get_patt()
            D = opponent.get_pdef()
        elif attack_t == 3:
            A = self.get_satt() #attack type 3 is special attack/defense
            D = opponent.get_sdef()
        else:
            print('Invalid attack_tyoe, turn skipped.')
            return None
        
        av = randint(1, 100)
        accuracy = move.get_accuracy()
        if av > accuracy:
            print('Move missed!')
            return None
        
        modifier = 1.0
        opp_elm1 = opponent.get_element1()
        move_elm = move.get_element()
        if opp_elm1 in is_effective_dictionary[move_elm]: 
            #move element is strong against opponent
            modifier = modifier*2
        elif opp_elm1 in not_effective_dictionary[move_elm]: #move element weak
            modifier = modifier/2
        elif opp_elm1 in no_effect_dictionary[move_elm]: #move element has no effect
            modifier = 0
            return None
            
        opp_elm2 = opponent.get_element2() #checked and modified for both pokemon's elements
        if opp_elm2 in is_effective_dictionary[move_elm]:
            modifier = modifier*2
        elif opp_elm2 in not_effective_dictionary[move_elm]:
            modifier = modifier/2
        elif opp_elm2 in no_effect_dictionary[move_elm]:
            modifier = 0
            return None
        
        if modifier > 1:
            print("It's super effective!")
        elif modifier < 1:
            print("Not very effective...")
        if (move_elm == self.get_element1()) or (move_elm == self.get_element2()):
            modifier *= 1.5  #STAB bonus

        damage = ((mp * (A/D) * 20) / 50 + 2) * modifier
        opponent.subtract_hp(int(damage))
        
    def subtract_hp(self,damage):
        '''takes damage variable and subtracts it from hp of Pokemon'''
        self.hp = (self.hp-damage) if (self.hp-damage > 0) else 0
    

        