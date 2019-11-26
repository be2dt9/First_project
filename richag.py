#import constmod
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

first_mass = 4
second_mass = 2
lendth_arm = 6

first_lendth = (second_mass * lendth_arm) / (first_mass + second_mass)
second_lendth = lendth_arm - first_lendth

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

def triangle_draw_func(x_fir=0, y_fir=0,
                       x_sec=-1, y_sec=-1,
                       x_thr=1, y_thr=-1):
    
    x = [x_fir, x_sec, x_thr, x_fir]
    y = [y_fir, y_sec, y_thr, y_fir]
    plt.plot(x, y, 'b')

triangle_draw_func()
plt.show()