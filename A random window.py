from tkinter import *
root = Tk()

root.geometry("500x500")
root.title("A random window")

btn = Button(root, text = "Press",background = "purple",command = root.destroy, bd = 7)
btn.pack(side = "top")

btn = Button(root, text = "Press",background = "blue",command = root.destroy, bd = 7)
btn.pack(side = "bottom")

btn = Button(root, text = "Press",background = "pink",command = root.destroy, bd = 7)
btn.pack(side = "left")

btn = Button(root, text = "Press",background = "red",command = root.destroy, bd = 7)
btn.pack(side = "right")


root.mainloop()