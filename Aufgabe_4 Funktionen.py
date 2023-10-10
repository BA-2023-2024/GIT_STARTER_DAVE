

def Quadrant_1(x,y):
    if(x<0 and y<0):
        print("Dritter Quadrant.")
    elif(x<0 and y>0):
        print("Vierter Quadrant.")
    elif(x>0 and y>0):
        print("Erster Quadrant.")
    else:
        print("Zweiter Quadrant.")

y=float(input("Erste Kordinate?: "))
x=float(input("Zweite Kordinate?: "))

Quadrant_2= Quadrant_1(x,y)
