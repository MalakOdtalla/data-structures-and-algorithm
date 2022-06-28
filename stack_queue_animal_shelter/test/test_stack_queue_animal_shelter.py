from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter,Cat,Dog

def test_enqueu():
    animals = AnimalShelter()
    A = Dog('A')
    B= Dog('B')
    M = Cat('M')
    K = Cat('K')
    animals.enqueue(A)
    animals.enqueue(B)
    animals.enqueue(M)
    animals.enqueue(K)

    expected = ('A', 'B', 'M', 'K')
    actual = A.name ,B.name, M.name,K.name
    assert expected == actual



def test_dequeue_cat():
    animals = AnimalShelter()
    A = Dog('alex')
    B = Dog('Aln')
    M = Cat('M')
    K = Cat('K')
    animals.enqueue(A)
    animals.enqueue(B)
    animals.enqueue(M)
    animals.enqueue(K)

    expected = 'M'
    actual = animals.dequeue('cat')
    assert expected == actual

def test_dequeue_dog():
    animals = AnimalShelter()
    A = Dog('alex')
    B = Dog('Aln')
    M = Cat('M')
    K = Cat('K')
    animals.enqueue(A)
    animals.enqueue(B)
    animals.enqueue(M)
    animals.enqueue(K)

    expected = 'B'
    actual = animals.dequeue('dog')
    assert expected == actual

def test_dequeue_any():
    animals = AnimalShelter()
    A = Dog('A')
    M = Cat('M')
    animals.enqueue(A)
    animals.enqueue(M)

    expected = None
    actual = animals.dequeue('any')
    assert expected == actual