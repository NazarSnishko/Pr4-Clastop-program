class Animal:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name
        
class Zoo:
    def __init__(self):
        self.list_animals = []
        
    def add_animal(self, animal):
        self.list_animals.append(animal)
        print(f"{animal.kind} {animal.name} додано до списку")
    
    def remove_from_list(self, animal):
        if animal in self.list_animals:
            self.list_animals.remove(animal)
            print(f"{animal.kind} {animal.name} вилучено зі списку")
        else:
            print(f"{animal.kind} {animal.name} не знайдено у списку ")
                
    def add_new_animal(self, kind, name):
        new_animal = Animal(kind, name)
        self.list_animals.append(new_animal)
        print(f"{new_animal.kind} {new_animal.name} додано до списку")
        
    def whole_list(self):
        print("весь список у зоопарку: ")
        for animal in self.list_animals:
            print(f"{animal.kind} {animal.name}")
                
                
Dog = Animal("Собака", "Тузік")
Cat = Animal("Кіт", "Вася")
Mouse = Animal("Миша", "Маша")
zoo = Zoo()

zoo.add_animal(Dog)
zoo.add_animal(Cat)
zoo.add_animal(Mouse)

zoo.remove_from_list(Cat)

zoo.add_new_animal("Собака", "Петро")

zoo.whole_list()
