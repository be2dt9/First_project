import constmod as cm
def arm(loadmass = cm.earthmass, unit = ["mass", 60], high = 0.01, g = cm.g):
    """ Функция рассчитывающая работу(A), перемещение(S), отношение плеч(ratio) и
	время(t)(в зависимости от входных данных) по заданным аргументам: масса 
	груза(load mass); единица измерения и ее значение(unit["", amount]);
	высоту на которую необходимо поднять груз(high); гравитация(g).
    """
    if unit[0] == "mass":
        F0 = loadmass * g
        F = unit[1] * g
        ratio = F0/F
        S = high * ratio
        A = S*F
        if (2*g*S)**0.5 > cm.c:
            tacceleration = cm.c/g #время через которое точка достигнет скорости света
            Sacceleration = tacceleration**2*g/ 2 #расстояние которое тело пройдет с ускорением
            t = tacceleration + (S - Sacceleration)/cm.c
        else:
            t = (2*S/g)**0.5
        print("Отношение плеч =", ratio, "Работа =", A, "Перемещение =", S, "Время =", t)
    else:
        F0 = loadmass * g
        ratio = F0/unit[1]
        S = high * ratio
        A = S*unit[1]
        print("Отношение плеч =", ratio, "Работа =", A, "Перемещение =", S)
arm()
