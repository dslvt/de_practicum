import sys
import math
import matplotlib.pyplot as plt


class B():
    def __init__(self, x0, y0, X, n):
        self.x0 = x0
        self.y0 = y0
        self.h = n
        self.step = (X-x0)/n
        self.max_y = 2

    def exact(self):
        x = [self.x0]
        y = [self.y0]
        for i in range(int(self.h)):
            yn = solu(x[-1] + self.step)
            x.append(x[-1] + self.step)
            y.append(yn)
        return x, y

    def euler(self):
        x = [self.x0]
        y = [self.y0]
        for i in range(int(self.h)):

            yn = y[-1] + self.step * f(x[-1], y[-1])
            if yn > self.max_y or yn < -self.max_y:
                print('a')
                ex, ey = self.exact()
                yn = ey[i]
            print(yn)
            x.append(x[-1] + self.step)
            y.append(yn)
        return x, y

def solu(x):
    if (sol1(x)<0):
        return 3.1748/(-pow(math.fabs(sol1(x)), (1/3.0)))
    else:
        return 3.1748/(pow(sol1(x), (1/3.0)))

k2 = lambda x, y, h: f(x + h / 2.0, y + (h / 2.0) * f(x, y))
k3 = lambda x, y, h: f(x + h / 2.0, y + (h / 2.0) * k2(x, y, h))
k4 = lambda x, y, h: f(x + h, y + h * k3(x, y, h))

f = lambda x, y: ((math.pow(y, 4.0))*math.cos(x)-y*math.tan(x))
sol1 = lambda x: (36.0*x+24.0*math.sin(2.0*x)+3.0*math.sin(4.0*x)-32.0)*(-(1.0/math.cos(x) ** 3.0))
sol = lambda x: 3.1748/(pow(sol1(x), (1/3.0)))

sh = lambda x:((36*x+24*math.sin(2*x)+3*math.sin(4*x)-32)*(-math.pow(1/math.cos(x), 3)))


# real_x = [0.0]
# real_y = [1.0]
# last_x = 8.0
#
# h = 10000
# step = (last_x-real_x[0])/h
# for i in range(int(h)):
#     y = solu(real_x[-1]+step)
#     real_x.append(real_x[-1]+step)
#     real_y.append(y)
# #     print(real_x[-1]+step, y)
#
# plt.plot(real_x, real_y)
# plt.grid(True, which='both')
#
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
#
# eulerx = [0.0]
# eulery = [1.0]
# last_x = 8.0
#
# h = 100000
# step = (last_x - eulerx[0]) / h
# for i in range(int(h)):
#     y = eulery[-1] + step * f(eulerx[-1], eulery[-1])
#     #     print(eulerx[-1]+step, y)
#     eulerx.append(eulerx[-1] + step)
#     eulery.append(y)
#
# plt.plot(eulerx, eulery)
# plt.grid(True, which='both')
#
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
#
# runge_x = [0.36480000000000223]
# runge_y = [-7.882102832312473]
# last_x = 8.0
#
# h = 100000
# step = (last_x - runge_x[0]) / h
# for i in range(int(h)):
#     x, y = runge_x[-1], runge_y[-1]
#     y = y + (step / 6.0) * (f(x, y) + k2(x, y, step) * 2.0 + k3(x, y, step) * 2.0 + k4(x, y, step))
#
#     #     print(runge_x[-1]+step, y)
#     runge_x.append(x + step)
#     runge_y.append(y)
#
# plt.plot(runge_x, runge_y)
# plt.grid(True, which='both')
#
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')