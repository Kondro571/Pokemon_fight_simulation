class Move():
    
    def __init__(self,name,type,category,power,accuracy,pp):
        self.name=name
        self.category=category
        self.type=type
        self.power=power
        self.accuracy=accuracy
        self.pp=pp
        self.max_pp=pp
    
    
    def use(self):
        self.pp=-1
    
    
    
    
    
    
    
    
    
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    def get_category(self):
        return self.category
    
    def get_power(self):
        return self.power
    
    def get_accuracy(self):
        return self.accuracy

    def get_pp(self):
        return self.pp
    
    def get_maxPP(self):
        return self.max_pp
    
    def set_pp(self,pp):
        self.pp=pp
    
    def __str__(self):
        return f"{self.name},{self.category},{self.power},{self.accuracy},{self.pp}\n"

        
    
    
