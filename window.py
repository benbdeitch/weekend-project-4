import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from deck import Deck

from player import Player
class Intro():

    def __init__(self, variable):
        #setting up the window
        self.window = tk.Tk()
        self.window.configure(bg = 'green')
        #setting up the grid
        self.frame = tk.Frame(self.window, bg = 'green')
        self.frame.grid(row =0, column = 0)
        welcome = tk.Label(self.frame, bg= 'green', text= "Welcome to Blackjack", font=("Arial", 25), padx = 150, pady = 60)
        welcome.grid()
        minor_frame = tk.Frame(self.window, background='green', pady = 60)
        minor_frame.grid(row = 9, column = 0)
        #Handling the randomized image
        self.deck1 = Deck(1)
        
        
        coords = self.deck1.take_card().to_image()
        image_name = coords[1]
        coords = coords[0]
        self.image1 = Image.open(image_name)
        cropped_image = self.image1.crop((coords[0], coords[1], coords[2], coords[3]))
        card_img= ImageTk.PhotoImage(cropped_image)
        self.card_label = tk.Label(self.frame, image=card_img, background= 'green')
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
            image_name = coords[1]
            self.image1 = Image.open(image_name)
            coords = coords[0]
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

class Game_Window:
    def __init__(self,variable): 
        self.deck = Deck(6)
        self.player = Player(100)
        self.dealer = Player(100)
         
         
         
         
         
         
         #setting up the window
        self.variable = variable
        self.window = tk.Tk()
        self.window.configure(bg = 'green')
        self.window.columnconfigure(0, weight=1, minsize=42)
        self.dealer_hand =  []
        self.player_hand = []
        for i in range(6):
            self.window.columnconfigure(i+1, weight = 1, minsize = 80)
            self.dealer_hand.append(tk.Frame(width=73, height= 98, relief= tk.RAISED, borderwidth = 1, padx = 20, bg = 'green'))
            self.dealer_hand[i].grid(row = 0, column = i+1)
            self.player_hand.append(tk.Frame(width=73, height= 98, relief= tk.RAISED, borderwidth = 1, padx = 20, bg = 'green'))
            self.player_hand[i].grid(row = 3, column = i+1)

        self.window.rowconfigure(2, weight=1, minsize=200)

        #deck frame
        deck_frame = tk.Frame()
        deck_frame.grid(row = 2, column = 1)
        card_back = ImageTk.PhotoImage(Image.open("images/card_back.png"))
        deck_back = tk.Label(deck_frame, image = card_back)
        deck_back.grid()

        

        #setting up the grid
        top_frame = tk.Frame(self.window, bg = 'red', height = 150, padx = 20, pady = 40)
        top_frame.grid(row = 0, column = 0)
        dealer_label = tk.Label(top_frame, text = "Dealer's Hand")
        dealer_label.grid()
        dealer_cash = tk.Label(top_frame, text = "${:.2f}".format(-1 *self.player.get_cash() + 100))
        dealer_cash.grid()
        bottom_frame = tk.Frame(self.window, bg = 'red', height = 150, padx = 20, pady = 40)
        bottom_frame.grid(row = 3, column = 0)
        player_cash = tk.Label(bottom_frame, text = "${:.2f}".format(self.player.get_cash()))
        player_cash.grid()
        player_label = tk.Label(bottom_frame, text = "Player's Hand")
        player_label.grid()
        
        
        self.minor_frame = tk.Frame(self.window, background='green', pady = 60)
        self.minor_frame.grid(row = 4, column = 1)
        
        
        self.outside = Starter(self.variable, self.window,self)
        text_grid= tk.Frame(self.window, background= 'green')
        text_grid.grid(columnspan=2, row = 2, column = 2)

        def play():
            self.play_label.grid_forget()
            self.message = tk.Label(text_grid, text = "Make a Bet")
            self.message.grid()
            for x in range(len(self.outside.tinyframe)-2):
                self.outside.tinyframe[x].grid(row = 4, column = x+1 )
        play_frame = tk.Frame(self.window, background='green')
        play_frame.grid(row = 2, column = 0)
        self.play_label = ttk.Button(play_frame, text = "Play", command = play)
        self.play_label.grid()

        self.window.mainloop()


