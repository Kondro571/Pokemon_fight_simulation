# Definicja interfejsu strategii!!!!
import math
from typeChart import type_chart

class MoveStrategy:
    def perform_move(self, attacker, defender):
        pass

# Konkretne strategie (algorytmy) dla różnych typów ruchów
class PhysicalMoveStrategy(MoveStrategy):
    def perform_move(self, attacker, defender,move):
        
        STAB=1
        type_efectivnes=1
        
        attacker_type=attacker.get_types()
        defender_type=defender.get_types()
        
        if move.type in attacker_type:
            STAB=1.5
        
        for type in defender_type:
            if type is not None:
                type_efectivnes *= type_chart[move.type][type]

       
        move.pp-=1
        
        damage =(((2*attacker.level/5+2)*move.power*(attacker.attack/defender.defense))/50+2)*STAB*type_efectivnes
        damage=math.floor(damage)
        defender.previous_hp=defender.hp
        defender.hp -= damage
        print(f"{attacker.name} uzyl {move.name} i zadal {damage} obrazen!")
        if type_efectivnes>1:
            print("Super effectivne!")
        elif type_efectivnes<1:
            print("Not very effective!")
            
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} faint!")

class SpecialMoveStrategy(MoveStrategy):
    def perform_move(self, attacker, defender,move):
        
        STAB=1
        type_efectivnes=1
        
        attacker_type=attacker.get_types()
        defender_type=defender.get_types()
        
        if move.type in attacker_type:
            STAB=1.5
        
        for type in defender_type:
            if type is not None:
                type_efectivnes *= type_chart[move.type][type]

                
        move.pp-=1
                
        damage = (((2*attacker.level/5+2)*move.power*(attacker.sp_attack/defender.sp_defense))/50+2)*STAB*type_efectivnes
        damage=math.floor(damage)
        defender.previous_hp=defender.hp
        damage=math.floor(damage)
        defender.hp -= damage
        print(f"{attacker.name} uzyl {move.name} i zadal {damage} obrazen!")
        if type_efectivnes>1:
            print("Super effectivne!")
        elif type_efectivnes<1:
            print("Not very effective!")
            
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} faint!")

class StatusMoveStrategy(MoveStrategy):
    def perform_move(self, attacker, defender,move):
        move.pp-=1
        print(f"{attacker.name} uzywa ruchu statusowego!")

# class Pokemon:
#     def __init__(self, name, attack, defense, sp_attack, sp_defense, hp, move_strategy):
#         self.name = name
#         self.attack = attack
#         self.defense = defense
#         self.sp_attack = sp_attack
#         self.sp_defense = sp_defense
#         self.hp = hp
#         self.move_strategy = move_strategy

#     def use_move(self, defender):
#         self.move_strategy.perform_move(self, defender)


# if __name__ == "__main__":

#     pokemon1 = Pokemon("Charizard", 84, 78, 109, 85, 78, PhysicalMoveStrategy())
#     pokemon2 = Pokemon("Blastoise", 83, 100, 85, 105, 79, SpecialMoveStrategy())
#     pokemon3 = Pokemon("Alakazam", 50, 45, 135, 85, 55, StatusMoveStrategy())


#     pokemon1.use_move(pokemon2)
#     pokemon2.use_move(pokemon1)
#     pokemon3.use_move(pokemon1)

