from tkinter import *
import os


#Creating an instance of Tk initializes this interpreter and creates the root window. I dont have to call tkinter it later
root = Tk()
# All the images that are in the game
photo = PhotoImage(file="giphy.gif", )
goblin_image = PhotoImage(file="gobba.png")
pikachu_image = PhotoImage(file= "thumb-89303.gif")
nice_picture = PhotoImage(file= "cyrodiil-pixel-art.png")
first_room_picture = PhotoImage(file= "ucho_first_room_pixelart.png")
hurt_goblin_picture = PhotoImage(file="hurt_gobba.png")


# The main framework (all the windows)
Stats = Label(root, width=15, height=50, bg="red")
Stats.pack(side=LEFT)
NPC_images = Label(root, image=goblin_image , width=200, height=200, bg="green" )
NPC_images.pack(side=RIGHT, anchor=NW)
label = Label(root, image=photo, width=900, height=450, bg="black")
label.pack()


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, expand = "yes")
#root.configure(width=1200, height=600,)
root.configure( bg="black")



#stats of the small goblin
Hp =10
magic =0
inventory = ()



# window for the stats
# here in the "text" parameter we need to use "+" instead of "," because otherwise tkinter will add curly brackets to
# the displayed text and convert into tuple
stat =  Label(Stats,font=("Courier", 13), width=10, height=30, bg="black", fg="white",
              text= " HP =" + str(Hp) + "\n magic = "+ str(magic) +"\n" "\n" "Inventory:\n" " nic " )
stat.pack()




# this function will save the progress bu creating a a simple txt file and later reading it.
def save_csv():
    f = open("ucho_the_origins_save.txt", "w+")
    f.write("The player has made some progress")
    os.mkdir('pizza_pictures')
    f.close()

# save_csv()

# the functions were written before i had learned about code naming rules and code ethics so it isn`t pretty and
# it is messy. Im working to clean  it



def first_orc():
    introduction["text"] =  "You leave the room. Your eyes are quickly getting used to the dark. \n "\
                            "You see that an orc sits nearby. As soon as he notices you, \n "\
                            "he approaches you, barking his fangs. \n "\
                            "-HEY, little git - he says in a bored voice - \n "\
                            "-What is your name?"
    introduction.pack()
    def grimgor_name():
        introduction["text"] =  "- Stupid git, this name is already taken !! - \n "\
                                "The orc frowns and you get a blow to the face before you can react. \n "\
                                " You fall backwards with a black eye  When you get up from the floor,  \n "\
                                "the orc loses interest and goes your way ... \n "\
                                "You are alone in the middle of the \n" \
                                "corridor"

        introduction.pack()

        def auch():
            introduction["text"] = "You lie, the shadows fly in front of your eyes, \n "\
                                    "you try to catch those funny shapes but they run away all the time.\n " \
                                   " it takes you A few minutes to go back to yourself. "
            introduction.pack()
        NPC_images["image"] = hurt_goblin_picture
        label['image'] = hurt_goblin_picture
        button0['text'] = 'get up from the floor'
        button0["fg"] = "blue"
        button0["command"] = tower_first_look
        button2['text'] = "look at the stars"
        button2["command"] = auch
        button2["fg"] = "green"
        button1["fg"] = "blue"
        button1["text"] = "go back to the room"
        button1["command"] = first_room_looking
        # need be careful by declaring global variable as it will affect all places where Hp is referenced
        global Hp
        Hp -= 1
        # next line will update the label stats as without it the Hp stays at 10
        stat["text"] = " HP =" + str(Hp) + "\n magic = "+ str(magic) +"\n" "\n" "Inventory:\n" " nic "

    button0["text"] = "yyyy, glonk?"
    button0["command"] = choosing_name
    button2['text'] = "skub"
    button0["fg"] = "green"
    button2["fg"] = "green"
    button2["command"] = choosing_name
    button1["fg"] = "red"
    button1["text"] = "GRIMGOR IRONHIDE !!"
    button1["command"] = grimgor_name


def change_text():
    introduction["text"] =  "You see how the light slowly breaks through the thin layer of earth \n" \
                            " under which you lie, you shovel the sand aside. \n " \
                            "On the one side, you see a huge hole through which \n " \
                            "the sun shines. You see the damaged tiles \n" \
                            "covering the floor and walls. One broken door leads to the room."
    introduction.pack()
    label['image'] = first_room_picture
    label.pack()
    button0['text'] = 'go to the hole in the door'
    button0['command'] = first_orc
    button2['text'] = "go to the hole in the wall"
    button2["fg"] = "green"
    button2["command"] = big_hole
    button1["text"] = "look around the room"
    button1["command"] = first_room_looking

