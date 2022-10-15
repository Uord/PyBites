class Animal:

    seq = 10000
    animals = []

    def __init__(self, name):
        self.name = name.capitalize()
        Animal.seq += 1
        self.seq = Animal.seq
        Animal.animals.append(str(self))

    def __str__(self):
        return f"{self.seq}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join(cls.animals)
