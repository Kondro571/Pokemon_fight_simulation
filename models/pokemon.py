from MoveStrategy import *
class Pokemon():
    
    def __init__(self,name,lvl,types,HP,attack,defense,spAttack,spDef,speed,moves,image,b_image):
        self.name=name
        self.level=lvl
        self.types=types
        self.max_hp= self.calc_hp(HP,self.level)
        self.previous_hp=self.max_hp
        self.hp=self.max_hp
        self.attack=self.calc_stats(attack,self.level)
        self.defense=self.calc_stats(defense,self.level)
        self.sp_attack=self.calc_stats(spAttack,self.level)
        self.sp_defense=self.calc_stats(spDef,self.level)
        self.speed=self.calc_stats(speed,self.level)
        self.moves=moves
        self.image=image
        self.b_image=b_image
        self.move_strategy=None
        self.alive=True
        
        self.observers=[]
        
    #wzorzec strategii:
    def use_move(self, defender,move):
        self.move_strategy.perform_move(self, defender,move)
        
    def set_move_strategy(self, strategy):
        self.move_strategy=strategy
         
    def calc_hp(self,hp,level,iv=0,ev=0):
        return (2*hp+iv+(ev/4))*level/100 + level +10

    def calc_stats(self,stat,level,iv=0,ev=0,nature=1):
        return (2*stat+iv+(ev/4)*level/100 + 5) * nature
    
#--------obserwator--------------------------------------------------------
    def del_damage(self,damage):
        self.hp-=damage
        if self.hp<0:
            self.hp=0
            self.alive=False
        self.notify_observers()
        
    def add_observer(self,observer):
        self.observers.append(observer)
        
    def notify_observers(self):
        for observer in self.observers:
            observer.draw(self)
        
        
        
    def get_name(self):
        return self.name

    def get_types(self):
        return self.types
    
    def get_level(self):
        return self.level
    
    def get_MaxHP(self):
        return self.maxHP
    
    def get_HP(self):
        return self.hp
    
    def get_atack(self):
        return self.atack
    
    def get_defence(self):
        return self.defence
    
    def get_spAtack(self):
        return self.spAtack
    
    def get_spDef(self):
        return self.spDef
    
    def get_speed(self):
        return self.speed
    
    def get_moves(self):
        return self.moves
    
    def get_image(self):
        return self.image
    
    def get_b_image(self):
        return self.b_image
    
    def set_HP(self,HP):
        self.hp=HP
        


    def __str__(self):
        result = f"name:{self.name}\nlevel:{self.level}\ntypes:{self.types}\nmoves:\n"
        for move in self.moves:
            result += f"{move} "
        result += "\n"
        return result