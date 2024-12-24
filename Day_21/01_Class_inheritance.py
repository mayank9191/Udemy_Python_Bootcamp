class Animal:  # Parent Class
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):          # Child Class
    def __init__(self):
        super().__init__()

    def breathe(self):       # do something extra than inherit class method function
        super().breathe()    # it will do the same way off function of parent class
        print("doing this underwater")

    def swim(self):
        print("moving in water.")


luke = Fish()
luke.swim()
luke.breathe()
print(luke.num_eyes)
