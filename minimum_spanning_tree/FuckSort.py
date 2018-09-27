class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost

    def __repr__(self):
            return "({},{},{})".format(self.city1, self.city2, self.cost)


c1 = Connection("Acity", "Bcity", 2)
c2 = Connection("Acity", "Ccity", 2)
c3 = Connection("Bcity", "Ccity", 3)

connections = [c3, c2, c1]
print(connections)
print(sorted(connections, key=lambda c: (c.cost, c.city1, c.city2)))
# [(Bcity, Ccity, 3), (Acity, Ccity, 2), (Acity, Bcity, 2)]
# [(Acity, Bcity, 2), (Acity, Ccity, 2), (Bcity, Ccity, 3)]
