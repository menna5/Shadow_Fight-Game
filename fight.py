import pygame as pg
import pygame.mixer
from pygame import mixer
from fighter import Fighter

score=[0, 0] #player scores [p1,p2]
flag  = False
def main(player1, player2):
    global flag 
    mixer.init()
    
    # sets the frame rate of the game to suit all computers.
    clock = pg.time.Clock()
    fps = 60
    
    #define colors
    white=(255,255,255)
    
    #define game variables
    global score #player scores [p1,p2]
    intro_count=3
    last_count_update=pg.time.get_ticks()
    round_over =False
    ROUND_OVER_COOLDOWN=2000
    
    # window size.
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    
    # sets the display size of the game.
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # sets the name on the bar of the game.
    pg.display.set_caption('Arena')
    
    # loading background images.
    background_img = pg.image.load('assets/background/background.png').convert_alpha()
    
    
    # define fighter variables.
    WARRIOR_SIZE = 162
    WARRIOR_SCALE = 4
    WARRIOR_OFFSET = [72, 56]
    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE,WARRIOR_OFFSET]
    WIZARD_SIZE = 250
    WIZARD_SCALE = 3
    WIZARD_OFFSET = [112, 107]
    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
    
    
    #load music and sounds
    pg.mixer.music.load("assets/audio/music.mp3")
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1,0.0,5000)
    sword_fx =pg.mixer.Sound("assets/audio/sword.wav")
    sword_fx.set_volume(0.5)
    magic_fx =pg.mixer.Sound("assets/audio/magic.wav")
    magic_fx.set_volume(0.75)
    
    
    # load spreadsheets.
    warrior_sheet = pg.image.load('assets/warrior/warrior.png').convert_alpha()
    wizard_sheet = pg.image.load('assets/wizard/wizard.png').convert_alpha()
    
    #load victory image
    victory_img= pg.image.load("assets/icons/victory.png").convert_alpha()
    
    
    # number of frames in each animation.
    WARRIOR_ANIMATION_FRAMES = [10, 8, 1, 7, 7, 3, 7]
    WIZARD_ANIMATION_FRAMES = [8, 8, 1, 8, 8, 3, 7]
    
    
    # define fonts
    victory_font=pg.font.Font('assets/fonts/turok.ttf',80)
    count_font=pg.font.Font('assets/fonts/turok.ttf',80)
    score_font=pg.font.Font('assets/fonts/turok.ttf',30)
    
    
    # function for drawing test
    def draw_text(text,font,text_color,x,y):
        img=font.render(text,True,text_color)
        screen.blit(img,(x,y))
    
    
    # function for drawing background.
    def draw_bg():
        scaled_bg = pg.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))
    
    
    #function for drawing fighters health bars
    def draw_health_bar(health,x,y):
        ratio=health/100
        pg.draw.rect(screen,'#4C4862',(x-2,y-2,404,34))
        pg.draw.rect(screen,'#4C4862',(x,y,400,30))
        pg.draw.rect(screen,'#20192B',(x,y,400*ratio,30))
    
    
    
    # creating objects of class.
    fighter_1 = Fighter(1,  200, 310, False ,WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_FRAMES, sword_fx)
    fighter_2 = Fighter(2,  700, 310,  True,WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_FRAMES, magic_fx)
    
    
    active = True
    flag = 0
    
    # controls the boot of the game.
    while active:
    
        #Game.first_page()
        
        # calling the set frame rate function.
        clock.tick(fps)
    
        # calling the draw background function.
        draw_bg()
    
        #show player stats
        draw_health_bar(fighter_1.health,20,20)
        draw_health_bar(fighter_2.health,580,20)
        draw_text(player1,score_font,'#ffffff' , 20 , 60)
        draw_text(player2,score_font,'#ffffff' , 577 , 60)
    
    
    
        # update countdown
        if intro_count<=0:
    
            # move players.
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2 , round_over)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1, round_over)
        else:
            # display count timer
            draw_text(str(intro_count),count_font,"#ffffff",SCREEN_WIDTH/2,SCREEN_HEIGHT/3)
            # update count timer
            if (pg.time.get_ticks()-last_count_update)>=1000:
                intro_count-=1
                last_count_update=pg.time.get_ticks()
    
    
        # update fighters.
        fighter_1.update()
        fighter_2.update()
    
        # draw players.
        fighter_1.draw(screen)
        fighter_2.draw(screen)
    
    
        #check for player defeat
        if round_over == False:
            if fighter_1.alive == False or fighter_2.alive == False:
                score[0] += fighter_1.score
                score[1] += fighter_2.score
                round_over = True
                round_over_time = pg.time.get_ticks()
        else:
            # display victory text
            draw_text('Game Over',victory_font,"#ffffff",330, 150)
            if pg.time.get_ticks() -round_over_time > ROUND_OVER_COOLDOWN:
                round_over = False
                intro_count = 3
                pg.quit()
                break
                
        # get the event from event handler func in pygame module.
        # if the event is "QUIT", it stops running the game.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                active = False
                flag = True
        if flag:
            pg.quit()
            break
        else:
            # updates the display of the game.
            pg.display.update()    

def get_score():
    global score
    return score