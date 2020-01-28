import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

#переменные велечины
seconds_in_year = 365 * 24 *60 * 60
seconds_in_day = 24 * 60 * 60
years = 3
t = np.arange(0,years*seconds_in_year,seconds_in_day)
#опреде функцию для си-мы диф. ур-ий
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3) = s
     
     #динамика первого тела под 2 и 3
    dxdt1 = v_x1
    dv_xdt1 = (- G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
                - G * m3 * (x1 - x3) / ((x1 - x3)**2  + (y1 - y3)**2)**1.5)
    dydt1 = v_y1
    dv_ydt1 = (- G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
                - G * m2 * (y1 - y3) / ((x1 - x3)**2  + (y1 - y3)**2)**1.5)
     #динамика второго  тела под 1 и 3
    dxdt2 = v_x2
    dv_xdt2 = (- G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
                - G * m3 * (x2 - x3) / ((x2 - x3)**2  + (y2 - y3)**2)**1.5)
    dydt2 = v_y2
    dv_ydt2 = (- G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
                - G * m3 * (y2 - y3) / ((x2 - x3)**2  + (y2 - y3)**2)**1.5)
     #динамика третьего  тела под 1 и 2
    dxdt3 = v_x3
    dv_xdt3 = (- G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
                - G * m2 * (x3 - x2) / ((x3 - x2)**2  + (y3 - y2)**2)**1.5)
    dydt3 = v_y3
    dv_ydt3 = (- G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
                - G * m2 * (y3 - y2) / ((x3 - x2)**2  + (y3 - y2)**2)**1.5)
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3)
     
 #определяем нач значения и параметры
x10 = - 6.15*149.68*10**9
v_x10 = 0
y10 = 0
v_y10 = 15000

x20 = 6.15*149.68*10**9
v_x20 = 0
y20 = 0
v_y20 = 10000

x30 = 2.15*149.68*10**9
v_x30 = 0
y30 = 0
v_y30 =  20000
     
s0 = (x10, v_x10,y10,v_y10,
      x20, v_x20,y20,v_y20,
      x30, v_x30,y30,v_y30)    
m1 = (1.99*10**30) * 1.06
m2 =(1.99*10**30) * 0.6
m3 = (1.99*10**30) * 0.3
G = 6.67 * 10**(-11)
# решаем с-му ур-ий
sol = odeint(move_func, s0, t)
# строрим решение в виде графика
fig = plt.figure()
bodys = []
for i in range(0, len(t), 1):
    body1, = plt.plot(sol[:i,0], sol[:i,2],'-',color='r')
    body1_line, = plt.plot(sol[:i,0], sol[:i,2],'-',color='r')
    
    body2, = plt.plot(sol[:i,4], sol[:i,6],'-',color='g')
    body2_line, = plt.plot(sol[:i,4], sol[:i,6],'-',color='g')
    
    body3, = plt.plot(sol[:i,8], sol[:i,10],'-',color='b')
    body3_line, = plt.plot(sol[:i,8], sol[:i,10],'-',color='b')
    
    bodys.append([body1,body1_line,body2,body2_line,body3,body3_line])
ani = ArtistAnimation(fig, bodys, interval=20)
plt.axis('equal')
ani.save("1.gif")
    

