import math

def kleiner(a,b):
    if a<b:
        return a
    else:
        return b

#überpruefung
print(kleiner(6,9))
def longest(wort_1,wort_2,wort_3):
    return max((len(wort_1),len(wort_2),len(wort_3)))

#überpruefung
print(longest("asd", "asdefr","asdasdasdsasdas"))


    


def pythagoras(a,b):
    c=math.sqrt((a**2)+(b**2))

    return c
    
#überpruefung
print(pythagoras(4,8))

def umfangRechteck(a, b):
    return (2*(a+b))

#überpruefung
print(umfangRechteck(2,4)) 

def flaecheKugel(r):
    return (4 *math.pi *r**2)

#überpruefung
print(flaecheKugel(10))

def notenberechnung(max, erreichte):
    note=erreichte/max*5+1
    return(note)

#überpruefung
print(notenberechnung(41,41))
