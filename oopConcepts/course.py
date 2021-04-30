class Course:
    def __init__(self, name, ratings): # Parameterized constructor
        self.name = name
        self.ratings = ratings

    def avgRatings(self): # Instance Method
        count = len(self.ratings)
        sumRat = sum(self.ratings)
        return sumRat/count

c1 = Course("Java", [1, 2, 3])
print(c1.name, c1.ratings, c1.avgRatings())

c2 = Course("Java Service", [2, 3, 4, 5])
print(c2.name, c2.ratings, c2.avgRatings())
