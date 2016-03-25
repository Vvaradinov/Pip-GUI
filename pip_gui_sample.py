import pip
import tkinter

DEFAULT_FONT = ("Helevetica Black",20)
class Pip_gui():
    def __init__(self):
        self._root_window = tkinter.Tk()

        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight =1)
        self._root_window.columnconfigure(1, weight = 1)

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 100, height = 100,
            background = "white")
        self._canvas.grid(
            row = 1, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self.text_install = tkinter.StringVar()
        self.text_install.set("Install")

        self.text_upgrade = tkinter.StringVar()
        self.text_upgrade.set("Upgrade")

        self._search_box = tkinter.Entry(master= self._root_window,font=DEFAULT_FONT)
        self._search_box.grid(row = 0,column= 0,sticky = tkinter.W)

        self._search_button = tkinter.Button(master = self._root_window,textvariable= self.text_install,command= lambda: self.install(),font=DEFAULT_FONT)
        self._search_button.grid(row = 0,column=0,sticky = tkinter.E,columnspan= 1)
        self._search_button.config(height = 0,width = 6)

        self._search_button = tkinter.Button(master = self._root_window,textvariable= self.text_upgrade,command= lambda: self.upgrade(),font=DEFAULT_FONT)
        self._search_button.grid(row = 0,column=1,sticky = tkinter.E,columnspan= 1)
        self._search_button.config(height = 0,width = 6)

        self._user_inputs = []

    def run(self):
        self._root_window.mainloop()

    def install(self):
        """
        If button clicked = Install
        """
        user_input = self._search_box.get()
        self._user_inputs.append(user_input)
        self._search_box.delete(0,"end")
        pip.main(["install",self._user_inputs[0]])
        self._user_inputs.remove(self._user_inputs[0])

    def upgrade(self):
        """
        If button clicked = Upgrade
        """
        user_input = self._search_box.get()
        self._user_inputs.append(user_input)
        self._search_box.delete(0,"end")
        pip.main(["install","--upgrade",self._user_inputs[0]])
        self._user_inputs.remove(self._user_inputs[0])
if __name__ == "__main__":
    Pip_gui().run()