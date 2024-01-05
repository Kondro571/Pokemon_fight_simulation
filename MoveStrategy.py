# strategia!!!!
import math
from typeChart import type_chart

class MoveStrategy:
    def perform_move(self, attacker, defender):
        pass

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
        
        defender.del_damage(damage)
        
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
        
        defender.del_damage(damage)
        
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
        attacker.del_damage(0)
        move.pp-=1
        print(f"{attacker.name} uzywa ruchu statusowego!")


