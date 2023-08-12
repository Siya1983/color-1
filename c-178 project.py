from tkinter import*
import random
root=Tk()
root.title("random encapsulation colour")
root.geometry("600x600")
root.configure(background="light yellow")

label_name=Label(root,bg="white",font=70,)
label_name.place(relx=0.5,rely=0.5,anchor=CENTER)

class game():
    def __init__(self):
        self.score=0
    def update_game(self):
        self.text=["RED","ORANGE","BLUE","PURPLE","BLACK","GREEN"]
        self.random_no_for_text=random.randint(0,5)
        self.color=["red","orange","blue","purple","black","green"]
        self.random_for_color=random.randint(0,5)
        label_name["text"]=self.text[self.random_no_for_text]
        label_name["fg"]=self.color[self.random_for_color]
obj=game()
btn=Button(root,text="CHANGE COLOR",command=obj.update_game,bg="dark olive green",
fg="white",relief=FLAT,padx=10,pady=1,font=("Ariel",15))
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
    
root.mainloop()
