import sys
import math

class Method():
    def __init__(self, x0, y0, X, n):
        self.x0 = x0
        self.y0 = y0
        self.X = X
        self.set_n(n)
        self.c = self.get_c()
        self.solution = lambda x: self.c*math.pow(math.e, -x) + math.sin(x)/2.0 + math.cos(x)/2.0
        self.f = lambda x, y: math.cos(x) - y

    def plot(self):
        pass

    def get_c(self):
        return (self.y0 - math.sin(self.x0)/2.0 - math.cos(self.x0)/2.0)/(math.pow(math.e, -self.x0))

    def local_error(self):
        x, y = self.plot()
        error = [abs(self.solution(x[0]) - y[0])]
        for i in range(len(x[1:])):
            error.append(error[-1]+abs(self.solution(x[i]) - y[i]))
        return error

    def global_error(self, startn=1, finishn=100):
        errory, errorx = [], []
        last_h = self.h
        for i in range(startn, finishn+1):
            self.h = i
            self.step = (self.X - self.x0) / i
            lerror = self.local_error()
            errory.append(lerror[-1])
            errorx.append(i)
        self.set_n(last_h)
        return  errorx, errory

    def set_x0(self, x0):
        try:
            self.x0 = float(x0)
            self.c = self.get_c()
            self.step = (self.X-self.x0)/float(self.h)
        except BaseException:
            print('invalid x0')

    def set_y0(self, y0):
        try:
            self.y0 = float(y0)
            self.c = self.get_c()
        except BaseException:
            print('invalid y0')

    def set_X(self, X):
        try:
            self.X = float(X)
        except BaseException:
            print('invalid X')

    def set_n(self, n):
        try:
            self.h = int(n)
            self.step = (self.X-self.x0)/float(n)
        except BaseException:
            print('invalid n')