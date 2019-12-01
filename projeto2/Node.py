class Node:
    def __init__(self, key, movie):
        self.key = key
        self.movie = movie
        self.left = None
        self.right = None

    def __str__ (self):
        return '{}'.format(self.movie)
