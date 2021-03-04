import sys
import tkinter as tk


class App:
    def __init__(self):
        #初期化処理
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

    def mainloop(self):
        self.master.mainloop()

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()


# root = tk.Tk()
# root.title(u"タスク管理ファイル")
# root.geometry("400x300")

# #画面上部
# Static1 = tk.Label(text=u'本日のタスクを記入してください')
# Static1.pack()

# #入力欄
# EditBox = tk.Entry(width=50)
# EditBox.pack()

# #　入力された文字を取得
# value = EditBox.get()
# print(value)

# root.mainloop()