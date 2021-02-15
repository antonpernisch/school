import math

def DrawShape():
    shape = input("What shape do you want to draw? \n 1. Square \n 2. Rectangle\n 3. Circle\n")
    if shape == "1" :
        size = input("How big should the square be?\n")
        try:
            Square(int(size))
        except:
            print("Size must be a number!")
            DrawShape()


    elif shape == "2":
        width = input("Width?\n")
        height = input("Height?\n")
        try:
            Rectangle(int(width), int(height))
        except:
            print("Width or height must be a number!")
            DrawShape()

    elif shape == "3":
        r = input("Radius? Accepting only odd numbers!\n")
        #try:
        Circle(int(r))
        #except:
            #print("Radius must be a number!")
            #DrawShape()
    
    else:
        print("Not a valid choice. Choose a number from options provided\n")
        DrawShape()

def Square(a):
    if a > 1 :
        print("#"*a)
        for i in range(0,a-2):
            # changed from a-2 to a-4, a-2 didn't work for me
            print("#"," "*(a-2),"#")
        print("#"*a)
    elif a == 1:
        print("#")
    else:
        print("Your size is not valid")

def Rectangle(w,h):
    if w == 1 and h == 1:
        print("#")
    elif w == 1 and h > 1:
        for i in range(h+1):
            print("#")
    elif w > 1 and h == 1:
        print("#"*w)
    elif w > 1 and h > 1:
        print("#"*w)
        for i in range(h-2):
            # for some weird reason, if i used w-2, it will put w spaces, even tho it's defined w-2
            # this problem was also in Square
            print("#", " "*(w-4), "#")
        print("#"*w)
    else:
        print("Your size is not valid")

def Circle(r):
    if r == 1:
        print("#")
    elif r%2 == 1 and r > 1: # we can accept only odd numbers, since we can't divide symbol in half...
        sn = (math.ceil(float(r)/2))-1 # calculate starting spaces
        snk = sn # keep the starting value for later use in algorithm 
        print(" "*sn, "#"*r)
        ins = r # inner spaces
        rc = 0 # row counter init
        while rc < snk:
            sn -= 1
            print(" "*sn, "#", " "*(ins-2), "#")
            ins += 2
            rc += 1
        for n in range(r):
            print("#", " "*(ins-2), "#")
        rc = 0
        while rc < snk:
            ins -= 2
            print(" "*sn, "#", " "*(ins-2), "#")
            sn += 1
            rc += 1
        print(" "*sn, "#"*r)
    else:
        print("Your size is not valid")


DrawShape()
