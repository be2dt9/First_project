import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import constmod as cm
lendth = 100
def arm(loadmass = 100, unit = [1, 10], high = 1):
    """
    """
    if unit[0] == "mass":
        F0 = loadmass * cm.g
        F = unit[1] * cm.g
        ratio = F0/F
        S = high * ratio
        A = S*F
        t = ((2*S/cm.g)**0.5)
        print("Отношение плеч =", round(ratio, 2), "Работа =", round(A, 2), "Путь =", round(S, 2), "Время =", round(t, 2))
        return ratio, A, S, t
    else:
        F0 = loadmass * cm.g
        ratio = F0/unit[1]
        S = high * ratio
        A = S*unit[1]
        print("Отношение плеч =", ratio, "Работа =", A, "Путь =", S)
        return ratio, A, S
arm()
fig = plt.figure()
def point_arm(first_mass=100, second_mass=10, lendth=100):
    
    first_lendth = round((second_mass * lendth) / (first_mass + second_mass), 2)
    second_lendth = round(lendth - first_lendth, 2)
    return [first_lendth, second_lendth]

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
    
    x = [x, x-5, x+5, x]
    y = [y, y-5, y-5, y]
    return x, y
x_move = np.linspace(point_arm()[1], 0, 100)
anim_list = []

point_xn = point_arm()[0]
point_xk = point_arm()[1]
plt.plot([-point_xn, point_xk], [0, 0], 'b')
plt.plot( circle_draw_func(-point_xn, 10, 10)[0],  circle_draw_func(-point_xn, 10, 10)[1])
plt.plot( circle_draw_func(point_xk, 1, 1)[0], circle_draw_func(point_xk, 1, 1)[1] )


for i in range(0, 100, 1):
    x, y = triangle_draw_func(x_move[i], 0)
    obj, = plt.plot(x, y, 'g')
    anim_list.append([obj])

plt.axis('equal')
ani = ArtistAnimation(fig, anim_list, interval=50)
ani.save('ani.gif')