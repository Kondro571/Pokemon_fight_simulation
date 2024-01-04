# Definicja interfejsu strategii!!!!
import math
import typeChart
type_chart = {
    'Normal': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 0.5, 'Ghost': 0, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Fire': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1, 'Grass': 2, 'Ice': 2, 'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 2, 'Fairy': 1},
    'Water': {'Normal': 1, 'Fire': 2, 'Water': 0.5, 'Electric': 1, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 1, 'Ground': 2, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 2, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 1, 'Fairy': 1},
    'Electric': {'Normal': 1, 'Fire': 1, 'Water': 2, 'Electric': 0.5, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 1, 'Ground': 0, 'Flying': 2, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 1, 'Fairy': 1},
    'Grass': {'Normal': 1, 'Fire': 0.5, 'Water': 2, 'Electric': 1, 'Grass': 0.5, 'Ice': 2, 'Fighting': 1, 'Poison': 0.5, 'Ground': 2, 'Flying': 0.5, 'Psychic': 1, 'Bug': 0.5, 'Rock': 2, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Ice': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1, 'Grass': 1, 'Ice': 0.5, 'Fighting': 1, 'Poison': 1, 'Ground': 2, 'Flying': 2, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Fighting': {'Normal': 2, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 1, 'Poison': 0.5, 'Ground': 1, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Rock': 2, 'Ghost': 0, 'Dragon': 1, 'Dark': 2, 'Steel': 2, 'Fairy': 0.5},
    'Poison': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 2, 'Ice': 1, 'Fighting': 1, 'Poison': 0.5, 'Ground': 0.5, 'Flying': 1, 'Psychic': 2, 'Bug': 1, 'Rock': 1, 'Ghost': 0.5, 'Dragon': 1, 'Dark': 1, 'Steel': 0, 'Fairy': 2},
    'Ground': {'Normal': 1, 'Fire': 2, 'Water': 1, 'Electric': 2, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 2, 'Ground': 1, 'Flying': 0, 'Psychic': 1, 'Bug': 0.5, 'Rock': 2, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 2, 'Fairy': 1},
    'Flying': {'Normal': 1, 'Fire': 1, 'Water': 2, 'Electric': 0.5, 'Grass': 2, 'Ice': 1, 'Fighting': 2, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Psychic': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 2, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 0.5, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 1, 'Dark': 0, 'Steel': 0.5, 'Fairy': 1},
    'Bug': {'Normal': 1, 'Fire': 0.5, 'Water': 1, 'Electric': 1, 'Grass': 2, 'Ice': 1, 'Fighting': 0.5, 'Poison': 0.5, 'Ground': 1, 'Flying': 0.5, 'Psychic': 2, 'Bug': 1, 'Rock': 1, 'Ghost': 0.5, 'Dragon': 1, 'Dark': 2, 'Steel': 0.5, 'Fairy': 0.5},
    'Rock': {'Normal': 1, 'Fire': 2, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 2, 'Fighting': 0.5, 'Poison': 1, 'Ground': 0.5, 'Flying': 2, 'Psychic': 1, 'Bug': 2, 'Rock': 1, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Ghost': {'Normal': 0, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 0, 'Poison': 0.5, 'Ground': 1, 'Flying': 1, 'Psychic': 2, 'Bug': 0.5, 'Rock': 1, 'Ghost': 2, 'Dragon': 1, 'Dark': 1, 'Steel': 1, 'Fairy': 1},
    'Dragon': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 1, 'Steel': 0.5, 'Fairy': 0},
    'Dark': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 0.5, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 2, 'Bug': 1, 'Rock': 1, 'Ghost': 0.5, 'Dragon': 1, 'Dark': 0.5, 'Steel': 1, 'Fairy': 0.5},
    'Steel': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Grass': 1, 'Ice': 2, 'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 2, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel':0.5, 'Fairy': 0.5},
    'Fairy': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 1, 'Fairy': 1 }
}
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

