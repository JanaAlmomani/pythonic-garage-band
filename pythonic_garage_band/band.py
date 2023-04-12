from abc import ABC, abstractmethod

class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solo = [] 
        for member in self.members:
            solo.append(member.play_solo())
        return solo

    def __str__(self):
        return f'Band Name = {self.name}'

    def __repr__(self):
        return f'Band Name = {self.name}'

    @classmethod
    def to_list(cls):
        return cls.instances
    

class Musician:#super (parent) 
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

    # def __str__(self):
    #       return f'My name is : {self.name}'
    
    # def __repr__(self): 
    #     return f'I am a representation of {self.name}'

class Guitarist(Musician): #sub class 
    def __init__(self ,name):
        super().__init__(name)

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"
        
    #My name is Joan Jett and I play guitar
    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
      return f'Guitarist instance. Name = {self.name}'
    
    
    
class Bassist(Musician): #sub class 
    def __init__(self ,name):
        super().__init__(name)
    
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"
   
    def __str__(self):
        return f'My name is {self.name} and I play bass'
    
    #"Bassist instance. Name = Meshell Ndegeocello"
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    
class Drummer(Musician): #sub class 
    def __init__(self ,name):
        super().__init__(name)
   
    def get_instrument(self):
      return "drums"
    
    def play_solo(self):
        return "rattle boom crash"

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
       return f'Drummer instance. Name = {self.name}'
     
    
    