def machinery_1():
        introduction["text"] = " You wander the huge building for a few nice hours, \n " \
                               "you pass by goblins and orcs, all laden with parts and equipment.\n " \
                               " Hundreds of rooms are full of engineers, huge smithies and workshops\n " \
                               " smoke and blaze. Finally you manage to reach the mighty square.\n " \
                               " Sunlight floods your eyes. You are at the very top !! \n " \
                               "Hundreds of greenskins are working on a powerful device. "

        introduction.pack()
        def machinery_engineer():
            introduction["text"] = " You approach one of the engineers involved in drawing up plans"
            introduction.pack()
            def machinery_description():
                introduction["text"] = " -This will be the largest rockfarthower we have ever made \n" \
                                       "-We have a great plan foretold by the shaman! everyone knows \n " \
                                       "that the gobbos are from the MOON. but we will go back there.\n" \
                                       " If you want, you can help. Want? "
                introduction.pack()
            button0['text'] = '"What are you working on?"'
            button0["command"] = machinery_description
            def join_engineers():
                introduction["text"] = " Are you sure you want to spend the next few months helping the engineers?"
                introduction.pack()
                button0['text'] = 'yes'
                button0["command"] = save_csv
                button2['text'] = "no"
                button2["command"] = machinery_engineer
                button1["fg"] = "blue"
                button1["text"] = "also no but blue"
                button1["command"] = machinery_engineer
            button2['text'] = "I want to join"
            button2["command"] = join_engineers
            button1["text"] = "Return to the middle of the square"
            button1["command"] = machinery_look
        def machinery_look():
            introduction["text"] = "The great machine soars into the sky. A set of ropes and chains\n" \
                                   " fastens the construction.Swarm of goblins walks and climbs\n" \
                                   " onto the planks. A group of engineers oversees\n" \
                                   " and draws plans for new parts. "
            introduction.pack()
            button0['text'] = ' look around the big place'
            button0["command"] = machinery_look

            button2['text'] = "approach the engineer"
            button2["command"] = machinery_engineer
            button1["fg"] = "blue"
            button1["text"] = "go back to the tower"
            button1["command"] = tower_first_look
        button0['text'] = 'look around the big place'
        button0["command"] = machinery_look

        button2['text'] = "approach the engineer"
        button2["command"] = machinery_engineer
        button1["fg"] = "blue"
        button1["text"] = "go back to the tower"
        button1["command"] =tower_first_look


def choosing_name():
        introduction["text"] = "-Okay. It's a cool little git name- Without looking at you\n" \
                               " he went his way. The tower is made of pieces\n" \
                               " of bricks, stones, wood. The building seems huge, \n" \
                               " consists of randomly arranged rooms and corridors. \n" \
                               "  Above you can hear the noise of machines.\n" \
                               "  From below you can smell the pleasant smell of mushrooms. "
        introduction.pack()
        button0['text'] = 'go  upstairs'
        button0["fg"] = "blue"
        button0["command"] = machinery_1
        button2['text'] = "go downstairs"
        button2["command"] = tower_first_look
        button2["fg"] = "blue"
        button1["fg"] = "blue"
        button1["text"] = "go back to the room"
        button1["command"] = first_room_looking







def first_room_looking():
    introduction["text"] = " You are looking around. You find a piece of moss. \n" \
                           "There is some water in the puddle at the end. It is \n" \
                           "delicious and tastes of sand. There is no puddle anymore.\n" \
                           " A few mushrooms stick out of the mound from which you \n" \
                           "dug up. They have a tasty purple color. You eat one of \n" \
                           "them and it is quite nice. You eat the rest of them.\n" \
                           " Nothing more  to eat. "
    introduction.pack()
    label["image"] = first_room_picture
    label.pack()
    button0['text'] = 'walk to the door'
    button0["fg"] = "blue"
    button0["command"] = first_orc
    button2['text'] = "go to the hole in the wall"
    button2["fg"] = "blue"
    button2["command"] = big_hole
    button1["fg"] = "green"
    button1["text"] = "look around"
    button1["command"] = first_room_looking


