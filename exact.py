import math
from method import Method

class Exact(Method):
    def __init__(self, x0, y0, X, n):
        super(Exact, self).__init__(x0, y0, X, n)

    def plot(self):
        x = [self.x0]
        y = [self.y0]
        for i in range(int(self.h)):
            y.append(self.solution(x[-1]+self.step))
            x.append(x[-1]+self.step)
        return x, y