class Starter:

    def __init__(self,variable, window, parent): 
        self.window = window 
        self.variable = variable
        self.parent = parent
        self.player_picture = []
        self.dealer_picture = []
        
        self.tinyframe = []
        self.tinyframe.append(tk.Frame(window, bg = 'green', padx = 20, pady = 20))
        
        self.tinyframe.append(tk.Frame(window, bg = 'green', padx = 20, pady = 20))
    
        self.tinyframe.append(tk.Frame(window, bg = 'green', padx = 20, pady = 20))

        self.tinyframe.append(tk.Frame(window, bg = 'green', padx = 20, pady = 20))
       
        self.tinyframe.append(tk.Frame(window, bg = 'green', padx = 20, pady = 20))
     
        self.tinyframe.append( tk.Frame(window, bg = 'green', padx = 20, pady = 20))
        
        def reveal_hand():
            for x in self.parent.dealer.hand():
                x.show()
            
        def score_loop(entity):
            score = entity.score_hand()
            match score:
                case 100:
                    return "Blackjack!" 
                case -1:
                    return "Bust"
                case _:
                    return score
            
        def you_lose():
            pass
        def update_cards(player):
            if player == self.parent.player:
                self.picture = self.player_picture
            else:
                self.picture = self.dealer_picture
            for x in self.dealer_picture:
                x.grid_forget()
            else:
                self.picture = []
            for x in range(len(player.hand)):
                data = player.hand[x].to_image()
                image_name = data[1]
                data = data[0]
                print(image_name)
                image1 = Image.open(image_name)
                cropped_image = image1.crop((data[0], data[1], data[2], data[3]))
                card_img= ImageTk.PhotoImage(cropped_image)
                if player == self.parent.dealer:
                    self.picture.append( tk.Label(self.parent.dealer_hand[x], image = card_img, width = 73, height = 98))
                if player == self.parent.player:
                    self.picture.append(tk.Label(self.parent.player_hand[x], image = card_img, width = 73, height = 98))
                self.picture[x].image = card_img
                self.picture[x].grid()
                
            five_bet.grid_forget()
            ten_bet.grid_forget()
            fifteen_bet.grid_forget()
            twenty_bet.grid_forget()

        def hit_me(event):
            card = self.parent.deck.take_card()
            self.parent.player.hit(card)
            data = card.to_image()
            image_name = data[1]
            data = data[0]
            print(image_name)
            image1 = Image.open(image_name)
            cropped_image = image1.crop((data[0], data[1], data[2], data[3]))
            card_img= ImageTk.PhotoImage(cropped_image)
            self.picture.append(tk.Label(self.parent.player_hand[len(self.picture)% 6], image = card_img, width = 73, height = 98))
            self.picture[-1].image = card_img
            self.picture[-1].grid()
            self.parent.player.hit(card)
            result = score_loop(self.parent.player)
            match result:
                case -1:
                    pass




        def game_end(winner):
            if winner:
                pass 
        def game_loop():
            pass


        
        def start_play(self):
            
            self.tinyframe[4].grid(row = 4, column = 5)
            self.tinyframe[5].grid(row = 4, column = 6)
            self.parent.dealer.hit(self.parent.deck.take_card_hide())
            print(self.parent.dealer.hand)
            self.parent.dealer.hit(self.parent.deck.take_card())
            print(self.parent.dealer.hand)
            self.parent.player.hit(self.parent.deck.take_card())
            self.parent.player.hit(self.parent.deck.take_card())
            update_cards(self.parent.dealer)
            update_cards(self.parent.player)
            print(score_loop(self.parent.dealer))
            if score_loop(self.parent.dealer) == "Blackjack!":
                pass

        def add_bet_5():
            self.parent.player.make_wager(self.variable.get())
            for x in range(len(self.tinyframe)-2):
                self.tinyframe[x].grid_forget()
            
            self.parent.message.configure(text = "WAGER: ${:.2f}".format(self.variable.get()))
            start_play(self)
            
        def add_bet_10():
            self.parent.player.make_wager(self.variable.get()*2)
            for x in range(len(self.tinyframe)-2):
                self.tinyframe[x].grid_forget()
            
            self.parent.message.configure(text = "WAGER:  ${:.2f}".format(self.variable.get()*2))
            start_play(self)
                
           
        def add_bet_15():
            self.parent.player.make_wager(self.variable.get()*3)
            for x in range(len(self.tinyframe)-2):
                self.tinyframe[x].grid_forget()
                
            self.parent.message.configure(text = "WAGER: ${:.2f}".format(self.variable.get()*3))
            start_play(self)
        def add_bet_20():
            self.parent.player.make_wager(self.variable.get()*4)
            for x in range(len(self.tinyframe)-2):
                self.tinyframe[x].grid_forget()
            
            self.parent.message.configure(text = "WAGER: ${:.2f}".format(self.variable.get()*4))
            start_play(self)


        ##Betting buttons
        five_bet = ttk.Button(self.tinyframe[0], text="${:.2f}".format(self.variable.get()), command = add_bet_5)
        
        five_bet.grid(row = 0, column = 0)
        ten_bet = ttk.Button(self.tinyframe[1], text= "${:.2f}".format(self.variable.get()*2), command = add_bet_10)
        
        ten_bet.grid(row = 0, column = 0)
        fifteen_bet = ttk.Button(self.tinyframe[2], text="${:.2f}".format(self.variable.get()*3), command = add_bet_15)
        
        fifteen_bet.grid(row = 0, column = 0)
        twenty_bet = ttk.Button(self.tinyframe[3], text ="${:.2f}".format(self.variable.get()*4), command = add_bet_20)
        
        twenty_bet.grid(row = 0, column = 0)

        #Hit/Stay button 
        hit_button = ttk.Button(self.tinyframe[4], text ="Hit!".format(self.variable.get()*4))
        hit_button.bind('<Button-1>', hit_me)
        hit_button.grid(row = 0, column = 0)
        stay_button = ttk.Button(self.tinyframe[5], text ="Stay".format(self.variable.get()*4), )
        stay_button.grid()
        