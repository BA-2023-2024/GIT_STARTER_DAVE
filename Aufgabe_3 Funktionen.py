def Zahlen_einlesen():
    a=int(input("Gib eine Zahl an: "))
    b= int(input("Gib eine zweite Zahl an: " ))
    result=a+b
    return result

print(Zahlen_einlesen())

def multiplizieren(a,b):
    return a*b

print(multiplizieren(3,5))
    


def quader(länge,höhe,breite):
    volume=länge*höhe*breite
    oberfläche= 2*(länge*höhe+länge*breite+höhe*breite)
    return volume,oberfläche

print(quader(2,6,4))

      
    
