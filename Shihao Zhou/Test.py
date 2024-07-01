import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Input Received", f"You entered: {user_input}")
    else:
        messagebox.showwarning("No Input", "Please enter something in the text box.")

# 创建主窗口
root = tk.Tk()
root.title("Simple GUI")

# 创建标签
label = tk.Label(root, text="Enter something:")
label.pack(pady=10)

# 创建文本输入框
entry = tk.Entry(root)
entry.pack(pady=5)

# 创建按钮
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=20)

# 运行主循环
root.mainloop()
