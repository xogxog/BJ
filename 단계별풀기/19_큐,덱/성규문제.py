import math

def my_pi(cnt, c, S, S1) :
    if cnt == 20 :
        c = c/2
        S = (math.sin(c))**2
        S1 = S / (2+(2*((1-S)**(1/2))))

        return c,S,S1


    else :
        c,S,S1= my_pi(cnt+1,c,S,S1)
    c = c / 2
    S = (math.sin(c)) ** 2
    S1 = (S / (2 + (2 * ((1 - S) ** (1 / 2)))))
    P = 2 * ((S1) ** (1 / 2))

    return c,S,S1


n = 2
ceta = math.pi / (2**(n-1))
Sn = math.sin(ceta)**2
Sn_plus_1 = Sn / (2+(2*math.sqrt(1-Sn)))



_ceta, _Sn, _Sn_Plus_1 = my_pi(3, ceta, Sn, Sn_plus_1)

Pn = (2**20)*(math.sqrt(_Sn_Plus_1))

print(Pn)


