from turtle import Turtle
t = Turtle()

while True:
    Mov_back_forw = str(input('The Turtle should move forward or backward? type forw or back Forw(Forward) B(Backward): ')).lower()
    Mov_sides = str(input('The Turtle should turn to left or right? Type R(Right) ou L(Left): ' )).lower()
    Pos = int(input("How many degrees do you want to turn? "))
    speed = int(input("How many pixels do you want to move? "))
    
    if Mov_back_forw == 'forw' or Mov_back_forw == 'f' and Mov_sides == 'r':
        t.forward(speed) 
        t.right(Pos)
    elif Mov_back_forw == 'forw' or Mov_back_forw == 'f' and Mov_sides == 'l':
        t.forward(speed)
        t.left(Pos)
    elif Mov_back_forw == 'back' or Mov_back_forw == 'b' and Mov_sides == 'r':
        t.backward(speed)
        t.right(Pos)
    elif Mov_back_forw == 'back' or Mov_back_forw == 'b' and Mov_sides == 'l':
        t.backward(speed)
        t.left(Pos)
        
    decisao = input("Do you want to still Drawing? ").lower()
    
    if decisao == 'no' or decisao == 'n':
        print("Closing the draw graphics")
        break