import sys
import math
from method import Method

class Euler(Method):
    def __init__(self, x0, y0, X, n):
        super(Euler, self).__init__(x0, y0, X, n)

    def plot(self):
        x = [self.x0]
        y = [self.y0]
        for i in range(int(self.h)):
            yn = y[-1] + self.step * self.f(x[-1], y[-1])
            x.append(x[-1]+self.step)
            y.append(yn)
        return x, y