def first_room():
    introduction["text"] = " Jesteś w małym pomieszczeniu, w końcie jest masa piachu z\n " \
                            "której wylazłeś. Na ścianach jest trochę mchu i grzybów.\n " \
                            "Kafelki wyglądają na zniszczone. W konatach są pajęczyny i\n " \
                           "kawałki drewna. "
    introduction.pack()
    label["image"] = first_room_picture
    label.pack()
    button0['text'] = 'Podchodzę do   drzwi'
    button0["fg"] = "blue"
    button0["command"] = first_orc
    button2['text'] = "Podchodzę do  dziury w ścianie"
    button2["fg"] = "blue"
    button2["command"] = big_hole
    button1["fg"] = "green"
    button1["text"] = "Rozglądam się po pomieszczeniu"
    button1["command"] = first_room_looking

def big_hole():
    introduction["text"] = "Z wybitej dziury rozlega się piękny widok, spoglądasz ze zrójnowanej\n" \
                           "wieży, potężna konstrukcja wzmocniona jest prowizorycznymi rusztowaniami\n" \
                           "poniżej widać miasto zbudowane z wszelkiej maści gruzów i kamieni,\n" \
                           "w mieście panuje ruch i gwar ale trudno dostrzec pojedyńcze sylwetki.\n" \
                           "Dalej widać pola uprawne, las oraz góry, lecz nawet one nie są tak wysokie\n" \
                           "jak wieża z której spoglądasz. "
    introduction.pack()
    label["image"] = nice_picture
    button0['text'] = 'spoglądam w dół'
    button0["fg"] = "green"
    def sightseeing_from_the_towet():
        introduction["text"] = " Widzisz piękny widok. Wielka wieża, z której wyglądasz góruje na całym\n" \
                               " krajobrazem. W dole widać miasto z mrowiem innych postaci. Chmury leniwie\n" \
                               "pełzną po niebie. W oddali las ciągnie się aż po horyzont."
        introduction.pack()
    button0["command"] = sightseeing_from_the_towet
    button2['text'] = "patrzę prosto na słońcę!!!"
    button2["fg"] = "red"

    def yyy():
        introduction['text'] = " YYYYHHUUEE!?!!?"
        introduction.pack()
        button0['text'] = 'FFFFFLLLLLLL'
        button2['text'] = "yes"
        button1["text"] = "42??"
        label['image'] = pikachu_image
        label.pack()
        def blinded_by_the_sun():
            introduction["text"] = " Blask zalewa ci oczy. Mrugasz ale niewiele to pomaga. Musisz poczekać parę minut\n" \
                                   "aż wróci ci wzrok. Powoli znowu widzisz swoje otoczenie."
            introduction.pack()
            button0["command"] = big_hole
            button2["command"] = big_hole
            button1["command"] = big_hole
        button0["command"] = blinded_by_the_sun
        button2["command"] = blinded_by_the_sun
        button1["command"] = blinded_by_the_sun
    button2["command"] = yyy
    button1["text"] = "wracam z powrotem do pokoju"
    button1["fg"] = "blue"
    button1["command"] = first_room

def going_downstairs():
    introduction["text"] = "Jesteś w rozległych podziemiach. Wszędzie widać świecące grzyby i pracujące gobliny. \n" \
                           "Słychać z dołu brzmienie bębnów i pyszny zapach grzybów. Wchodzisz do jednego z pokoi." \
                           "Widać sporo grzybów, jakieś zwierzaki i szamanów z śmisznymi czapkami. "
    button0['text'] = 'podejdź do szamana'
    def first_shaman():
        introduction["text"] = "- Hej mały gobba! :D Co tu porabiasz? "

        def first_shaman_text():
            introduction["text"] = "Ogólnie przygotowójemy wszystko co jest potrzebne. Hodujemy grzyby, odprawiamy \n" \
                                   "rytułały gdzie pobieramy wizje od BOGÓW czy robimy wszystko zgodnie z planem i \n" \
                                   "doznajemy oświecenia. Najbardziej oddani zyskują magiczne moce od BOGÓW!!\n" \
                                   "Ogólnie jest spoko. Ogarniamy tą bude. "
        button0['text'] = 'Czym sie zajmujecie?'
        button0["command"] = first_shaman_text
        button0["fg"] = "green"
        button2['text'] = "Wracam do wieży"
        button2["command"] = tower_first_look
        button2["fg"] = "blue"
        button1["text"] = "Chcę dołączyć"
        button1["command"] = save_csv
        button1["fg"] = "blue"
    button0["command"] = first_shaman
    button0["fg"] = "green"
    def first_shaman_look():
        introduction["text"] = "Całe pomieszczenie zalane jest blaskiem grzybów. Wszędzie biegają małe stworki \n" \
                               "nazywające się squigi. Widać parę zielonoskórych odprawiających rytułały na \n" \
                               "grzybach i dbających o utrzymanie wszystkiego. Na ścianach lśnią magiczne symbole."
    button2['text'] = "Rozejrzyj się"
    button2["command"] = first_shaman_look
    button2["fg"] = "green"
    button1["text"] = "wróć na górę"
    button1["command"] = tower_first_look
    button1["fg"] = "blue"




