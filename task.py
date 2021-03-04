import sys
import tkinter as tk


class App:
    def __init__(self):
        #初期化処理
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

        # 入力エリア
        self.input_area = InputArea(self.master)
        self.input_area.pack()

    def mainloop(self):
        self.master.mainloop()

class InputArea(tk.Frame):
    """
    TODOの入力エリア
    ユーザーの入力を処理する
    ユーザーが入力したTODOテキストを追加ボタンでリストに追加するのが役割
    """

    def __init__(self,master):
        super(InputArea,self).__init__(master)

        # ラベル
        self.label = tk.Label(self,text="TODO")
        self.label.pack(side='left')

        # 入力行の作成
        self.entry = tk.Entry(self)
        self.entry.pack(side='left')

        # 追加ボタン
        self.add_btn = tk.Button(self,text='追加',command=self._click_add_btn)
        self.add_btn.pack(side='left')

    def _click_add_btn(self):
        print('add',self.entry.get())


def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()

