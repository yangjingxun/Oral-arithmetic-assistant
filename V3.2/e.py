import tkinter

root = tkinter.Tk()

tupleVar = ('python', 'java', 'C', 'C++', 'C#')
var = tkinter.StringVar()
# 这里必须要带*号，要不然解释器会认为是一个数据，只会显示一行的
optionMenu = tkinter.OptionMenu(root, var, *tupleVar)
optionMenu.pack()

root.mainloop()
