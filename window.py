import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from deck import Deck
from game_table import table
class Intro():

    def __init__(self, variable):
        #setting up the window
        self.window = tk.Tk()
        self.window.configure(bg = 'green')
        #setting up the grid
        frame = tk.Frame(self.window, bg = 'green')
        frame.grid(row =0, column = 0)
        welcome = tk.Label(frame, bg= 'green', text= "Welcome to Blackjack", font=("Arial", 25), padx = 150, pady = 60)
        welcome.grid()
        minor_frame = tk.Frame(self.window, background='green', pady = 60)
        minor_frame.grid(row = 9, column = 0)
        #Handling the randomized image
        self.deck1 = Deck(1)
        self.image1 = Image.open("images/cards.png")
        coords = self.deck1.take_card().to_image()
        
        cropped_image = self.image1.crop((coords[0], coords[1], coords[2], coords[3]))
        card_img= ImageTk.PhotoImage(cropped_image)
        self.card_label = tk.Label(frame, image=card_img, background= 'green')
        self.card_label.grid(row = 3, column = 0)

        def close():
            variable.set(False)
            self.window.destroy()

        def play():
            variable.set(True)
            self.window.destroy()
        def random_card(event):
            if len(self.deck1.cards) == 0:
                self.deck1 = Deck(1)
            
            coords = self.deck1.take_card().to_image()
            print(coords)
            cropped_image = self.image1.crop((coords[0], coords[1], coords[2], coords[3]))
            
            card_img= ImageTk.PhotoImage(cropped_image)
            self.card_label.image = card_img
            self.card_label.configure(image = card_img)
            self.card_label.grid(row = 3, column = 0)
            self.card_label.bind("<Button-1>", random_card)
        
        self.card_label.bind("<Button-1>", random_card)

        tinyframe_1 = tk.Frame(minor_frame, bg = 'green', padx = 20)
        tinyframe_1.grid(row = 0, column = 1)
        tinyframe_2 = tk.Frame(minor_frame, bg = 'green', padx = 20)
        tinyframe_2.grid(row = 0, column = 2)


        play_button = ttk.Button(tinyframe_1, text="Play!", command = play)
        
        play_button.grid(row = 0, column = 0)
        quit_button = ttk.Button(tinyframe_2, text="Quit!", command = close)
        quit_button.grid(row = 0, column = 0)


        self.window.mainloop()


class Starter:

    def __init__(self,variable): 
         #setting up the window
        self.variable = variable
        self.window = tk.Tk()
        self.window.configure(bg = 'green')
        #setting up the grid
        frame = tk.Frame(self.window, bg = 'green')
        frame.grid(row =0, column = 0)
        welcome = tk.Label(frame, bg= 'green', text= "Select your starting bet", font=("Arial", 25), padx = 150, pady = 60)
        welcome.grid()
        minor_frame = tk.Frame(self.window, background='green', pady = 60)
        minor_frame.grid(row = 9, column = 0)
        tinyframe_1 = tk.Frame(minor_frame, bg = 'green', padx = 20)
        tinyframe_1.grid(row = 0, column = 1)
        tinyframe_2 = tk.Frame(minor_frame, bg = 'green', padx = 20)
        tinyframe_2.grid(row = 0, column = 2)
        tinyframe_3 = tk.Frame(minor_frame, bg = 'green', padx = 20)
        tinyframe_3.grid(row = 0, column = 3)
        tinyframe_4 = tk.Frame(minor_frame, bg = 'green', padx = 20)
        tinyframe_4.grid(row = 0, column = 4)
        
        def set_vary_5():
            self.variable.set(5.00)
            print(self.variable.get())
        def set_vary_10():
            self.variable.set(10.00)
            print(self.variable.get())
        def set_vary_15():
            self.variable.set(10.00)
            print(self.variable.get())
        def set_vary_20():
            self.variable.set(10.00)
            print(self.variable.get())


        ##Betting buttons
        five_bet = ttk.Button(tinyframe_1, text="$5.00", command = set_vary_5)
        
        five_bet.grid(row = 0, column = 0)
        ten_bet = ttk.Button(tinyframe_2, text="$10.00", command = set_vary_10)
        
        ten_bet.grid(row = 0, column = 0)
        fifteen_bet = ttk.Button(tinyframe_3, text="$15.00", command = set_vary_15)
        
        fifteen_bet.grid(row = 0, column = 0)
        twenty_bet = ttk.Button(tinyframe_4, text="$20.00", command = set_vary_20)
        
        twenty_bet.grid(row = 0, column = 0)

        self.window.mainloop()