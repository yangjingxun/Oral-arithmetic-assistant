
import tkinter as tk

# 创建窗口
root = tk.Tk()

# 创建文本框组件
text_box = tk.Text(root, width=30, height=10)

# 添加文本框组件到窗口中
text_box.pack()

# 输出内容到文本框中
text_box.insert('1.0', 'Hello, World!\n')

# 进入主循环
root.mainloop()

