
class Donkey:
    def __init__(self,age:int,weight:float) -> None:
        self.age = age
        self.weight = weight

    def sound(self):
        print('DONKEY MAKES EEYORE SOUND')

    def show_info(self):
        print(f'AGE : {self.age}-YEAR-OLD.')
        print(f'WEIGHT : {self.weight} KG.')
