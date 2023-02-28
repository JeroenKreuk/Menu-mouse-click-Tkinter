from tkinter import *
root = Tk()
menu = Menu(root)

root.title("Left mouse click options")


for buttons in range(5):
    Label(root, bg="Black", fg="orange", font="none 10 bold", text="Button "+ str(buttons)).grid(row=1+buttons, column=0, sticky=W, pady = 1, padx = 1)
    Label(root, bg="Black", fg="orange", font="none 10 bold", text="Button "+ str(buttons)).grid(row=1+buttons, column=1, sticky=W, pady = 1, padx = 1)
    Label(root, bg="Black", fg="orange", font="none 10 bold", text="Button "+ str(buttons)).grid(row=1+buttons, column=2, sticky=W, pady = 1, padx = 1)
    Label(root, bg="Black", fg="orange", font="none 10 bold", text="Button "+ str(buttons)).grid(row=1+buttons, column=3, sticky=W, pady = 1, padx = 1)
    Label(root, bg="Black", fg="orange", font="none 10 bold", text="Button "+ str(buttons)).grid(row=1+buttons, column=4, sticky=W, pady = 1, padx = 1)

class mouse:
    def __init__(self, event):
        self.event = event

        menu.delete(0, "end") #menu.add_commend will be remembered therefor all previous menu.add_command will be removerd

        #add menu
        menu.add_command(label="Print xy location mouse", command=lambda: self.mouse_location())
        menu.add_command(label="Print text button", command=lambda: self.widget_text())
        menu.add_command(label="Print row button", command=lambda: self.row())
        menu.add_command(label="Print column button", command=lambda: self.column())

        #post menu on the location of the mouse
        menu.post(self.event.x_root, self.event.y_root)

        #print some test when the left mouse is clicked
        r = self.event.widget.grid_info()['row']
        c = self.event.widget.grid_info()['column']
        print("Each click this will be triggered: " + "row = " +  str(r) + " Column = " + str(c))


    def mouse_location(self):
        x = self.event.x_root
        y = self.event.y_root
        print("X = " + str(x) + "   Y = " + str(y))

    def widget_text(self):
        print(self.event.widget.cget('text'))

    def row(self):
        r = self.event.widget.grid_info()['row']
        print("Row button: " + str(r))

    def column(self):
        c = self.event.widget.grid_info()['column']
        print("Column button: " + str(c))


root.bind('<3>', mouse) # this will make sure that when the left mouse is clicked some action will happen

root.mainloop()