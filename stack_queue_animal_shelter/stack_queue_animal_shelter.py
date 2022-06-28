from stack_and_queue.stack_and_queue.Queue import Queue

class Dog:
    type = 'dog'
    def __init__(self,name):
        self.name = name

class Cat:
    type = 'cat'
    def __init__(self,name):
        self.name = name


class  AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):

        if animal.type == 'cat':
            self.cats.enqueue(animal)
        elif animal.type == 'dog':
            self.dogs.enqueue(animal)

    def dequeue(self,pref):

        try:
            if pref == 'cat':
                cat = self.cats.dequeue()
                return cat.name
            elif pref == 'dog':
                dog = self.dogs.dequeue()
                return dog.name
        except AttributeError as e:
            return None


