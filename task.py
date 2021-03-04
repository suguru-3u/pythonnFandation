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

        # 表示エリア
        self.list_area = ListArea(self.master)
        self.list_area.pack()

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

class ListArea(tk.Frame):
    """
    TODOリストの表示エリア
    ユーザーが入力したTODOが表示される
    """

    def __init__(self,master):
        super(ListArea,self).__init__(master)

        # リストアの作成
        self.listbox = tk.Listbox(self,height=5)
        self.listbox.pack()

        # 削除のボタンの作成
        self.del_btn = tk.Button(self,text='削除',command=self._click_del_btn)
        self.del_btn.pack()
    
    def _click_del_btn(self):
        """
        選択中のTODOを削除する
        """
        print('delete selection')
        sel = self.listbox.curselection()
        for i in sel[::-1]:
            self.listbox.delete(i)


def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()

