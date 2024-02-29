class Animal:
    def __init__(self, kind, name):
        self.kind=kind
        self.name=name
        
class Zoo:
    def __init__(self):
        self.list_animals=[]
        
    def add_animal(self, animal):
        self.list_animals.append(animal)
        print(f"{animal.kind} {animal.name} added to list")
    
    def remove_from_list(self, animal):
        for i self.list_animals:
            if animal==i:
                self.list_animals.remove(i)
                
                
Dog= Animal("Dog", "Tyzik")
Cat=Animal("Cat", "Vasia")
Mouse= Animal("Mouse", "Masha")
zoo = Zoo()

zoo.add_animal(Dog)
zoo.add_animal(Cat)
zoo.add_animal(Mouse)


        
        
    