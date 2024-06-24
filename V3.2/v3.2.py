import random
import tkinter as tk
import tkinter.messagebox
import time
window = tk.Tk()           
window.title('口算助手')      
canvas = tk.Canvas(window, width=500, height=50)
canvas.pack()
canvas.create_text(250,25, text='请输入要生成几篇口算', fill='black', font=('Arial', 20))
c=tk.Text(window, height=3)     
c.pack()
def getTextInput1():
    try:
        global passage
        passage = eval(c.get("1.0","end"))
    except NameError as e1:
        tk.messagebox.showwarning(title='提示',
		message='请勿输入特种符号')
    except SyntaxError as e2:
        tk.messagebox.showwarning(title='提示',
		message='请勿输入特种符号')
canvas = tk.Canvas(window, width=500, height=50)
canvas.pack()
canvas.create_text(250,25, text='请输入输出文件标题', fill='black', font=('Arial', 20))
b=tk.Text(window, height=3)     
b.pack()
def getTextInput2():
    try:
        global tittel
        tittel_Rep = str(b.get("1.0","end"))
        tittel = tittel_Rep[:-1]
        tittel = str(tittel + ".txt")
        open(tittel,"x")
        t = open(tittel, 'w', encoding='utf-8')
        window.destroy()
        try:
            for x in range(passage):
                for y in range(25):
                    first = str(random.randint(0, 100))
                    second = str(random.randint(0, 100))
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
        except SyntaxError as e4:
            tk.messagebox.showwarning(title='提示',
                message='请勿输入特种符号')
        except NameError as e5:
            tk.messagebox.showwarning(title='提示',
		message='请勿输入特种符号')
    except FileExistsError as e3:
        tk.messagebox.showwarning(title='提示',
		message='文件名重复')
def do_all():
    getTextInput1()
    getTextInput2()
def make():
    btnRead=tk.Button(window, height=1, width=10, text="生成", command=do_all)       
    btnRead.pack()
make()
def btnReadExit():
    window.destroy()
btnRead2=tk.Button(window, height=1, width=10, text="退出", command=btnReadExit)
btnRead2.pack()
window.mainloop()
time.sleep(10)

