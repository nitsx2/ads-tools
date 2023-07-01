class DSU():
    def __init__(self, nodes):
        self.parent = [i for i in range(nodes)]
        self.height = [1 for _ in range(nodes)]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.height[x] > self.height[y]:
            self.parent[y] = x
        elif self.height[y] > self.height[x]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.height[x] += 1

    def find(self, x):
        if self.parent[x] != x:
            parent = self.find(self.parent[x])
        self.parent[x] = parent
        return self.parent[x]