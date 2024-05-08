'''
This is a file that contains the variables relieble for settings of some sort
'''
WIDTH = 1280
HEIGHT = 720
FPS = 3
TILESIZE = 18

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# X - border
# P - Podatkova
# ▓ - Park
# V - piana Vyshnya
# 0 - K2 florr 0
# 1 - K1
# C - Church
# I - IT-space
# Ø - Canteene
# ß - ЦШ (I don't know why)
UCU_MAP = [
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X','P','P','P','P','P','P','P','P','P','P',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X','P','P','P','P','P','P','P','P','P','P',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X','P','P','P','P','P','P','P','P','P','P',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X','P','P','P','P','P','P','P','P','P','P',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X','P','P','P','P','P','P','P','P','P','P',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X','P','P','P','P','P','P','P','P','P','P',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X','P','P','P','P','P','P','P','P','P','P',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','V','V','V','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','V','V','V','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','V','V','V','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','ß','ß','ß','ß','ß','ß','ß',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','I','I','I','I','I','I','I','I','I','I',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','I','I','I','I','I','I','I','I','I','I',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','I','I','I','I','I','I','I','I','I','I',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','I','I','I','I','I','I','I','I','I','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','I','I','I','I','I','I','I','I','I','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','I','I','I','I','I','I','I','I','I','I',' ',' ',' ',' ',' ',' ',' ','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','I','I','I','I','I','I','I','I','I','I',' ',' ',' ',' ',' ',' ',' ','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ','I','I','I','I','I','I','I','I','I','I',' ',' ',' ',' ',' ',' ',' ','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','1','1','1','1','1','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','1','1','1','1','1','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','1','1','1','1','1','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','▓','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]

print(UCU_MAP[-1][-1])