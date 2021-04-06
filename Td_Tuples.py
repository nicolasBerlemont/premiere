def quatreOperations(a,b):
    t = ( a+b, a-b, a*b, a//b)
    return t


#ex 3
t = (3,6,9,2)
def prefixe(t,e):
    tN = (e,) + (t)
    return tN

def suffixe(t,e):
    tN = (t) + (e,)
    return tN

def insere(t,e,i):
    for c in range(len(t)):
        tN = ()
        if c == i:
            tN = tN + (e[i])
        else:
            tN = tN + (t[i])
    return tN
  
  