def abrir (mapa):
    return [x.split() for x in open (mapa, 'r')]

def recorrer (mapa, x, y):
    if y==(len(mapa[x])-1) and x==(len(mapa)-1):
        return True
    elif y<(len(mapa[x])-1):
        return recorrer (mapa,x,y+1)
    elif x<(len(mapa)-1):
        return recorrer (mapa.x+1,0)
    else:
        return False
def rec(mapa,x,y):
    if x==(len(mapa)):
        return True
    elif x<(len(mapa)):
        print(mapa[x])
        return rec (mapa.x+1,0)
    else:
        return False

print(rec(abrir('mapa.txt'),0,0))
