# Write your code here
cake = []


def cakes(eggs, butter, flour):
    egg = eggs / 5
    but = butter / 250
    flo = flour / 250
    cake.insert(1, egg)
    cake.insert(2, but)
    cake.insert(3, flo)
    print(min(cake))


cakes(15, 500, 1000)
