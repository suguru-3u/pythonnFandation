import sys
import tkinter as tk


root = tk.Tk()
root.title(u"タスク管理ファイル")
root.geometry("400x300")

#画面上部
Static1 = tk.Label(text=u'本日のタスクを記入してください')
Static1.pack()

#入力欄
EditBox = tk.Entry(width=50)
EditBox.pack()

#　入力された文字を取得
value = EditBox.get()

root.mainloop()