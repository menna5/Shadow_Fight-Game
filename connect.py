# modules
import sqlite3
import pygame as pg
import threading
import fight, table

# connecting database
con = sqlite3.connect('game.db')
cur = con.cursor() 
# creating a table 
#cur.execute('CREATE TABLE "user" (name TEXT NOT NULL, id INTEGER, score INTEGER DEFAULT 0,date text default CURRENT_DATE, time text default CURRENT_TIME, PRIMARY KEY(id AUTOINCREMENT))')\

cur.execute('insert into user (name) values (\'Mena\')')
scores = cur.execute('select * from users limit 10 ord dec')
con.commit()
con.close()

# initialization
pg.init()
screen = pg.display.set_mode((1000, 600))
background = pg.image.load('assets/background/background.png').convert_alpha()
background = pg.transform.scale(background, (1000, 600))
# clock 
clock = pg.time.Clock()

#font
font = pg.font.Font('assets/fonts/turok.ttf',80)

# running
running = True
# get Keypresses.
while running:
    key = pg.key.get_pressed()
    screen.fill('#0d0e2e')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
    pg.display.set_caption('Arena')
    # background
    screen.blit(background, (0, 0))
    
    if key[pg.K_UP]:
        break
    
    pg.display.update()
    clock.tick(60)
    
fight.main()
table.display(scores)

if table.flag():
    pg.init()
    screen = pg.display.set_mode((1000, 600))
    background = pg.image.load('assets/background/background.png').convert_alpha()
    background = pg.transform.scale(background, (1000, 600))
    fight.main()
else:
    pg.quit()