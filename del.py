import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

inputFile = input("Name File: ")
myFile = open(f"{inputFile}", "r")
mfile = myFile.read()
remove = mfile[2:-1]
myFile.close()

saveFile = open("Completed.txt", "w")
data = remove
saveFile.write(data)
saveFile.close()

print("Completed ^_^")
