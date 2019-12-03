import constmod as cm
def arm(loadmass = cm.earthmass, unit = [1, 10], high = 0.001):
    """
    """
    if unit[0] == "mass":
        F0 = loadmass * cm.g
        F = unit[1] * cm.g
        ratio = F0/F
        S = high * ratio
        A = S*F
        t = ((2*S)**0.5)
        print("Отношение плеч =", ratio, "Работа =", A, "Путь =", S, "Время =", t)
    else:
        F0 = loadmass * cm.g
        ratio = F0/unit[1]
        S = high * ratio
        A = S*unit[1]
        print("Отношение плеч =", ratio, "Работа =", A, "Путь =", S)
arm()