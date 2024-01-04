    def __init__(self):
        
        move_downland = Download()
        rootM=move_downland.download("moves.xml")
        
        parser_move = move_parser()
        self.moves=parser_move.parse(rootM)
        
        pokemon_downland = Download()
        rootP=pokemon_downland.download("pokemon.xml")
        
        parser_Ppokemon=pokemon_parser()
        self.pokemon=parser_Ppokemon.parse(rootP,self.moves)
        
        self.player1_pokemon=[]
        self.player2_pokemon=[]
        self.current_Pokemon1=None
        self.current_Pokemon2=None
        self.turn=0
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Symulacja Walki Pokemonów")
        
        # Inicjalizacja Pygame GUI
        self.gui_manager = pygame_gui.UIManager((800, 600))