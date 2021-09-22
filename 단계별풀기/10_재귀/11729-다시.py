def hanoi(n,_from,_to,_aux) :

    if n == 1 :
        print(str(_from)+' '+str(_to))
        return

    hanoi(n-1, _from, _aux, _to)
    print(str(_from)+' '+str(_to))
    hanoi(n-1, _aux, _to, _from)



n = int(input())

print(2**n-1)
hanoi(n, 1, 3, 2)