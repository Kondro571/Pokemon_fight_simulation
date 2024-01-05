#singleton
import copy
from MoveStrategy import *
class RoundActionManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RoundActionManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def calculate_damage(self, attacker, defender, move):
        if move.category=="Physical":
            attacker.move_strategy=PhysicalMoveStrategy()
        elif move.category=="Special":
            attacker.move_strategy=SpecialMoveStrategy()
        else:
            attacker.move_strategy=StatusMoveStrategy()
            
        attacker.use_move(defender,move)


    def perform_switch_action(self, new_pokemon):
        new_pokemon.del_damage(0)
        return (new_pokemon)
        


