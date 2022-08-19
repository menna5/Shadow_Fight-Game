import pygame, threading

def first_page():
    
    # initialization
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Loading..')
    
    Font = pygame.font.SysFont('Inter', 100)
    
    
    # clock 
    clock = pygame.time.Clock()
    
    # work
    WORK = 1000000
    
    # BG
    loading_bg = pygame.image.load("assets\Loading Bar Background.png")
    loading_bg_rect = loading_bg.get_rect(center=(640, 360))
    
    # loading bar
    loading_bar = pygame.image.load("assets\Loading Bar.png")
    loading_bar_rect = loading_bar.get_rect(midleft=(320, 180))
    loading_progress = 0
    loading_bar_width = 2
    loading_finish = False
    
    #text
    text = Font.render('Getting into the game ..', False, '#ffffff')
    textRect = text.get_rect(center=(625, 200))
    
    def doWork():
        global loading_progress, loading_finish
        
        for i in range(WORK):
            delay = 12526348 / 1323648 * 1236546
            loading_progress = i
        loading_finish = True
        
    # Thread
    threading.Thread(target=doWork).start()
    
    # running
    running = True
    flag = 0
    # get Keypresses.
    while running:
        screen.fill('#0d0e2e')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                flag = 1
        if not loading_finish:
            loading_bar_width = int(loading_progress / WORK * 720)
            loading_bar = pygame.transform.scale(loading_bar, (loading_bar_width, 150))
            loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
            screen.blit(text, textRect)
            screen.blit(loading_bg, loading_bg_rect)
            screen.blit(loading_bar, loading_bar_rect)
        else:
            break
        if flag:
            pygame.quit()
        else:
            pygame.display.update()
            clock.tick(60)
first_page()
