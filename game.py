from dateDownland import *
import random
import pygame
import pygame_gui
from pygame.locals import *
from memento.CareTaker import CareTaker
from memento.memento import Memento
from RoundActionManager import RoundActionManager
from Draw import *

import os

def get_image_files_in_folder(folder_path):
    image_extensions = ['.png']  # Dodaj inne rozszerzenia obrazków według potrzeb

    image_files = []
    for file_name in os.listdir(folder_path):
        if any(file_name.lower().endswith(ext) for ext in image_extensions):
            image_files.append(file_name)

    return image_files

# Przykład użycia
folder_path = "image/Battleback"
image_files_list = get_image_files_in_folder(folder_path)



class Game():
    
    def __init__(self):
        self.round_action_manager = RoundActionManager()
        
        move_downland = Download()
        rootM=move_downland.download("date/moves.xml")
        
        parser_move = move_parser()
        self.moves=parser_move.parse(rootM)
        
        pokemon_downland = Download()
        rootP=pokemon_downland.download("date/pokemon.xml")
        
        parser_Ppokemon=pokemon_parser()
        self.pokemon=parser_Ppokemon.parse(rootP,self.moves)
        
        self.game_end=False
        self.player1_pokemon=[]
        self.player2_pokemon=[]
        self.current_pokemon1=None
        self.current_pokemon2=None
        self.attack_displayC=AttackDisplay(50,480,180,50,10)
        self.tean_display=TeamDisplay(480,420,150,50,10)
        self.draw_team()
        
        self.attacks_buttons=[]
        self.pokemon_buttons=[]
        
        self.turn=0
        
        self.caretaker=CareTaker()
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Symulacja Walki Pokemonów")
        
        # tworzenie healthbars
        self.player1_pokemon_healh_bar = HealthBar(50,250,250,20)
        self.player2_pokemon_healh_bar = HealthBar(400,25,250,20)
        
        self.player1_pokemon_sprite = Sprite(100, 255,225,225)
        self.player2_pokemon_sprite = Sprite(500, 50,255,255)
        
        # Inicjalizacja Pygame GUI
        self.gui_manager = pygame_gui.UIManager((800, 600))
        
        background_image = pygame.image.load("image/Battleback/"+random.choice(image_files_list))
        self.background_image = pygame.transform.scale(background_image, (800, 600))

        self.win.blit(self.background_image,(0,0))
        
    
    def run(self):
        self.memento_display()
        self.screen_display()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.create_memento_button.rect.collidepoint(event.pos):
                        self.create_memento()
                        self.screen_display()
                        
                    if self.restore_from_memento_button.rect.collidepoint(event.pos):
                        self.restore_from_memento()
                        self.screen_display()
                        
                    for button in self.attacks_buttons:
                        if button.rect.collidepoint(event.pos):
                            
                            selected_attack = button.user_data["move_name"]
                            move = self.get_move_from_name(selected_attack)
                            if move:
                                self.attack_action(move)
                                self.screen_display()

                            
                            
                    for button in self.pokemon_buttons:
                        if button.rect.collidepoint(event.pos):
                            
                            selected_pokemon = button.text
                            pok = self.get_pokemon_from_name(selected_pokemon)
                            if pok:
                                self.switch_action(pok)
                                self.screen_display()


            self.gui_manager.process_events(event)
            self.gui_manager.update(60)
            

            self.gui_manager.draw_ui(self.win)
            pygame.display.update()
            self.clock.tick(60)
            

    def screen_display(self):
        
        self.win.blit(self.background_image,(0,0))
        self.gui_manager.update(0)
        
        self.pokemon_buttons=self.tean_display.draw(self.gui_manager,self.player1_pokemon)
        if self.check_end():

            #self.sprites_display()
            
            
            if not self.current_pokemon2.alive:
                self.current_pokemon2=self.choose_random_alive_pokemon(self.player2_pokemon)
                
            for button in self.attacks_buttons:
                button.kill()
                
            self.player2_pokemon_sprite.draw(self.win,self.current_pokemon2.image)
            if self.current_pokemon1.alive:

                for button in self.pokemon_buttons:
                    button.kill()
                self.attacks_buttons=self.attack_displayC.draw(self.gui_manager,self.current_pokemon1)
                self.player1_pokemon_sprite.draw(self.win,self.current_pokemon1.b_image)
                self.pokemon_buttons=self.tean_display.draw(self.gui_manager,self.player1_pokemon)
                self.player1_pokemon_healh_bar.draw(self.win,self.current_pokemon1)




            self.player2_pokemon_healh_bar.draw(self.win,self.current_pokemon2)

            
            
            



        #self.attacks_display()
        #self.pokemon_team_display()
        

    def get_move_from_name(self,name):
        moves=self.current_pokemon1.get_moves()
        for move in moves:
            if move.name==name:
                return move
        return None
    
    def get_pokemon_from_name(self,name):
        for pokemon in self.player1_pokemon:
            if pokemon.name==name:
                return pokemon
        return None
    
    def choose_random_alive_pokemon(self,pokemon_list):
        alive_pokemon = [pokemon for pokemon in pokemon_list if pokemon.alive]
        if alive_pokemon:
            return random.choice(alive_pokemon)
        else:
            return None
    
    def attack_action(self,move):
        print(self.turn)
        
        if self.current_pokemon1.speed>self.current_pokemon2.speed:
            move2=random.choice(self.current_pokemon2.get_moves())
            
            self.round_action_manager.calculate_damage(self.current_pokemon1, self.current_pokemon2, move)
            if self.current_pokemon2.alive:
                self.round_action_manager.calculate_damage(self.current_pokemon2, self.current_pokemon1, move2)
        else:
            move2=random.choice(self.current_pokemon2.get_moves())
 
            self.round_action_manager.calculate_damage(self.current_pokemon2, self.current_pokemon1, move2)
            if self.current_pokemon1.alive:
                self.round_action_manager.calculate_damage(self.current_pokemon1, self.current_pokemon2, move)
        
    
        self.turn+=1
            

    def switch_action(self,pokemon):
        
        if self.current_pokemon1.alive:
            move2=random.choice(self.current_pokemon2.get_moves())
            self.round_action_manager.calculate_damage(self.current_pokemon2, pokemon, move2)
            self.turn+=1
        
        self.current_pokemon1=self.round_action_manager.perform_switch_action(pokemon)


   
   
    
    def memento_display(self):
        button = pygame.Rect(20, 10, 70, 30)    
        self.create_memento_button = (pygame_gui.elements.UIButton(relative_rect=button, text="save", manager=self.gui_manager))
        
        button = pygame.Rect(100, 10, 70, 30)    
        self.restore_from_memento_button = (pygame_gui.elements.UIButton(relative_rect=button, text="load", manager=self.gui_manager))
   
    def draw_team(self):
        self.player1_pokemon = [copy.deepcopy(pokemon) for pokemon in random.sample(self.pokemon, 6)]
        self.current_pokemon1 = self.player1_pokemon[0]

        self.player2_pokemon = [copy.deepcopy(pokemon) for pokemon in random.sample(self.pokemon, 6)]
        self.current_pokemon2 = self.player2_pokemon[0]
        
    def create_memento(self):
        memento = Memento(self.turn, self.player1_pokemon,self.current_pokemon1, self.player2_pokemon,self.current_pokemon2)
        self.caretaker.add_state(memento)
        print("Zapisano stan walki!")

    def restore_from_memento(self):
        if self.caretaker.has_states():
            memento = self.caretaker.get_last_state()
            self.turn = memento.get_turn()
            self.player1_pokemon = memento.get_player1()
            self.player2_pokemon = memento.get_player2()
            self.current_pokemon1 = memento.get_pokemon1()
            self.current_pokemon2 = memento.get_pokemon2()
            print("Przywrócono walkę!")

    def check_end(self):
        all_dead = all(not pokemon.alive for pokemon in self.player1_pokemon)
        all_dead2 = all(not pokemon.alive for pokemon in self.player2_pokemon)
        if all_dead:
            print("Przegrales!")
            self.win.blit(self.background_image,(0,0))
            for button in self.attacks_buttons:
                button.kill()
            
            self.game_end=True
            return False
        if all_dead2:
            print("Wygrales!")
            self.win.blit(self.background_image,(0,0))
            for button in self.attacks_buttons:
                button.kill()
            self.game_end=True
            return False
        
        return True
  

if __name__ == "__main__":
    simulation = Game()
    simulation.run()
    pygame.quit()