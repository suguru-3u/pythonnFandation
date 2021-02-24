# file = "test.txt"
# fileobj = open(file)
# text = fileobj.read()
# fileobj.close()
# print(text)

# with open(file) as fileobj:
#     text = fileobj.read()
#     newtext = text.split(" ")
#     print(newtext)

# import sys
# arglist = sys.argv
# print(arglist)
# if len(sys.argv)<2:
#     print("読み込みができませんでした")
#     sys.exit()

# file = sys.argv[1]
# with open(file) as fileobj:
#     data = fileobj.read()
#     print(data)

# import tkinter as tk
# import tkinter.filedialog as fd

# root = tk.Tk()
# root.withdraw()

# file = fd.askopenfilename(
#     title = "ファイルを選んでください",
#     filetype = [("TEXT",".txt"),("TEXT",".py"),("HTML",".html")]
# )

# if file:
#     with open(file) as fileobj:
#         text = fileobj.read()
#         print(text)

import sys
import tkinter

root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

Static1 = tkinter.Label(text=u'test')
Static1.pack()

root.mainloop()