import math
from method import Method

class RungeKutta(Method):
    def __init__(self, x0, y0, X, n):
        super(RungeKutta, self).__init__(x0, y0, X, n)

    def plot(self):
        x = [self.x0]
        y = [self.y0]
        k2 = lambda x, y, h: self.f(x + h / 2.0, y + (h / 2.0) * self.f(x, y))
        k3 = lambda x, y, h: self.f(x + h / 2.0, y + (h / 2.0) * k2(x, y, h))
        k4 = lambda x, y, h: self.f(x + h, y + h * k3(x, y, h))
        for i in range(int(self.h)):
            yn = y[-1] + (self.step / 6.0) * (self.f(x[-1], y[-1]) + k2(x[-1], y[-1], self.step) * 2.0 + k3(x[-1], y[-1], self.step) * 2.0 + k4(x[-1], y[-1], self.step))
            x.append(x[-1]+self.step)
            y.append(yn)
        return x, y