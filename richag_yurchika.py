#import constmod
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

g = 9.8
r_e = 5

f_m = 4
s_m = 5
l_a = 30

def point_arm(first_mass, second_mass, lendth_arm):
    
    first_lendth = round((second_mass * lendth_arm) / (first_mass + second_mass), 2)
    second_lendth = round(lendth_arm - first_lendth, 2)
    return [first_lendth, second_lendth]

fig = plt.figure()
def circle_draw_func(x_centre=0, y_centre=0, Radius=100, N=360):
    """
    Пояснение будет писать егор...
    """
    x = np.zeros(N)
    y = np.zeros(N)
    alpha = np.linspace(0, 2*np.pi, N)
    for i in range(0, N, 1):
        x[i] = x_centre + Radius * np.cos(alpha[i])
        y[i] = y_centre + Radius * np.sin(alpha[i])
    return x, y

def triangle_draw_func(x=0, y=0):
    
    x = [x, x-r_e, x+r_e, x]
    y = [y, y-r_e, y-r_e, y]
    plt.plot(x, y, 'b')


'''
Ничего не понятно
'''
point_xn = point_arm(f_m, s_m, l_a)[0]
point_xk = point_arm(f_m, s_m, l_a)[1]
plt.plot([-1 * point_arm(f_m, s_m, l_a)[0], point_arm(f_m, s_m, l_a)[1]], [0, 0])
triangle_draw_func()
plt.plot( circle_draw_func(-point_xn, f_m, f_m)[0],  circle_draw_func(-point_xn, f_m, f_m)[1])
plt.plot( circle_draw_func(point_xk, s_m, s_m)[0], circle_draw_func(point_xk, s_m, s_m)[1] )
plt.axis('equal')
plt.show()

rng = arrange(-point_xn, point_xk, 0.01)
for i in rng:
    x, y = triangle_draw_func(x=i, y=0)
    obj, = plt.plot()