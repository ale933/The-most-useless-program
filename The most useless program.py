from tkinter import *

root = Tk()
root.geometry("550x500+572+293")
root.title("The Most Useless Program")

def useless():
	pass


def usefull():
	label.config(text="Oh! A usefull button!")


def choise(YoN):
	if YoN == "yes":
		ans.config(text="HOW?")

	if YoN == "no":
		ans.config(text="HOW?")
		

def review():
	global pop
	pop = Toplevel(root)
	pop.geometry("250x140+572+293")
	pop.title("Review")

	quest = Label(pop, text="Do You Like This Program?").pack()
	y = Button(pop, text="Yes", command=lambda: choise("yes"), pady=20, padx=20).pack(side=LEFT)
	n = Button(pop, text="No", command=lambda: choise("no"), pady=20, padx=20).pack(side=RIGHT)
	global ans
	ans = Label(pop, text="", font=('', 20, 'bold'))
	ans.pack()



uselessButton = Button(root, text="The Useless Button", command=useless).pack(fill=X)


usefullButton = Button(root, text="Maybe A Usefull Button", command=usefull).pack(pady=5, fill=X)
label = Label(root, text="", font=('Helvetica', 18, 'bold'))
label.pack()

''''''
menu = Menu(root)
root.config(menu=menu)

reviewM = Menu(menu, tearoff=0)

menu.add_cascade(label="Review", menu=reviewM)

reviewM.add_command(label="Review", command=review)
''''''

root.mainloop()
