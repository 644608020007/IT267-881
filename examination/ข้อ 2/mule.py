
from donkey import *
from horse import *

class Mule(Horse,Donkey):
    def __init__(self, name: str, color: str,age:int,weight:float,max_height: float = 200) -> None:
        super().__init__(name, color, max_height,)
        self.age = age
        self.weight = weight
        
    
    def run(self):
        super().run()
    
    def show_info(self):
        print(f'COLOR :{self.color}')
        print(f'MAX HEIGHT :{self.max_height} CM.')
        print(f'AGE :{self.age}-YEAR-OLD.')
        print(f'WEIGHT :{self.weight} KG.')

mule1 =Mule('MUMU','BLUE-EYED CREAM',3,200)
print(f'**** MUMU INFO ****')
mule1.show_name()
mule1.show_info()

mule2 = Mule('MEME','PALOMINO',1,120.7)
print(f'**** MEME INFO ****')
mule2.sound()
mule2.show_name()
mule2.show_info()






    
    