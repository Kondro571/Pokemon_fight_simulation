import xml.etree.ElementTree as ET
import copy
from models.move import *
from models.pokemon import *

class Download():
    
    def __init__(self):
        pass
        
    def download(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        return root
            

class move_parser:
    def __init__(self):
        pass
    
    def parse(self, root):
    
        list_moves=[]
        
        for pozycja in root.findall(".//move"):
            name=pozycja.find("name").text
            type=pozycja.find("type").text
            category=pozycja.find("category").text
            power=int(pozycja.find("power").text)
            accuracy=int(pozycja.find("accuracy").text)
            pp=int(pozycja.find("pp").text)
            list_moves.append(Move(name,type,category,power,accuracy,pp))
            
        return list_moves

class pokemon_parser:
    def __init__(self):
        pass
    
    def parse(self, root,list_moves):
        list_pokemon=[]
        
        for pokemon in root.findall(".//pokemon"):
            moves=[]
            pok_moves=[]
            name=pokemon.find("name").text
            level=int(pokemon.find("level").text)
            type1=pokemon.find("type1").text
            type2=pokemon.find("type2").text
            hp=int(pokemon.find("hp").text)
            attack=int(pokemon.find("attack").text)
            defense=int(pokemon.find("defense").text)
            sp_attack=int(pokemon.find("sp_attack").text)
            sp_defense=int(pokemon.find("sp_defense").text)
            speed=int(pokemon.find("speed").text)
            image=pokemon.find("image").text
            b_image=pokemon.find("b_image").text
            moves.append(pokemon.find("move1").text)
            moves.append(pokemon.find("move2").text)
            moves.append(pokemon.find("move3").text)
            moves.append(pokemon.find("move4").text)
            
            for move in list_moves:
                if move.get_name() in moves:
                    pok_moves.append(copy.deepcopy(move)) 
                    

            list_pokemon.append(Pokemon(name,level,[type1,type2],hp,attack,defense,sp_attack,sp_defense,speed,pok_moves,image,b_image))
            
        return list_pokemon