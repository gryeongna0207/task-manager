# app.py 예시 (간단한 틀만 보여드립니다)
import tkinter as tk

root = tk.Tk()
root.title("업무 일정 관리")
root.geometry("400x300")

label = tk.Label(root, text="여기에 달력과 일정 목록이 표시됩니다.")
label.pack(pady=20)

root.mainloop()
