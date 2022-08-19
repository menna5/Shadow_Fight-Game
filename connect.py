# modules
import sqlite3
import pygame as pg
import fight, table
from button import Button

# connecting database
con = sqlite3.connect('game.db')
cur = con.cursor() 
# creating a table 
#cur.execute('CREATE TABLE "user" (name TEXT NOT NULL, id INTEGER, score INTEGER DEFAULT 0,date text default CURRENT_DATE, time text default CURRENT_TIME, PRIMARY KEY(id AUTOINCREMENT))')\

scores = cur.execute('select * from user order by score desc limit 10')
con.commit()

# initialization window
pg.init()
screen = pg.display.set_mode((1000, 600))
background = pg.image.load('assets/background/background.png').convert_alpha()
background = pg.transform.scale(background, (1000, 600))
# clock 
clock = pg.time.Clock()

#font
font = pg.font.Font('assets/fonts/turok.ttf',80)

# create button
play_btn = Button(image=None, pos=(510, 400), text_input="PLAY", font=font, base_color="#ffffff", hovering_color="White")

# running
running = True
flag = 0
# get Keypresses.
while running:
    pg.display.set_caption('Arena')
    # background
    screen.blit(background, (0, 0))
    
    # check keyboard and mouse to start 
    key = pg.key.get_pressed()
    click = pg.mouse.get_pos()
    
    # show the button
    play_btn.update(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            flag = 1
        if event.type == pg.MOUSEBUTTONDOWN:
            if play_btn.checkForInput(click):
                running = False
        elif key[pg.K_SPACE]:
            running = False

    pg.display.update()
    clock.tick(60)
# If the user clicked quit, the window will close
if flag:
    pg.quit()
else:
    fight.main()
    scores = cur.execute('select * from user order by score desc limit 10')
    con.commit()
    if not fight.check():
        table.display(scores)
    if table.flag():
        pg.init()
        screen = pg.display.set_mode((1000, 600))
        background = pg.image.load('assets/background/background.png').convert_alpha()
        background = pg.transform.scale(background, (1000, 600))
        fight.main()
        scores = cur.execute('select * from user order by score desc limit 10')
        con.commit()
        if not fight.check():
            table.display(scores)
    else:
        pg.quit()
con.close()
