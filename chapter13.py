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

# import sys
# import tkinter
# import tkinter.filedialog as fd

# root = tkinter.Tk()
# root.withdraw()
# root.title(u"Software Title")
# root.geometry("400x300")

# Static1 = tkinter.Label(text=u'test')
# Static1.pack()

# file = fd.askopenfilename(
#     title = "ファイルを洗濯してください",
#     filetypes=[("TEXT",".txt"),("TEXT",".py"),("HTML",".html")]
# )

# if file:
#     with open(file) as fileobj:
#         text = fileobj.read()
#         print(text)

# root.mainloop()

# file = "test.txt"
# target = "f"

# with open(file) as fileobj:
#     while True:
        # text = fileobj.read(3)
        # if text:
        #     print(text)
        # else:
        #     break
        # try:
        #     line = next(fileobj)
        #     if line.find(target) >=0:
        #         print("見つかりました")
        #         print(line,end = "")
        #         break
        # except StopIteration:
        #     print("見つかりませんでした")
        #     break
