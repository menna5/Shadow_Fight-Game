from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import fight

# bg color
color = '#71556C'
flag = False
play_again = False
def display(scores):
    master = Tk()
    master.title('Score')
    master.geometry('1000x600')
    master.configure(bg='#86514D')
    img = Image.open("assets/background/background.png")
    img = img.resize((1000,600))
    img = ImageTk.PhotoImage(img)
    lbl = Label(master,image=img)
    lbl.pack(side='top',fill=Y,expand=True)
    game_frame = Frame(master)
    game_frame.pack()
    
    # scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)
    
    game_scroll = Scrollbar(game_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)
    
    my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)
    
    my_game.pack()
    
    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)
    
    # define our column
    
    my_game['columns'] = ('player_rank', 'player_name', 'player_score', 'Date', 'Time')
    
    # format our column
    my_game.column("#0", width=0, stretch=NO)
    my_game.column("player_rank", anchor=CENTER, width=100)
    my_game.column("player_name", anchor=CENTER, width=100)
    my_game.column("player_score", anchor=CENTER, width=100)
    my_game.column("Date", anchor=CENTER, width=100)
    my_game.column("Time", anchor=CENTER, width=100)
    
    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("player_rank", text="Rank", anchor=CENTER)
    my_game.heading("player_name", text="Name", anchor=CENTER)
    my_game.heading("player_score", text="Score", anchor=CENTER)
    my_game.heading("Date", text="Date", anchor=CENTER)
    my_game.heading("Time", text="Time", anchor=CENTER)
    
    # add data
    i = 1
    for score in scores:
        my_game.insert(parent='', index='end', text='', values=(f'{i}', f'{score[0]}', f'{score[2]}', f'{score[3]}', f'{score[4]}'))
        i += 1
    my_game.pack()
    
    frame = Frame(master)
    frame.pack(pady=40, padx=50)
    
    def playAgain():
        global flag
        flag = False
        play_again = True
        master.destroy()
        
    def quitt():
        global flag
        flag = True
        master.destroy()   
    
    
    # Buttons
    play_btn = Button(master, text = "Play Again", command = playAgain)
    play_btn.pack(pady=10)
    quit_btn = Button(master, text = "Quit", command = quitt)
    quit_btn.pack(pady=10)
    master.mainloop()