# 집 그리는 프로그램

from graphics import *
win = GraphWin("집 그리는 프로그램", 1280,720)
win.setBackground("white")

P1 = win.getMouse()
P1.draw(win)
P2 = win.getMouse()

Rec = Rectangle(P1,P2)
Rec.draw(win)

# 폭
if P1.getX() > P2.getX() :
    R1_W = P1.getX() - P2.getX()
else :
    R1_W = P2.getX() - P1.getX()

# 집 바닥

if P1.getY() > P2.getY() :
    R1_B = P1.getY()
else :
    R1_B = P2.getY()

P3 = win.getMouse()

Rec2_P1 = Point(P3.getX() - (R1_W / 5 / 2), P3.getY())
Rec2_P2 = Point(P3.getX() + (R1_W / 5 / 2), R1_B)

Rec2 = Rectangle(Rec2_P1, Rec2_P2)
Rec2.draw(win)

# 문 끝!

# 문 폭

if Rec2_P1.getX() > Rec2_P2.getX() :
    R2_W = Rec2_P1.getX() - Rec2_P2.getX()
else :
    R2_W = Rec2_P2.getX() - Rec2_P1.getX()
    
P4 = win.getMouse()

S_P1 = Point(P4.getX() - (R2_W/4), P4.getY() +(R2_W/4))
S_P2 = Point(P4.getX()+R2_W/4,P4.getY()-R2_W/4)

S1 = Rectangle(S_P1,S_P2)
S1.draw(win)

# 창문 끝!

P5 = win.getMouse()
L1 = Line (P5,Rec.getP1())
L2 = Line (P5,Point(Rec.getP2().getX(), Rec.getP1().getY()))
L1.draw(win)
L2.draw(win)