def tower_first_look():
    introduction["text"] = "Jesteś w wierzy. Zbudowana jest z kawałków cegieł, kamieni, drewna\n" \
                           "Budowla wydaje się olbrzymia, składa się z losowo rozmieszczonych\n" \
                           "pomieszczeń i korytarzy. Wszędzie słychać kroki i odgłosy różnych\n" \
                           "zielonoskórych. Z góry słychać chałas maszyn. Z dołu czujesz \n" \
                           "przyjemny zapach grzybów. Możesz też wrócić do pokoju"
    introduction.pack()
    button0['text'] = 'Idę do góry'
    button0["command"] = machinery_1
    button0["fg"] = "blue"
    button2['text'] = "Idę na dół"
    button2["command"] = going_downstairs
    button2["fg"] = "blue"
    button1["text"] = "wracam do pokoju"
    button1["command"] = first_room_looking
    button1["fg"] = "blue"






#
# stat =  Label(Stats,font=("Courier", 13), width=8, height=1, bg="black", fg="white",
#               text= " HP  " )
# stat.pack(side=LEFT, anchor=NW)
# stat =  Label(Stats,font=("Courier", 13), width=8, height=2, bg="black", fg="white",
#               text= 10 )
# stat.pack()
#
# stat =  Label(Stats,font=("Courier", 13), width=8, height=1, bg="black", fg="white",
#               text= " mana  " )
# stat.pack(side=LEFT, anchor=NW)
# stat =  Label(Stats,font=("Courier", 13), width=8, height=2, bg="black", fg="white",
#               text= 0)
# stat.pack()
#
#
# stat =  Label(Stats,font=("Courier", 13), width=10, height=2, bg="black", fg="white",
#               text= " Ekwipunek:\n" )
# stat.pack(side=LEFT, anchor=NW)








# the main text box that is changing
introduction = Label(root,font=("Courier", 15), width=80, height=10, bg="black", fg="white",
                     text="Witaj, to krótka historia małego goblina. Chcesz zagrać?\n"
                           "Kolor przycisków ma znaczenie. Niebieski to przejście do innej lokacji\n"
                          "zielony to działanie, czerwony oznacza opcje która wydaje \n"
                          "się głupia goblinowi, a to coś już znaczy. ")
introduction.pack()


# exit and the buttons
button2 = Button(bottomFrame, width=35, height=1,
                    text="Nie che mi się", fg="red", command = root.destroy)
button2.pack(side=BOTTOM)

button0 = Button(bottomFrame, width=35, height=1,
                 text="Zobacz co marek przygotował", fg="green",
                 command= change_text, )
button0.pack(side=BOTTOM)


button1 = Button(bottomFrame, width=35, height=1,
                 text="Jasne że zagram", fg="blue",
                 command= change_text, )
button1.pack(side=BOTTOM, )



'''
picture template
photo = PhotoImage(file="thumb-89303.gif")
label = Label(root, image=photo)
label.pack()



command=lambda: prev(panel)
    Goblin_image = PhotoImage(file="thumb-89303.gif")
    label["image"] = Goblin_image
    label.pack()
 
 function template
def nameOfFunction():
    introduction["text"]
    button0['text'] = 'Idę do góry'
    button0["command"] = Machinery_1
    button0["fg"] = "blue"
    button2['text'] = "Idę na dół"
    button2["command"] = Tower_first_look
    button2["fg"] = "blue"
    button1["text"] = "Wychodzę z wieży"
    button1["command"] = Tower_first_look
    button1["fg"] = "blue"               
    
'''

root.mainloop()
