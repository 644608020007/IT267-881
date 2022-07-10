class JuiceOrder:

    def __init__(self, menu, size) -> None:
        self.menu = menu
        self.size = size

    def check_menu(self):
        if self.menu == 'OJ':
            self.price = 25
        elif self.menu == 'AJ':
            self.price = 25
        elif self.menu == 'WJ':
            self.price = 30
        elif self.menu == 'PJ':
            self.price = 30
        self.compute_price()
        self.display_order()

    def compute_price(self):
        if self.size == 'L':
            self.price = self.price + 5

    def display_order(self):
        print(f"{self.menu}({self.size} * {self.price}) => {self.price}")

#test 1 
item1 = JuiceOrder('WJ', "L")
item1.check_menu()
#test 2 
item2 = JuiceOrder('OJ', "R")
item2.check_menu()
#test 3 
item3 = JuiceOrder('PJ', "L")
item3.check_menu()
