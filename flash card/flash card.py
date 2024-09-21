from tkinter import* 
import pandas as pd 
import random
try:

    data = pd.read_csv("C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/flash card/ words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/flash card/french_words.csv")
    to_learn=original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient='records')
new_card={}


def next_card():
    global new_card , flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French" , fill='black')
    canvas.itemconfig(word, text=new_card['French'] , fill='black')
    canvas.itemconfig(card_image, image=card_front_image)
    flip_timer=window.after(3000, flip_card)  # Flip the card after 3 seconds

def flip_card():
    canvas.itemconfig(title, text='English' , fill="white")
    canvas.itemconfig(word, text=new_card["English"] , fill='white')
    canvas.itemconfig(card_image, image=card_back_image)
 
 
def is_known():
    to_learn.remove(new_card)
    data=pd.DataFrame(to_learn)  
    data.to_csv("C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/flash card/ words_to_learn.csv")

    next_card()
  



window = Tk()
window.title("flash card")
window.minsize(800,800)
window.config(padx=50 , pady=50 , bg='#B1DDC6') 

flip_timer=window.after(3000 , func=flip_card)

canvas = Canvas(width=800 ,height= 526 , highlightthickness=0)
card_back_image= PhotoImage(file='C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/flash card/card_back.png')



card_front_image = PhotoImage(file='C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/flash card/pic.png')
card_back_image = PhotoImage(file='C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/flash card/card_back.png')
card_image = canvas.create_image(410, 270, image=card_front_image)

title = canvas.create_text(400, 150, text="Title", font=("Arial", 24, 'bold'))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 35, 'bold'))
canvas.config(bg='#B1DDC6')
canvas.grid(column=1, row=0, columnspan=2)


yes_image =PhotoImage(file='C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/flash card/right.png')
yes = Button(image=yes_image , width=100 , height=100 , highlightthickness=0 ,command=is_known)
yes.grid(column=2 , row=1)
no_image =PhotoImage(file='C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/flash card/wrong.png')
no = Button(image=no_image , width=100 , height=100 , highlightthickness=0 , command=next_card)
no.grid(column=1  , row=1)


 
next_card()










window.mainloop()
