from tkinter import *#导入模块
from tkinter import messagebox#导入模块
class Application(Frame):#定义类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text="Hello", command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s' % name)


app = Application()
app.master.title('Hello World')
app.mainloop()