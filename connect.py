# modules
import sqlite3
import pygame as pg
import fight, score
from classes import *

# connecting database
con = sqlite3.connect('game.db')
cur = con.cursor() 

# creating a table - it happened once
#cur.execute('CREATE TABLE "user" (name TEXT NOT NULL, id INTEGER, score INTEGER DEFAULT 0,date text default CURRENT_DATE, time text default CURRENT_TIME, PRIMARY KEY(id AUTOINCREMENT))')

# initialization window
pg.init()
screen = pg.display.set_mode((1000, 600))
background = pg.image.load('assets/background/background.png').convert_alpha()
background = pg.transform.scale(background, (1000, 600))

# clock 
clock = pg.time.Clock()

#font
font = pg.font.Font('assets/fonts/turok.ttf',80)
txt_font = pg.font.Font('assets/fonts/turok.ttf', 32)


# create button
play_btn = Button(image=None, pos=(510, 400), text_input="PLAY", font=font, base_color="#ffffff", hovering_color="White")

# text boxes for inputs
player1 = InputBox(110, 225, 50, 40, txt_font)
player2 = InputBox(660, 225, 50, 40, txt_font)
players = [player1, player2]

# text above textboxes
username1, username2 = 'Player 1 Name :', 'Player 2 Name :'
name1=txt_font.render(username1,True,"#ffffff")
name2=txt_font.render(username2,True,"#ffffff")

# to check if the user want to quit
flag = 0
# running
running = True
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
        player1.handle_event(event)
        player2.handle_event(event)
                
        if event.type == pg.MOUSEBUTTONDOWN:
            if play_btn.checkForInput(click):
                cur.execute('insert into user (name) values (?)', (player1.text,))
                cur.execute('insert into user (name) values (?)', (player2.text,))
                con.commit()
                running = False
        elif key[pg.K_SPACE]:
            running = False
            cur.execute('insert into user (name) values (?)', (player1.text,))
            cur.execute('insert into user (name) values (?)', (player2.text,))
            con.commit()
    for player in players:
        player.update()
        player.draw(screen)
    
    screen.blit(name1,(110,175))
    screen.blit(name2,(660,175))
    pg.display.update()
    clock.tick(60)
    
    
    
# If the user clicked quit, the window will close
if flag:
    pg.quit()
else:
    playing = True
    fight.main(player1.text, player2.text)
    while playing:
        if score.flag or fight.flag:
            pg.quit()
            break
        # get the scores from the game
        updated_scores = fight.get_score()
        # get names of the player
        data = [name for name in cur.execute('select name from user')]
        names = [name[0] for name in data]
        # check names in database
        if player1 in names:
            cur.execute('update user set score= ? where name= ?', (updated_scores[0], player1,))
        if player2 in names:
            cur.execute('update user set score= ? where name= ?', (updated_scores[1], player2,))  
        # get top 10
        scores = cur.execute('select distinct * from user order by score desc limit 10')
        con.commit()
        # check if the user want to quit
        if not fight.flag:
            score.display(scores)
        # check if the user want to play again
        if score.play_again and not score.flag:
            pg.init()
            screen = pg.display.set_mode((1000, 600))
            background = pg.image.load('assets/background/background.png').convert_alpha()
            background = pg.transform.scale(background, (1000, 600))
            fight.main(player1.text, player2.text)
        elif score.flag or fight.flag:
            pg.quit()
            break

# close database
con.close()