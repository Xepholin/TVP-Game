from game import game_screen
from tkinter import *
from system import Player

def switch_game(login, errorTextFrame, username, password):
    '''
	Make the transition between the login screen and the game screen

			Parameters:
                login (Tk) : A Tk object
                errorTextFrame (Frame) : A Frame object
				username (str) : A String
                password (str) : A String
	'''

    if (username and password):
        user_pwd = "{} {} 0\n".format(username, password)
        
        with open("logs", 'a+') as file:
            file.seek(0)
            lines = file.readlines()
            boolean = 1
            player = Player(username, password, 0)

            for line in lines:
                temp = line.split()
                
                if (username == temp[0] and password == temp[1]):
                    player.set_max_score(int(temp[2]))
                    boolean = 0
                    break
                else:
                    continue
        
            if (boolean):
                file.write(user_pwd)

        login.destroy()

        game = Tk()
        game_screen(game, player)

        game.mainloop()
    else:
        errorTextFrame.itemconfig("text", text="Username or Password incorrect !")

def login_screen(login):
    '''
	Display login screen

			Parameters:
                login (Tk) : A Tk object
	'''

    login.geometry("960x540")
    login.minsize(960, 540)

    main = Frame(login)
    title = Frame(login, bd=3, bg="black")
    info = Frame(main, bd=1)
    log = Frame(main)

    titleLabel = Label(title, text="TVP Game", font=("Arial", 35))
    connectLabel = Label(info, text="Login", font=("Arial 25 underline"))

    titleLabel.pack()
    connectLabel.pack()

    usernameLabel = Label(log, text="Username :", font=("Arial", 15), anchor='w')
    username = StringVar()
    usernameEntry = Entry(log, textvariable=username, font=("Arial", 15))

    passwordLabel = Label(log, text="Password :", font=("Arial", 15), anchor='w')
    password = StringVar()
    passwordEntry = Entry(log, textvariable=password, show='*', font=("Arial", 15))

    errorTextCanvas = Canvas(log)
    errorTextCanvas.create_text(200, 8, text="", font=("Arial", 10), fill="red", tag="text")

    loginButton = Button(log, text="Login", font=("Arial", 11), width=25, height=1, command= lambda: switch_game(login, errorTextCanvas, username.get(), password.get()))

    usernameLabel.pack(fill=BOTH)
    usernameEntry.pack(fill=BOTH)
    passwordLabel.pack(fill=BOTH)
    passwordEntry.pack(fill=BOTH)
    loginButton.pack(pady=15)
    errorTextCanvas.pack()

    title.pack(pady=50)
    main.pack(pady=10)
    info.pack(pady=15)
    log.pack()