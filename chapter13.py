# file = "test.txt"
# fileobj = open(file)
# text = fileobj.read()
# fileobj.close()
# print(text)

# with open(file) as fileobj:
#     text = fileobj.read()
#     newtext = text.split(" ")
#     print(newtext)

import sys
# arglist = sys.argv
# print(arglist)
if len(sys.argv)<2:
    print("読み込みができませんでした")
    sys.exit()

file = sys.argv[1]
with open(file) as fileobj:
    data = fileobj.read()
    print(data)