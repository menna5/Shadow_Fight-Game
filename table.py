from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import fight

check = 0
def display(scores):
    master = Tk()
    master.title('Score')
    master.geometry('1000x600')
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
    
    my_game['columns'] = ('player_id', 'player_name', 'player_Rank')
    
    # format our column
    my_game.column("#0", width=0, stretch=NO)
    my_game.column("player_id", anchor=CENTER, width=100)
    my_game.column("player_name", anchor=CENTER, width=100)
    my_game.column("player_Rank", anchor=CENTER, width=100)
    
    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("player_id", text="Id", anchor=CENTER)
    my_game.heading("player_name", text="Name", anchor=CENTER)
    my_game.heading("player_Rank", text="Rank", anchor=CENTER)
    
    # add data
    for score in scores:
        my_game.insert(parent='', index='end', text='',
                       values=(f'{score[0]}', f'{score[1]}', f'{score[2]}'))
    my_game.pack()
    
    frame = Frame(master)
    frame.pack(pady=20)
    
    def playAgain():
        global check
        check = 1
        master.destroy()
    
    
    # Buttons
    play_btn = Button(master, text = "Play Again", command = playAgain)
    play_btn.pack(pady=10)
    quit_btn = Button(master, text = "Quit", command = master.destroy)
    quit_btn.pack(pady=10)
    master.mainloop()

def flag():
    return check
