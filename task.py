import sys
import tkinter as tk
import tkinter.messagebox as tkMessage

root = tk.Tk()
root.title(u"タスク管理ファイル")
root.geometry("400x400")

taskList = []

#　入力された文字を取得
def Update_task(event):
    getvalue = EditBox.get()
    taskNumber = len(taskList)
    print(taskNumber)
    taskList = getvalue   
    EditBox.delete(0, tk.END)
    tkMessage.showinfo('info',"Taskが登録されました")
    print(taskList)

#画面上部
Static1 = tk.Label(text=u'本日のタスクを記入してください')
Static1.pack()

#入力欄
EditBox = tk.Entry(width=50)
EditBox.pack()

#ボタン
Button = tk.Button(text=u'登録する')
Button.bind("<Button-1>",Update_task)
Button.pack()

#Task内容
label2 = tk.Label(text=taskList)
label2.pack()

root.mainloop()