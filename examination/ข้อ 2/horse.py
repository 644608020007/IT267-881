class Horse:
    def __init__(self,name:str,color:str,max_height:float = 200) -> None:
        self.name = name
        self.color = color
        self.max_height = max_height
    def run(self):
        print(f'{self.name} IS RUNNING')

    def show_name(self):
        print(f'NAME : {self.name}')

    def show_info(self):
        print(f'COLOR : {self.color}')
        print(f'MAX HEIGHT : {self.max_height} CM.')