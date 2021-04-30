class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.score = score
        self.name = name

    def display(self):
        print(self.id, self.name, self.score)
