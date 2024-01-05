import pygame
import pygame_gui
from models.pokemon import *
#obserwator
class HealthBar():
    def __init__(self,win,x,y,width,height,pokemon):
        self.x=x
        self.y=y
        self.win=win
        self.width=width
        self.height=height
        self.pokemon=pokemon
        self.pokemon.add_observer(self)

    def draw(self,pokemon):
        if isinstance(pokemon, Pokemon) and pokemon == self.pokemon:
  
            #backgrounf for health bar
            pygame.draw.rect(self.win, "black", (self.x-10, self.y-20, self.width+20, self.height+30))
            
            #pokemon name level
            font=pygame.font.SysFont("comicsansms", 15)
            text=font.render(f"{pokemon.name} lvl:{pokemon.level}", 1,(255,255,255))
            self.win.blit(text, (self.x, self.y-22))
            
            #health bar
           
            retio = pokemon.hp / pokemon.max_hp
            pygame.draw.rect(self.win, "red", (self.x, self.y, self.width, self.height))
            pygame.draw.rect(self.win, "green", (self.x, self.y, self.width * retio, self.height))
        
        # pygame.draw.rect(win, "red", (self.x, self.y, self.width, self.height))
        # previous_health = self.width * (pokemon.previous_hp / pokemon.max_hp)
        # health_width = self.width * (pokemon.hp / pokemon.previous_hp)
        # print(health_width," ",previous_health)
        
        # if pokemon.previous_hp == pokemon.max_hp:
        #     pygame.draw.rect(win, "green", (self.x, self.y, self.width, self.height))
        # for i in range(int(previous_health),int(health_width), -1):

        #     pygame.display.update()

        #     pygame.draw.rect(win, "green", (self.x, self.y, i, self.height))
        #     pygame.time.delay(5)  
        
        
class Sprite():
    def __init__(self,win,x,y,width,height):
        self.win=win
        self.x=x
        self.y=y
        self.width=width
        self.height=height

        
    def draw(self,image):
        pokemon_image = pygame.image.load("image/sprites/"+image)  
        pokemon_image = pygame.transform.scale(pokemon_image, (self.width, self.height))
        pokemon_rect = pokemon_image.get_rect()
        pokemon_rect.topleft = (self.x, self.y)
        self.win.blit(pokemon_image, pokemon_rect)
        
class AttackDisplay:
    def __init__(self,x,y,width,height,margin=10):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.margin=margin
        
    
    def draw(self,gui_manager,pokemon):
        attacks_buttons=[]
        attacks=pokemon.get_moves()
        button_width = self.width
        button_height = self.height
        button_margin_x = self.margin
        button_margin_y = self.margin

        start_x = self.x
        start_y = self.y

        rows = 2
        columns = 2
        for row in range(rows):
            for col in range(columns):
                button_rect = pygame.Rect(start_x + row * (button_width + button_margin_x),
                                        start_y + col * (button_height + button_margin_y),
                                        button_width, button_height)
                button=(pygame_gui.elements.UIButton(
                    relative_rect=button_rect, 
                    text=attacks[row*columns+col].name+" "+str(attacks[row*columns+col].pp)+"/"+str(attacks[row*columns+col].max_pp),
                    manager=gui_manager,
                    ))
                button.user_data={"move_name": attacks[row*columns+col].name}
                attacks_buttons.append(button)
        
        return attacks_buttons
    

class TeamDisplay():

    def __init__(self,x,y,width,height,margin=10):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.margin=margin
        
    def draw(self,gui_manager,pokemon_list):
                pokemon_buttons=[]
                button_width = self.width
                button_height = self.height
                button_margin_x = self.margin
                button_margin_y = self.margin
                
                start_x = self.x
                start_y = self.y
                
                rows = 2
                columns = 3
                
                for row in range(rows):
                    for col in range(columns):
                        pok=pokemon_list[row * columns + col]
                        button_rect = pygame.Rect(start_x + row * (button_width + button_margin_x),
                                                start_y + col * (button_height + button_margin_y),
                                                button_width, button_height)
                        
                        button=(pygame_gui.elements.UIButton(
                            relative_rect=button_rect,
                            text=pok.name,
                            manager=gui_manager
                            ))
                        
                        if not pok.alive:
                            button.disable()
                            
                        pokemon_buttons.append(button)
                        
                return pokemon_buttons
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
 
    # def attacks_display(self):
    #     self.attacks_buttons=[]
    #     attacks=self.current_pokemon1.get_moves()
    #     button_width = 150
    #     button_height = 50
    #     button_margin_x = 10
    #     button_margin_y = 10

    #     start_x = 50
    #     start_y = 480

    #     rows = 2
    #     columns = 2
    #     for row in range(rows):
    #         for col in range(columns):
    #             button_rect = pygame.Rect(start_x + row * (button_width + button_margin_x),
    #                                     start_y + col * (button_height + button_margin_y),
    #                                     button_width, button_height)
    #             self.attacks_buttons.append(pygame_gui.elements.UIButton(relative_rect=button_rect, text=attacks[row*columns+col].name, manager=self.gui_manager))
 
    # def pokemon_team_display(self):
    #     #team
    #     self.pokemon_buttons=[]
    #     button_width = 150
    #     button_height = 50
    #     button_margin_x = 10
    #     button_margin_y = 10

    #     start_x = 480
    #     start_y = 420

    #     rows = 2
    #     columns = 3

    #     for row in range(rows):
    #         for col in range(columns):
    #             button_rect = pygame.Rect(start_x + row * (button_width + button_margin_x),
    #                                     start_y + col * (button_height + button_margin_y),
    #                                     button_width, button_height)
    #             self.pokemon_buttons.append(pygame_gui.elements.UIButton(relative_rect=button_rect, text=self.player1_pokemon[row * columns + col].name, manager=self.gui_manager))
            
    # def sprites_display(self):
    #     pokemon_image = pygame.image.load("image/"+self.current_pokemon1.b_image)  
    #     pokemon_image = pygame.transform.scale(pokemon_image, (225, 225))
    #     pokemon_rect = pokemon_image.get_rect()
    #     pokemon_rect.topleft = (100, 255)
    #     self.win.blit(pokemon_image, pokemon_rect)
        
    #     pokemon_image = pygame.image.load("image/"+self.current_pokemon2.image)  
    #     pokemon_image = pygame.transform.scale(pokemon_image, (225, 225))
    #     pokemon_rect = pokemon_image.get_rect()
    #     pokemon_rect.topleft = (500, 50)
    #     self.win.blit(pokemon_image, pokemon_rect)