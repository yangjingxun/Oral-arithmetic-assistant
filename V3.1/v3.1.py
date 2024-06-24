# -*- coding : utf-8-*-
import random
import tkinter as tk
import tkinter.messagebox
import time
window = tk.Tk()           
window.title('口算助手:请输入要生成几篇口算')      
window.geometry("400x240") 
textExample=tk.Text(window, height=10)     
textExample.pack()   
def getTextInput1():
    try:
        global passage
        passage = eval(textExample.get("1.0","end"))
        window.destroy()
    except NameError as e1:
        tk.messagebox.showwarning(title='提示',
		message='请勿输入特种符号')
    except SyntaxError as e2:
        tk.messagebox.showwarning(title='提示',
		message='请勿输入特种符号')
btnRead=tk.Button(window, height=1, width=10, text="下一个", command=getTextInput1)   
btnRead.pack()     
window.mainloop()

window = tk.Tk()           
window.title('口算助手:请输入输出文件标题')      
window.geometry("400x240") 
textExample=tk.Text(window, height=10)     
textExample.pack()   
def getTextInput2():
    try:
        global tittel
        global t
        tittel_Rep = str(textExample.get("1.0","end"))
        tittel = tittel_Rep[:-1]
        tittel = str(tittel + ".txt")
        open(tittel,"x")
        t = open(tittel, 'w', encoding='utf-8')
        window.destroy()
    except FileExistsError as e3:
        tk.messagebox.showwarning(title='提示',
		message='文件名重复') 
btnRead=tk.Button(window, height=1, width=10, text="下一个", command=getTextInput2)   
btnRead.pack()     
window.mainloop()

window = tk.Tk()           
window.title('口算助手:请输入数值大小')      
window.geometry("400x240") 
textExample=tk.Text(window, height=10)     
textExample.pack()   
def getTextInput3():
    try:
        number = eval(textExample.get("1.0","end"))
        for x in range(passage):
            for y in range(25):
                first = str(random.randint(0, number))
                second = str(random.randint(0, number))
                out1 = str(first + "+" + second)
                out2 = str(first + "-" + second)
                out3 = str(first + "*" + second)
                out4 = str(first + "/" + second)
                t.write(out1 + "=     ")
                t.write(out2 + "=     ")
                t.write(out3 + "=     ")
                t.write(out4 + "=     \n")
            t.write("完成一篇\n")
        t.write("全部完成\n   ")
        tk.messagebox.showinfo(title='全部完成',
		message='全部完成')
        t.close()
        window.destroy()
    except NameError as e4:
        tk.messagebox.showwarning(title='提示',
		message='请勿输入特种符号')
    except SyntaxError as e5:
        tk.messagebox.showwarning(title='提示',
		message='请勿输入特种符号')
btnRead=tk.Button(window, height=1, width=10, text="下一个", command=getTextInput3)   
btnRead.pack()     
window.mainloop()
